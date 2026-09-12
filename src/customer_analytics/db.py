"""PostgreSQL loading utilities driven by environment variables."""

from __future__ import annotations

import os
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine

load_dotenv()


def get_engine() -> Engine:
    """Create a PostgreSQL SQLAlchemy engine from .env settings."""
    required = ["DB_HOST", "DB_PORT", "DB_NAME", "DB_USER", "DB_PASSWORD"]
    missing = [name for name in required if not os.getenv(name)]
    if missing:
        raise RuntimeError(f"Missing database settings: {', '.join(missing)}")

    return create_engine(
        "postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}".format(
            user=os.environ["DB_USER"],
            password=os.environ["DB_PASSWORD"],
            host=os.environ["DB_HOST"],
            port=os.environ["DB_PORT"],
            database=os.environ["DB_NAME"],
        )
    )


def load_customer_table(csv_path: Path, table_name: str | None = None) -> None:
    """Load the prepared CSV into PostgreSQL, replacing the target table."""
    table = table_name or os.getenv("DB_TABLE", "customer")
    df = pd.read_csv(csv_path)
    engine = get_engine()
    df.to_sql(table, engine, if_exists="replace", index=False)
    with engine.connect() as connection:
        connection.execute(text(f'SELECT 1 FROM "{table}" LIMIT 1'))
    print(f"Loaded {len(df):,} rows into PostgreSQL table '{table}'.")
