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
	txt = [line.replace('\n','').strip(' ').lower()
		for line in txt]
	start,end = day_range(txt)
	forecast = txt[start:end]
	meta = txt[4:6]
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
	unspaced = [
		[
			part.strip(' ')
			for part in line
		]
		for line in split
	]
	regrouped = [
		(line[0],line[1:])
		for line in unspaced
	]
	alerts = []
	remove = []
	for line in regrouped:
		if line[1]==['']:
			alerts.append(line[0])
			remove.append(line)
	for element in remove:
		regrouped.remove(element)
	return alerts,regrouped,meta
