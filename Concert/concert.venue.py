def get_concert_venue(concert_id):
    query = """
    SELECT venues.* FROM concerts
    JOIN venues ON concerts.venue_id = venues.id
    WHERE concerts.id = ?
    """
    cur.execute(query, (concert_id,))
    return cur.fetchone()
