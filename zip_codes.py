import sqlite3

def is_listed(zip_code):
	query = (zip_code,)
	conn = sqlite3.connect('zip_codes.db')
	c = conn.cursor()
	c.execute('SELECT * FROM lookup WHERE zipcode=?',query)
	if c.fetchone() is None:
		return False
	return True

def station_zone(zip_code):
	query = (zip_code,)
	conn = sqlite3.connect('zip_codes.db')
	c = conn.cursor()
	c.execute('SELECT station,zone FROM lookup WHERE zipcode=?',query)
	return c.fetchone()