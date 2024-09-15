Mock Code Challenge: Concerts Database
This project is designed to demonstrate your ability to manage a relational database with raw SQL queries. The challenge involves creating a database schema for managing concerts, bands, and venues, and implementing methods to interact with this data using Python’s sqlite3 library.

Overview
You are tasked with creating a database to store information about concerts, bands, and venues. The goal is to implement various methods to interact with and query this database using raw SQL.

Schema
bands Table

name (STRING): The name of the band.
hometown (STRING): The hometown of the band.
sql
Copy code
CREATE TABLE bands (
    name TEXT PRIMARY KEY,
    hometown TEXT
);
venues Table

title (STRING): The title of the venue.
city (STRING): The city where the venue is located.
sql
Copy code
CREATE TABLE venues (
    title TEXT PRIMARY KEY,
    city TEXT
);
concerts Table

id (INTEGER): Primary key for the concert record.
band_name (STRING): Foreign key referencing bands.name.
venue_title (STRING): Foreign key referencing venues.title.
date (STRING): Date of the concert.
sql
Copy code
CREATE TABLE concerts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    band_name TEXT,
    venue_title TEXT,
    date TEXT,
    FOREIGN KEY (band_name) REFERENCES bands(name),
    FOREIGN KEY (venue_title) REFERENCES venues(title)
);
Setup
Database Initialization

Create the database schema by executing the SQL commands above.
Insert Sample Data

Use the following SQL commands to populate the database with sample data:
sql
Copy code
-- Insert bands
INSERT INTO bands (name, hometown) VALUES ('The Rockers', 'Nashville');
INSERT INTO bands (name, hometown) VALUES ('The Jazz Cats', 'New Orleans');

-- Insert venues
INSERT INTO venues (title, city) VALUES ('The Big Arena', 'Nashville');
INSERT INTO venues (title, city) VALUES ('Jazz Club', 'New Orleans');

-- Insert concerts
INSERT INTO concerts (band_name, venue_title, date) VALUES ('The Rockers', 'The Big Arena', '2024-09-15');
INSERT INTO concerts (band_name, venue_title, date) VALUES ('The Jazz Cats', 'Jazz Club', '2024-09-16');
Python Methods
Implement the following methods to interact with the database. Ensure you have the sqlite3 library installed.

Connecting to the Database
python
Copy code
import sqlite3

conn = sqlite3.connect('concerts.db')
cursor = conn.cursor()
Methods
Retrieve All Concerts for a Band

python
Copy code
def band_concerts(band_name):
    query = 'SELECT * FROM concerts WHERE band_name = ?'
    cursor.execute(query, (band_name,))
    return cursor.fetchall()
Retrieve All Concerts for a Venue

python
Copy code
def venue_concerts(venue_title):
    query = 'SELECT * FROM concerts WHERE venue_title = ?'
    cursor.execute(query, (venue_title,))
    return cursor.fetchall()
Retrieve All Venues for a Band

python
Copy code
def band_venues(band_name):
    query = '''
    SELECT DISTINCT v.*
    FROM venues v
    JOIN concerts c ON v.title = c.venue_title
    WHERE c.band_name = ?
    '''
    cursor.execute(query, (band_name,))
    return cursor.fetchall()
Retrieve All Bands for a Venue

python
Copy code
def venue_bands(venue_title):
    query = '''
    SELECT DISTINCT b.*
    FROM bands b
    JOIN concerts c ON b.name = c.band_name
    WHERE c.venue_title = ?
    '''
    cursor.execute(query, (venue_title,))
    return cursor.fetchall()
Check if a Concert is in the Band's Hometown

python
Copy code
def concert_hometown_show(concert_id):
    query = '''
    SELECT 
        CASE
            WHEN v.city = b.hometown THEN 'true'
            ELSE 'false'
        END AS hometown_show
    FROM concerts c
    JOIN bands b ON c.band_name = b.name
    JOIN venues v ON c.venue_title = v.title
    WHERE c.id = ?
    '''
    cursor.execute(query, (concert_id,))
    return cursor.fetchone()[0] == 'true'
Get the Band’s Introduction for a Concert

python
Copy code
def concert_introduction(concert_id):
    query = '''
    SELECT 'Hello ' || v.city || '!!!!! We are ' || b.name || ' and we\'re from ' || b.hometown AS introduction
    FROM concerts c
    JOIN bands b ON c.band_name = b.name
    JOIN venues v ON c.venue_title = v.title
    WHERE c.id = ?
    '''
    cursor.execute(query, (concert_id,))
    return cursor.fetchone()[0]
Create a New Concert for a Band at a Venue

python
Copy code
def band_play_in_venue(band_name, venue_title, date):
    query = 'INSERT INTO concerts (band_name, venue_title, date) VALUES (?, ?, ?)'
    cursor.execute(query, (band_name, venue_title, date))
    conn.commit()
Get All Introductions for a Band

python
Copy code
def band_all_introductions(band_name):
    query = '''
    SELECT 'Hello ' || v.city || '!!!!! We are ' || b.name || ' and we\'re from ' || b.hometown AS introduction
    FROM concerts c
    JOIN bands b ON c.band_name = b.name
    JOIN venues v ON c.venue_title = v.title
    WHERE b.name = ?
    '''
    cursor.execute(query, (band_name,))
    return cursor.fetchall()
Get the Band with the Most Concerts

python
Copy code
def band_most_performances():
    query = '''
    SELECT b.name
    FROM bands b
    JOIN concerts c ON b.name = c.band_name
    GROUP BY b.name
    ORDER BY COUNT(c.id) DESC
    LIMIT 1
    '''
    cursor.execute(query)
    return cursor.fetchone()[0]
Find the First Concert on a Specific Date at a Venue

python
Copy code
def venue_concert_on(venue_title, date):
    query = 'SELECT * FROM concerts WHERE venue_title = ? AND date = ? LIMIT 1'
    cursor.execute(query, (venue_title, date))
    return cursor.fetchone()
Get the Most Frequent Band at a Venue

python
Copy code
def venue_most_frequent_band(venue_title):
    query = '''
    SELECT b.name
    FROM bands b
    JOIN concerts c ON b.name = c.band_name
    WHERE c.venue_title = ?
    GROUP BY b.name
    ORDER BY COUNT(c.id) DESC
    LIMIT 1
    '''
    cursor.execute(query, (venue_title,))
    return cursor.fetchone()[0]
Running the Code
Ensure you have Python installed with the sqlite3 library.
Create the database and tables using the provided schema.
Insert the sample data into the database.
Implement the methods in your Python script.
Test the methods by calling them with appropriate arguments.
License
This project is licensed under the MIT License.

