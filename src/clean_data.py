import pandas as pd
from pathlib import Path


PROJECT_FOLDER = Path(__file__).resolve().parent.parent

RAW_FILE = PROJECT_FOLDER / "data" / "raw" / "lagos_rent_sample.csv"
CLEANED_FILE = PROJECT_FOLDER / "data" / "cleaned" / "lagos_rent_cleaned.csv"


def clean_rent_data():
    rent_data = pd.read_csv(RAW_FILE)

    print(f"Rows before cleaning: {len(rent_data)}")

    # Remove extra spaces from column names
    rent_data.columns = rent_data.columns.str.strip().str.lower()

    # Clean text columns
    rent_data["location"] = (
        rent_data["location"]
        .astype(str)
        .str.strip()
        .str.title()
    )

    rent_data["property_type"] = (
        rent_data["property_type"]
        .astype(str)
        .str.strip()
        .str.title()
    )

    # Convert number columns into numeric values
    number_columns = [
        "bedrooms",
        "bathrooms",
        "annual_rent",
    ]

    for column in number_columns:
        rent_data[column] = pd.to_numeric(
            rent_data[column],
            errors="coerce",
        )

    # Remove incomplete, duplicated or invalid rows
    rent_data = rent_data.dropna()
    rent_data = rent_data.drop_duplicates()

    rent_data = rent_data[
        (rent_data["bedrooms"] > 0)
        & (rent_data["bathrooms"] > 0)
        & (rent_data["annual_rent"] > 0)
    ]

    rent_data["bedrooms"] = rent_data["bedrooms"].astype(int)
    rent_data["bathrooms"] = rent_data["bathrooms"].astype(int)
    rent_data["annual_rent"] = rent_data["annual_rent"].astype(int)

    rent_data.to_csv(CLEANED_FILE, index=False)

    print(f"Rows after cleaning: {len(rent_data)}")
    print(f"Cleaned file saved to: {CLEANED_FILE}")


if __name__ == "__main__":
    clean_rent_data()