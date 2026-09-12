"""CLI for loading a prepared CSV into PostgreSQL."""

from __future__ import annotations

import argparse
from pathlib import Path

from customer_analytics.db import load_customer_table


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Load prepared customer data into PostgreSQL.")
    parser.add_argument("--input", type=Path, default=Path("outputs/customer_clean.csv"))
    parser.add_argument("--table", default=None)
    args = parser.parse_args()
    load_customer_table(args.input, args.table)
