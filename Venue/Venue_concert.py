def venue_concerts(venue_id):
    query = cur.execute(query, (venue_id,))
    return cur.fetchall()

def test_concert_band():
    print("Testing Concert.band()")
    result = get_concert_band(1)  # Pass the ID of the concert
    print(result)  # Expected output: ('Band A', 'New York')

test_concert_band()
