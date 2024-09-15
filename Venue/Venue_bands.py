def venue_bands(venue_id):
    query = cur.execute(query, (venue_id,))
    return cur.fetchall()

def test_venue_bands():
    print("Testing Venue.bands()")
    result = venue_bands(1)  # Bands that performed at Venue 1
    print(result)  # Expected output: ['Band A']

test_venue_bands()
