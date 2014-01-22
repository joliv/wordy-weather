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

def city(zip_code):
	query = (zip_code,)
	conn = sqlite3.connect('zip_codes.db')
	c = conn.cursor()
	c.execute('SELECT city FROM cities WHERE zipcode=?',query)
	names = []
	for name in c.fetchall():
		lowercased = name[0].lower()
		if not lowercased in names:
			names.append(lowercased)
	return names

def url(zone):
	query = (zone,)
	conn = sqlite3.connect('zip_codes.db')
	c = conn.cursor()
	c.execute('SELECT forecast FROM zones WHERE zone=?',query)
	return c.fetchone()[0]
