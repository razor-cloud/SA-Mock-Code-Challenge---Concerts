def band_play_in_venue(band_id, venue_id, date):
    query = cur.execute(query, (band_id, venue_id, date))
    conn.commit()

def test_band_venues():
    print("Testing Band.venues()")
    result = band_venues(1)  # Band A's venues
    print(result)  # Expected output: [('Venue 1', 'New York'), ('Venue 2', 'Los Angeles')]

test_band_venues()
