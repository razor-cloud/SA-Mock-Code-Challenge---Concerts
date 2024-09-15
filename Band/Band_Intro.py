def band_all_introductions(band_id):
    query = cur.execute(query, (band_id,))
    concert_ids = cur.fetchall()
    
    introductions = []
    for concert_id in concert_ids:
        introductions.append(concert_introduction(concert_id[0]))
    
    return introductions

def test_band_all_introductions():
    print("Testing Band.all_introductions()")
    result = band_all_introductions(1)  # Band A's introductions
    for intro in result:
        print(intro)  # Expected output: Introduction for each concert

test_band_all_introductions()