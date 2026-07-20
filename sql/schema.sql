DROP TABLE IF EXISTS rent_listings;

CREATE TABLE rent_listings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    location TEXT NOT NULL,
    property_type TEXT NOT NULL,
    bedrooms INTEGER NOT NULL,
    bathrooms INTEGER NOT NULL,
    annual_rent INTEGER NOT NULL
);