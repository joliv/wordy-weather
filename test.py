import zip_codes as z
import weather as w

# zip_codes.zip_check()
def test_notzipcheck1():
	assert z.is_listed('notlisted') is False

def test_notzipcheck2():
	assert z.is_listed('92348') is False

def test_zipcheck1():
	assert z.is_listed('20815') is True

def test_zip_check2():
	assert z.is_listed('90210') is True

def test_zip_check3():
	assert z.is_listed('55057') is True


# zip_codes.station_zone()
def test_station_zone_20815():
	assert z.station_zone('20815') == ('kdca', 'dcz001')

def test_station_zone_90210():
	assert z.station_zone('90210') == ('ksmo', 'caz547')

def test_station_zone_55057():
	assert z.station_zone('55057') == ('ksyn', 'mnz077')

# zip_codes.city()
def test_city_20815():
	assert z.city('20815') == ['chevy chase']

def test_city_90210():
	assert z.city('90210') == ['beverly hills']

def test_city_55057():
	assert z.city('55057') == ['northfield']

# zip_codes.url()

def test_url_dcz001():
	assert z.url('dcz001') == 'http://weather.noaa.gov/pub/data/forecasts/zone/dc/dcz001.txt'

def test_url_mnz077():
	assert z.url('mnz077') == 'http://weather.noaa.gov/pub/data/forecasts/zone/mn/mnz077.txt'

def test_url_caz547():
	assert z.url('caz547') == 'http://weather.noaa.gov/pub/data/forecasts/zone/ca/caz547.txt'

# weather.forecast_txt

def test_forecast_txt_20815():
	assert w.forecast_txt('20815')[-2] == '$$\n'

def test_forecast_txt_90210():
	assert w.forecast_txt('90210')[-2] == '$$\n'

def test_forecast_txt_20006():
	assert w.forecast_txt('20006')[-2] == '$$\n'

def test_forecast_txt_55057():
	assert w.forecast_txt('55057')[-2] == '$$\n'

# weather.parse()

test_data = [
	'Expires:201401222100;;831272\n',
	'FPUS51 KLWX 221730\n',
	'ZFPLWX\n',
	'ZONE FORECAST PRODUCT\n',
	'NATIONAL WEATHER SERVICE BALTIMORE MD/WASHINGTON DC\n',
	'1230 PM EST WED JAN 22 2014\n',
	'\n',
	'DCZ001-VAZ054-222100-\n',
	'DISTRICT OF COLUMBIA-ARLINGTON/FALLS CHURCH/ALEXANDRIA-\n',
	'INCLUDING THE CITIES OF...WASHINGTON...ALEXANDRIA...FALLS CHURCH\n',
	'1230 PM EST WED JAN 22 2014\n',
	'.THIS AFTERNOON...MOSTLY SUNNY. COOLER WITH HIGHS AROUND 14.\n',
	'NORTHWEST WINDS 10 TO 15 MPH WITH GUSTS UP TO 25 MPH. WIND CHILL\n',
	'VALUES AS LOW AS 5 BELOW. \n',
	'.TONIGHT...PARTLY CLOUDY IN THE EVENING...THEN BECOMING MOSTLY\n',
	'CLOUDY. COLD WITH LOWS AROUND 6 ABOVE. NORTHWEST WINDS 5 TO 10 MPH...\n',
	'BECOMING WEST AFTER MIDNIGHT. WIND CHILL VALUES AS LOW AS 2 BELOW. \n',
	'.THURSDAY...MOSTLY CLOUDY IN THE MORNING...THEN PARTLY SUNNY WITH A\n',
	'SLIGHT CHANCE OF SNOW SHOWERS IN THE AFTERNOON. HIGHS IN THE LOWER\n',
	'20S. SOUTHWEST WINDS AROUND 5 MPH...INCREASING TO WEST 10 TO 15 MPH\n',
	'IN THE AFTERNOON. CHANCE OF SNOW 20 PERCENT. \n',
	'.THURSDAY NIGHT...PARTLY CLOUDY IN THE EVENING...THEN CLEARING. COLD\n',
	'WITH LOWS AROUND 10 ABOVE. NORTHWEST WINDS 10 TO 15 MPH. WIND CHILL\n',
	'VALUES AS LOW AS 1 BELOW. \n',
	'.FRIDAY...SUNNY. HIGHS IN THE LOWER 20S. WEST WINDS AROUND 10 MPH.\n',
	'WIND CHILL VALUES AS LOW AS 2 BELOW IN THE MORNING. \n',
	'.FRIDAY NIGHT...MOSTLY CLOUDY. LOWS AROUND 15. \n',
	'.SATURDAY...MOSTLY CLOUDY. HIGHS IN THE UPPER 30S. \n',
	'.SATURDAY NIGHT...PARTLY CLOUDY. LOWS AROUND 20. \n',
	'.SUNDAY...MOSTLY SUNNY. HIGHS IN THE MID 30S. \n',
	'.SUNDAY NIGHT...PARTLY CLOUDY. LOWS IN THE LOWER 20S. \n',
	'.MONDAY...PARTLY SUNNY. HIGHS IN THE LOWER 30S. \n',
	'.MONDAY NIGHT...PARTLY CLOUDY. COLD WITH LOWS 5 TO 10 ABOVE. WIND\n',
	'CHILL VALUES AS LOW AS ZERO. \n',
	'.TUESDAY...MOSTLY SUNNY. HIGHS AROUND 20. \n',
	'$$\n',
	'\n'
]

parsed = ([],
	[('this afternoon',
		['mostly sunny. cooler with highs around 14. northwest winds 10 to 15 mph with gusts up to 25 mph. wind chill values as low as 5 below.']),
	('tonight',
		['partly cloudy in the evening',
		'then becoming mostly cloudy. cold with lows around 6 above. northwest winds 5 to 10 mph',
		'becoming west after midnight. wind chill values as low as 2 below.']),
	('thursday',
		['mostly cloudy in the morning',
		'then partly sunny with a slight chance of snow showers in the afternoon. highs in the lower 20s. southwest winds around 5 mph',
		'increasing to west 10 to 15 mph in the afternoon. chance of snow 20 percent.']),
	('thursday night',
		['partly cloudy in the evening',
		'then clearing. cold with lows around 10 above. northwest winds 10 to 15 mph. wind chill values as low as 1 below.']),
	('friday',
		['sunny. highs in the lower 20s. west winds around 10 mph. wind chill values as low as 2 below in the morning.']),
	('friday night', ['mostly cloudy. lows around 15.']),
	('saturday', ['mostly cloudy. highs in the upper 30s.']),
	('saturday night', ['partly cloudy. lows around 20.']),
	('sunday', ['mostly sunny. highs in the mid 30s.']),
	('sunday night', ['partly cloudy. lows in the lower 20s.']),
	('monday', ['partly sunny. highs in the lower 30s.']),
	('monday night',
		['partly cloudy. cold with lows 5 to 10 above. wind chill values as low as zero.'])],
	['national weather service baltimore md/washington dc',
	'1230 pm est wed jan 22 2014'])

def test_parse():
	assert w.parse(test_data) == parsed