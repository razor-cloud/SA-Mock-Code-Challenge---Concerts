def hometown_show(concert_id):
    query = cur.execute(query, (concert_id,))
    return cur.fetchone()[0] == 1

def test_hometown_show():
    print("Testing Concert.hometown_show()")
    result = hometown_show(1)  # Concert 1: Band A in Venue 1 (New York)
    print(result)  # Expected output: True

test_hometown_show()
