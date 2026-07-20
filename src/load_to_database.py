import sqlite3
from pathlib import Path

import pandas as pd


PROJECT_FOLDER = Path(__file__).resolve().parent.parent

CLEANED_FILE = (
    PROJECT_FOLDER
    / "data"
    / "cleaned"
    / "lagos_rent_cleaned.csv"
)

DATABASE_FILE = PROJECT_FOLDER / "data" / "lagos_rent.db"
SCHEMA_FILE = PROJECT_FOLDER / "sql" / "schema.sql"


def create_database():
    rent_data = pd.read_csv(CLEANED_FILE)
    schema = SCHEMA_FILE.read_text(encoding="utf-8")

    with sqlite3.connect(DATABASE_FILE) as connection:
        connection.executescript(schema)

        rent_data.to_sql(
            "rent_listings",
            connection,
            if_exists="append",
            index=False,
        )

    print("SQLite database created successfully.")
    print(f"{len(rent_data)} rent listings were added.")
    print(f"Database saved to: {DATABASE_FILE}")


if __name__ == "__main__":
    create_database()