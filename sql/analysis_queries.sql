-- Total number of listings
SELECT COUNT(*) AS total_listings
FROM rent_listings;

-- Overall rent summary
SELECT
    ROUND(AVG(annual_rent), 2) AS average_annual_rent,
    MIN(annual_rent) AS lowest_annual_rent,
    MAX(annual_rent) AS highest_annual_rent
FROM rent_listings;

-- Average rent by location
SELECT
    location,
    COUNT(*) AS number_of_listings,
    ROUND(AVG(annual_rent), 2) AS average_annual_rent
FROM rent_listings
GROUP BY location
ORDER BY average_annual_rent DESC;

-- Average rent by property type
SELECT
    property_type,
    COUNT(*) AS number_of_listings,
    ROUND(AVG(annual_rent), 2) AS average_annual_rent
FROM rent_listings
GROUP BY property_type
ORDER BY average_annual_rent DESC;

-- Average rent by number of bedrooms
SELECT
    bedrooms,
    COUNT(*) AS number_of_listings,
    ROUND(AVG(annual_rent), 2) AS average_annual_rent
FROM rent_listings
GROUP BY bedrooms
ORDER BY bedrooms;

-- Five most expensive listings
SELECT
    location,
    property_type,
    bedrooms,
    bathrooms,
    annual_rent
FROM rent_listings
ORDER BY annual_rent DESC
LIMIT 5;