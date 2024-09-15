def venue_most_frequent_band(venue_id):
    query = cur.execute(query, (venue_id,))
    return cur.fetchone()

def test_venue_most_frequent_band():
    print("Testing Venue.most_frequent_band()")
    result = venue_most_frequent_band(1)  # Most frequent band at Venue 1
    print(result)  # Expected output: Band A if it played the most at this venue

test_venue_most_frequent_band()
