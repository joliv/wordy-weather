import zip_codes
from urllib import request

def forecast_txt(zip_code):
	station_zone = zip_codes.station_zone(zip_code)
	zone = station_zone[1]
	url = zip_codes.url(zone)
	page = request.urlopen(url)
	txt = [line.decode() for line in page]
	return txt
