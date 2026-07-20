import sqlite3
from pathlib import Path


PROJECT_FOLDER = Path(__file__).resolve().parent.parent

DATABASE_FILE = PROJECT_FOLDER / "data" / "lagos_rent.db"
ANALYSIS_FILE = PROJECT_FOLDER / "sql" / "analysis_queries.sql"


def run_analysis_queries():
    sql_text = ANALYSIS_FILE.read_text(encoding="utf-8")

    queries = [
        query.strip()
        for query in sql_text.split(";")
        if query.strip()
    ]

    with sqlite3.connect(DATABASE_FILE) as connection:
        for number, query in enumerate(queries, start=1):
            cursor = connection.execute(query)

            column_names = [
                description[0]
                for description in cursor.description
            ]

            rows = cursor.fetchall()

            print(f"\nQuery {number}")
            print("-" * 60)
            print(" | ".join(column_names))

            for row in rows:
                print(" | ".join(str(value) for value in row))


if __name__ == "__main__":
    run_analysis_queries()