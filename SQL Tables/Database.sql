-- Create bands table
CREATE TABLE bands (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    hometown VARCHAR(255)
);

-- Create venues table
CREATE TABLE venues (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    city VARCHAR(255)
);

-- Create concerts table
CREATE TABLE concerts (
    id SERIAL PRIMARY KEY,
    band_id INTEGER REFERENCES bands(id),
    venue_id INTEGER REFERENCES venues(id),
    date VARCHAR(255)
);
