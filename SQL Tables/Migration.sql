-- Insert into bands
INSERT INTO bands (name, hometown) VALUES ('Band A', 'New York');
INSERT INTO bands (name, hometown) VALUES ('Band B', 'Los Angeles');

-- Insert into venues
INSERT INTO venues (title, city) VALUES ('Venue 1', 'New York');
INSERT INTO venues (title, city) VALUES ('Venue 2', 'Los Angeles');

-- Insert into concerts
INSERT INTO concerts (band_id, venue_id, date) VALUES (1, 1, '2023-05-01');
INSERT INTO concerts (band_id, venue_id, date) VALUES (1, 2, '2023-06-01');
INSERT INTO concerts (band_id, venue_id, date) VALUES (2, 2, '2023-07-01');
