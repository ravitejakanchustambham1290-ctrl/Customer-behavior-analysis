"""Command-line pipeline for preparing the customer dataset."""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from customer_analytics.transform import clean_customer_data


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Prepare customer shopping data.")
    parser.add_argument("--input", type=Path, default=Path("data/customer.csv"))
    parser.add_argument("--output", type=Path, default=Path("outputs/customer_clean.csv"))
    return parser


def main() -> None:
    args = build_parser().parse_args()
    df = pd.read_csv(args.input)
    cleaned = clean_customer_data(df)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    cleaned.to_csv(args.output, index=False)
    print(f"Prepared {len(cleaned):,} rows and {len(cleaned.columns):,} columns.")
    print(f"Saved: {args.output}")


if __name__ == "__main__":
    main()
