import zip_codes
from urllib import request

def forecast_txt(zip_code):
	station_zone = zip_codes.station_zone(zip_code)
	zone = station_zone[1]
	url = zip_codes.url(zone)
	page = request.urlopen(url)
	txt = [line.decode() for line in page]
	return txt

def day_range(txt):
	for index,line in enumerate(txt):
		if line!='' and line.startswith('.'):
			begin = index
			end = txt.index('$$')-1
			return begin,end

def parse(txt):
	txt = [line.replace('\n','').strip(' ')
		for line in txt]
	start,end = day_range(txt)
	forecast = txt[start:end]
	forecast = [
		line.lower()
		for line in forecast
	]
	day_indices = [(i) for i,line in enumerate(forecast)
		if line.startswith('.')]
	grouped = [
		' '.join(forecast[day_index:day_indices[index+1]])
		for index,day_index in enumerate(day_indices)
		if index != len(day_indices)-1
	]
	grouped.append(
		' '.join(forecast[day_indices[-1]:])
	)
	cleaned = [
		line.lstrip('.')
		for line in grouped
	]
	split = [
		line.split('...')
		for line in cleaned
	]
	regrouped = [
		(line[0],"—".join(line[1:]))
		for line in split
	]
	return regrouped
