def band_concerts(band_id):
    query = cur.execute(query, (band_id,))
    return cur.fetchall()

def test_band_concerts():
    print("Testing Band.concerts()")
    result = band_concerts(1)  # Band A's concerts
    print(result)  # Expected output: [(1, 1, 1, '2023-05-01'), (2, 1, 2, '2023-06-01')]

test_band_concerts()
