def band_most_performances():
    query = cur.execute(query)
    return cur.fetchone()

def test_band_most_performances():
    print("Testing Band.most_performances()")
    result = band_most_performances()
    print(result)  # Expected output: Band A if it has the most concerts

test_band_most_performances()
