from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


PROJECT_FOLDER = Path(__file__).resolve().parent.parent

CLEANED_FILE = (
    PROJECT_FOLDER
    / "data"
    / "cleaned"
    / "lagos_rent_cleaned.csv"
)

CHARTS_FOLDER = PROJECT_FOLDER / "charts"


def analyse_rent_data():
    rent_data = pd.read_csv(CLEANED_FILE)

    print("\nLagos Rent Data Summary")
    print("-" * 35)

    average_rent = rent_data["annual_rent"].mean()
    median_rent = rent_data["annual_rent"].median()

    cheapest_property = rent_data.loc[
        rent_data["annual_rent"].idxmin()
    ]

    most_expensive_property = rent_data.loc[
        rent_data["annual_rent"].idxmax()
    ]

    print(f"Number of listings: {len(rent_data)}")
    print(f"Average annual rent: ₦{average_rent:,.0f}")
    print(f"Median annual rent: ₦{median_rent:,.0f}")

    print(
        "Cheapest listing: "
        f"{cheapest_property['location']} "
        f"at ₦{cheapest_property['annual_rent']:,.0f}"
    )

    print(
        "Most expensive listing: "
        f"{most_expensive_property['location']} "
        f"at ₦{most_expensive_property['annual_rent']:,.0f}"
    )

    average_by_property = (
        rent_data.groupby("property_type")["annual_rent"]
        .mean()
        .sort_values()
    )

    print("\nAverage Rent by Property Type")
    print(average_by_property.map(lambda rent: f"₦{rent:,.0f}"))

    create_property_type_chart(average_by_property)


def create_property_type_chart(average_by_property):
    CHARTS_FOLDER.mkdir(exist_ok=True)

    average_by_property.plot(
        kind="bar",
        title="Average Annual Rent by Property Type",
    )

    plt.xlabel("Property Type")
    plt.ylabel("Annual Rent in Naira")
    plt.xticks(rotation=0)
    plt.tight_layout()

    chart_file = CHARTS_FOLDER / "average_rent_by_property_type.png"

    plt.savefig(chart_file)
    plt.close()

    print(f"\nChart saved to: {chart_file}")


if __name__ == "__main__":
    analyse_rent_data()