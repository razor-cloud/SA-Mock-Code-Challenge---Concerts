import sqlite3

# Connect to the database
conn = sqlite3.connect('concerts.db')
cur = conn.cursor()
