# Lagos Rent Data Analysis

This is a small data analysis project I created to practise working with rental data using Python, Pandas, Matplotlib and SQL.

I used a sample of rental listings from different parts of Lagos. The project takes the data through a simple process: cleaning the CSV file, exploring rent prices, creating a chart and loading the cleaned data into a SQLite database for SQL analysis.

## Questions I Explored

- What is the average annual rent in the sample?
- What is the median annual rent?
- Which listing is the cheapest?
- Which listing is the most expensive?
- How does average rent differ by property type?
- How does rent vary across locations?
- Which listings are the five most expensive?

## Project Structure

```text
lagos-rent-data-analysis/
├── charts/
│   └── average_rent_by_property_type.png
├── data/
│   ├── raw/
│   │   └── lagos_rent_sample.csv
│   └── cleaned/
│       └── lagos_rent_cleaned.csv
├── notebooks/
│   └── lagos_rent_analysis.ipynb
├── sql/
│   ├── schema.sql
│   ├── cleaning_queries.sql
│   └── analysis_queries.sql
├── src/
│   ├── clean_data.py
│   ├── analyse_data.py
│   ├── load_to_database.py
│   └── run_sql_analysis.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Main Findings

The sample contains 10 rental listings.

- Average annual rent: **₦4,360,000**
- Median annual rent: **₦3,100,000**
- Cheapest listing: **Agege at ₦900,000**
- Most expensive listing: **Ikoyi at ₦12,000,000**

Apartments had the highest average rent, while mini flats had the lowest. The average rent was higher than the median because a few expensive listings increased the overall average.

This is a small practice dataset, so the findings should not be treated as a complete picture of the Lagos rental market.

## How to Run the Project

Install the required packages:

```bash
pip install -r requirements.txt
```

Clean the raw data:

```bash
python src/clean_data.py
```

Run the Python analysis and create the chart:

```bash
python src/analyse_data.py
```

Create the SQLite database:

```bash
python src/load_to_database.py
```

Run the SQL analysis:

```bash
python src/run_sql_analysis.py
```

You can also open the notebook:

```text
notebooks/lagos_rent_analysis.ipynb
```

## What I Practised

While working on this project, I practised:

- Reading and cleaning CSV data with Pandas
- Checking missing and duplicated values
- Grouping and summarising data
- Calculating averages and medians
- Creating and saving a bar chart
- Creating a SQLite database
- Writing SQL cleaning and analysis queries
- Organising a data project into folders
- Explaining findings in simple language