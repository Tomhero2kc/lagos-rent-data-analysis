-- Remove extra spaces from text fields
UPDATE rent_listings
SET
    location = TRIM(location),
    property_type = TRIM(property_type);

-- Remove rows with missing values
DELETE FROM rent_listings
WHERE
    location IS NULL
    OR property_type IS NULL
    OR bedrooms IS NULL
    OR bathrooms IS NULL
    OR annual_rent IS NULL;

-- Remove invalid numerical values
DELETE FROM rent_listings
WHERE
    bedrooms <= 0
    OR bathrooms <= 0
    OR annual_rent <= 0;

-- Remove duplicate listings
DELETE FROM rent_listings
WHERE id NOT IN (
    SELECT MIN(id)
    FROM rent_listings
    GROUP BY
        location,
        property_type,
        bedrooms,
        bathrooms,
        annual_rent
);