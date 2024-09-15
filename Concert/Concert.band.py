def get_concert_band(concert_id):
    query = cur.execute(query, (concert_id,))
    return cur.fetchone()

