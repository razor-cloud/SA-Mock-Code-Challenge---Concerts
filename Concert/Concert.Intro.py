def concert_introduction(concert_id):
    query = cur.execute(query, (concert_id,))
    result = cur.fetchone()
    return f"Hello {result[2]}!!!!! We are {result[0]} and we're from {result[1]}"

def test_concert_venue():
    print("Testing Concert.venue()")
    result = get_concert_venue(1)
    print(result)  # Expected output: ('Venue 1', 'New York')

test_concert_venue()
