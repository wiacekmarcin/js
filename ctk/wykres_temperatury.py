#-*- encoding : utf-8 -*-
import sys, os
import datetime
import re

from PIL import Image, ImageDraw, ImageFont
from image_utils import ImageText

import numpy as np
from scipy.interpolate import splrep, splev

from urllib.request import urlopen
import json

from wt_check_avg_temp import getWarningTemp, getWarningWind, getWarningRain, getWarningSnow
from wt_calendar_events import getCalendarEvents
from wt_events_utils import organize_warning, sumWarnings, reduce_warning_temp, reduce_warning_rain, reduce_warning_snow, reduce_warning_wind
class Wykres:
	def __init__(self):
		self.daysName = [u'Niedziela',u'Poniedziałek',u'Wtorek',u'Środa',u'Czwartek',u'Piątek',u'Sobota']
		self.daysName2 = [u'poniedzialek',u'wtorek',u'sroda',u'czwartek',u'piatek',u'sobota',u'niedziela']
		self.monthName = ['','styczeń', 'luty', 'marzec', 'kwiecień', 'maj', 'czerwiec', 'lipiec', 'sierpień', 'wrzesień', 'pażdziernik', 'listopad', 'grudzień']
		self.font = ImageFont.truetype("Roboto-Slab-Regular.ttf", 14)
		self.fontW = ImageFont.truetype("weathericons-regular-webfont.ttf", 20)
		self.fontS = ImageFont.truetype("weathericons-regular-webfont.ttf", 14)
		self.iconMap = {}
		self.minDTemp = None
		self.maxDTemp = None
		self._initIconMap()


	def _initIconMap(self):
		self.iconMap["01d"]="\uf00d" #"wi-day-sunny",
		self.iconMap["02d"]="\uf002" #"wi-day-cloudy",
		self.iconMap["03d"]="\uf013" #"wi-cloudy",
		self.iconMap["04d"]="\uf012" #"wi-cloudy-windy",
		self.iconMap["09d"]="\uf01a" #"wi-showers",
		self.iconMap["10d"]="\uf019" #"wi-rain",
		self.iconMap["11d"]="\uf01e" #"wi-thunderstorm",
		self.iconMap["13d"]="\uf01b" #"wi-snow",
		self.iconMap["50d"]="\uf014" #"wi-fog",
		self.iconMap["01n"]="\uf02e" #"wi-night-clear",
		self.iconMap["02n"]="\uf031" #"wi-night-cloudy",
		self.iconMap["03n"]="\uf031" #"wi-night-cloudy",
		self.iconMap["04n"]="\uf031" #"wi-night-cloudy",
		self.iconMap["09n"]="\uf037" #"wi-night-showers",
		self.iconMap["10n"]="\uf036" #"wi-night-rain",
		self.iconMap["11n"]="\uf03b" #"wi-night-thunderstorm",
		self.iconMap["13n"]="\uf038" #"wi-night-snow",
		self.iconMap["50n"]="\uf023" #"wi-night-alt-cloudy-windy"

	def _getDaysName(self, days) -> str:
		dt = datetime.datetime.now()
		d1 = dt.date()
		d2 = d1 + datetime.timedelta(days)
		return "%s,  %d %s" % (self.daysName2[d2.weekday()], d2.day, self.monthName[d2.month])

	def _getEventDays(self, days:int, events:dict[datetime.date, list[str]]) -> list[str]:
		dt = datetime.datetime.now()
		d1 = dt.date()
		d2 = d1 + datetime.timedelta(days=days)
		return events.get(d2, [])

	
	def _createBackground(self, width, minTemp, maxTemp, h1deg, w3h, cnth, keys, pogodaPoints, 
					   events:dict[datetime.date, list[str]]) -> tuple[Image.Image, Image.Image, Image.Image]:
		print(events)

		height = (maxTemp - minTemp) * h1deg + 16
		margin = int((width-(cnth*w3h)) / 2)

		items = 0
		eheight = 0
		for e in events:
			items = max(items, len(events[e]))
		#eheight += items * 16 + 10 + 16
		eheight += items * (3*20) + 10 + 16
		print(eheight)
		height += eheight

		#im = Image.new("RGB", (width, height), color="black")
		im = Image.new("RGB", (width, height), color=0)
		draw = ImageDraw.Draw(im)
	
		#im2 = Image.new("RGB", (width, 50 + eheight), color="black")
		im2 = Image.new("RGB", (width, 50 + eheight), color=0)
		draw2 = ImageDraw.Draw(im2)
	
		#im3 = Image.new("RGB", (width, w3h), color="black")
		im3 = Image.new("RGB", (width, w3h), color=0)
		draw3 = ImageDraw.Draw(im3)

		hdeszcz = 50
		#im4 = Image.new("RGB", (width, hdeszcz), color="black")
		im4 = Image.new("RGB", (width, hdeszcz), color=0)
		draw4 = ImageDraw.Draw(im4)

		imgBox = ImageText(draw2, (w3h*8-5, 3*20), font=self.font)
		maxPos = 0
		for i in range(int(cnth)+1) :
			if i % 2 == 0:
				c = (40, 40, 40)
				if i == cnth:
					draw2.text((margin + w3h*i - 5, 0), "24", font=self.font, fill="white")
				else:
					draw2.text((margin + w3h*i, 0), "%d" % ((i*3) % 24), font=self.font, fill="white")
			else:
				c = (0, 0, 0)
			if int(i/8) % 2 == 1:
				c = (c[0]+20, c[1]+20, c[2]+20)
			draw.rectangle((margin + w3h*i, 0, margin + w3h*i+w3h*8, height), fill=c, outline=c, width=1)
			draw4.rectangle((margin + w3h*i, 0, margin + w3h*i+w3h*8, height), fill=c, outline=c, width=1)

			if i % 8 == 0 and i < 5*8:
				draw2.text((margin + w3h*i, 16), self._getDaysName(int(i/8)), font=self.font, fill="white")
				pos = 30 
				eventsList = self._getEventDays(int(i/8), events)
				for e in eventsList:
					#lines, widths = ImageDraw.textwrap(e, font=self.font, max_width=w3h*8-10)
					#draw2.text((margin + w3h*i, pos), e, font=self.font, fill="white")
					bx = imgBox.simple_write_text_box((margin + w3h*i, pos), e, '\xA0\xA0\xA0\xA0', "white")
					pos += bx[1]+2
				maxPos = max(maxPos, pos)

		#ydescH = hdeszcz/(math.log(300)+1)
		#ymzawka = hdeszcz - (math.log(0.75)+1)*ydescH
		#draw4.line((0, ymzawka, width, ymzawka), fill='blue', width=1)
		#draw4.text((0, ymzawka), "mzawka", fill='blue', font=font, direction='ttb')
		
		#ylekki = hdeszcz - (math.log(3)+1)*ydescH
		#draw4.line((0, ylekki, width, ylekki), fill='blue', width=1)
		#draw4.text((width-draw4.textlength("lekki deszcz", font=font), ylekki), "lekki deszcz", fill='blue', font=font, direction='ttb')
		
		#ydeszcz = hdeszcz - (math.log(12)+1)*ydescH
		#draw4.line((0, ydeszcz, width, ydeszcz), fill='blue', width=1)
		#draw4.text((0, ydeszcz), "deszcz", fill='blue', font=font, direction='ttb')

		#ysilny = hdeszcz - (math.log(120)+1)*ydescH
		#draw4.line((0, ysilny, width, ysilny), fill='blue', width=1)
		#draw4.text((width-draw4.textlength("deszcz ulewny", font=font), ysilny), "deszcz ulewny", fill='blue', font=font, direction='ttb')
		
		#yulewa = hdeszcz - (math.log(250)+1)*ydescH
		#draw4.line((0, yulewa, width, yulewa), fill='blue', width=1)
		#draw4.text((0, yulewa), "ulewa", fill='blue', font=font, direction='ttb')
		#im4.show()

		temp = maxTemp
		while temp >= minTemp:
			ypos = (maxTemp - temp)*h1deg
			wl = 1
			if temp == 0:
				wl = 3
			elif temp % 10 == 0:
				wl = 2
				
			draw.line(((margin, ypos), (width-margin, ypos)), fill='gray', width=wl)
			draw.text((0, ypos), "%d %s C" % (temp,'\u00B0'), font=self.font, fill="white")
			#draw.text((width-2*margin-20, ypos), "%d %s C" % (temp,'\u00B0'), font=font, fill="white")
			draw = ImageDraw.Draw(im)
			temp = temp - 5
		
	
		points1 = []
		points2 = []
		points3 = []
		points4 = []

		for x in range(len(keys)):
			k = keys[x]
			if not k in pogodaPoints or pogodaPoints[k] is None:
				continue
			temp = pogodaPoints[k]['temp']
			#tempmin = pogodaPoints[k]['temp_min']
			#tempmax = pogodaPoints[k]['temp_max']
			feelstemp = pogodaPoints[k]['feels_like']

			x0 = margin + w3h*x -1 -3
			y0 = (maxTemp-temp) * h1deg +1 -3
			x1 = x0 + 3
			y1 = y0 + 3
			#draw.ellipse((x0, y0, x1, y1), fill='white', outline='red', width=2)
			#points1.append((margin + w3h*x , (maxTemp-tempmin) * h1deg))
			#points2.append((margin + w3h*x , (maxTemp-tempmax) * h1deg))
			points3.append((margin + w3h*x , (maxTemp-feelstemp) * h1deg))
			points4.append((margin + w3h*x , (maxTemp-temp) * h1deg))
			draw3.text((x0,  y0), "%2.1f" % temp, font=self.fontS, fill="white")
			
			draw3.text((margin + w3h*x, 0), self.iconMap[pogodaPoints[k]['icon']], font=self.fontW, fill="white")
			
		
		#x1 = np.array([p[0] for p in points1])
		#y1 = np.array([p[1] for p in points1])

		#x2 = np.array([p[0] for p in points2])
		#y2 = np.array([p[1] for p in points2])

		x3 = np.array([p[0] for p in points3])
		y3 = np.array([p[1] for p in points3])

		x4 = np.array([p[0] for p in points4])
		y4 = np.array([p[1] for p in points4])

		#pl_1 = splrep(x1, y1)
		#f_1 = splev(x1, spl_1)

		#spl_2 = splrep(x2, y2)
		#f_2 = splev(x2, spl_2)

		spl_3 = splrep(x3, y3)
		f_3 = splev(x3, spl_3)

		spl_4 = splrep(x4, y4)
		f_4 = splev(x4, spl_4)

		#x_new1 = np.linspace(points1[0][0], points1[-1][0], (cnth+1)*w3h)
		#y_new1 = splev(x_new1, spl_1)

		#x_new2 = np.linspace(points2[0][0], points2[-1][0], (cnth+1)*w3h)
		#y_new2 = splev(x_new2, spl_2)
		
		x_new3 = np.linspace(points3[0][0], points3[-1][0], (cnth+1)*w3h)
		y_new3 = splev(x_new3, spl_3)

		x_new4 = np.linspace(points4[0][0], points4[-1][0], (cnth+1)*w3h)
		y_new4 = splev(x_new4, spl_4)

		#poly = []
		#for i in range(len(x_new1)):
		#	poly.append((x_new1[i], y_new1[i]))

		#for i in range(len(x_new2)):
		#	poly.append((x_new2[len(x_new2)-i-1], y_new2[len(x_new2)-i-1]))
		
		points3fix = []
		for i in range(len(x_new3)):
			points3fix.append((x_new3[i], y_new3[i]))

		points4fix = []
		for i in range(len(x_new4)):
			points4fix.append((x_new4[i], y_new4[i]))

		#draw.polygon(poly, fill="green", outline="green", width=3)
		#draw.polygon(poly, fill="green", outline="green", width=3)
		draw.line(points3fix, fill="red", width=3)
		draw.line(points4fix, fill="green", width=3)

		im2 = im2.crop((0, 0, width, maxPos))
		im = im.crop((0, 0, width, height - (eheight - maxPos)))
		return (im, im2, im3)

	def _getPoints(self, cnth) -> tuple[float, float, list[str], dict[datetime.datetime, dict], dict[datetime.date, list[str]]]:
		dt = datetime.date.today() 
		dta = datetime.datetime(dt.year, dt.month, dt.day, 0, 0, 0)
		keys = []
		pogodaPoints = {}
		for i in range(cnth+1):
			keys.append(str(dta))
			dta = dta + datetime.timedelta(hours=3)
			pogodaPoints[dta] = []
		#print (keys)

		tkeys = []
		dta = datetime.datetime(dt.year, dt.month, dt.day, 0, 0, 0)
		for i in range(cnth+1):
			if dta.year == dt.year and dta.month == dt.month and dta.day == dt.day:
				tkeys.append(str(dta))
			dta = dta + datetime.timedelta(hours=3)
			
		#print (tkeys)

		url = "https://api.openweathermap.org/data/2.5/forecast?appid=b176485875db690244cb8acf93637572&id=7532279&lang=pl&units=metric"
		response = urlopen(url)
		data_json = json.loads(response.read().decode('utf-8'))
		
		cnt_items = int(data_json["cnt"]) or 0
		if cnt_items == 0:
			print("Brak danych")
			return 0, 0, [], {}, {}

		items = data_json["list"]
		if items is None:
			print("Brak danych")
			return 0, 0, [], {}, {}

		minTemp = None
		maxTemp = None

		t_minTemp = None
		t_maxTemp = None

		tf_minTemp = None
		tf_maxTemp = None

		idx = 0
		rainwarning_time = []
		snowwarning_time = []
		tempwarning_time = []
		windwarning_time = []

		tdregex=re.compile("^%d-%02d-%02d .*$" % (dt.year, dt.month, dt.day))

		rainMap = {
			'słabe opady deszczu' : 'słaby deszcz',
			'intensywne opady deszczu' : 'intensywny deszcz',
		}

		for i in items:
			dt_txt = i["dt_txt"]

			if i["dt_txt"] is None:
				continue

		
			m = i['main']
			if not dt_txt in keys:
				continue
			
			w = i['weather']

			if w is None:
				main = ''
				description = ''
				icon = ''
			else:
				main = w[0]['main']
				description = w[0]['description']
				icon = w[0]['icon']
		
			pogodaPoints[dt_txt] = {
				'temp' : m['temp'],
				'feels_like' : m['feels_like'],
				'temp_min' : m['temp_min'],
				'temp_max' : m['temp_max'],
				'pressure' : m['pressure'],
				'humidity' : m['humidity'],
				'main' : main,
				'description' : description,
				'icon' : icon,
				}
			
			
			if 'rain' in i.keys():
				rain_mm = float(i['rain']["3h"])
			else:
				rain_mm = None
			
			if 'snow' in i.keys():
				snow_mm = float(i['snow']["3h"])
			else:
				snow_mm = None

			if icon in ['09d', '09n', '10d', '10n', '11d', '11n', '13d', '13n',  '50d', '50n']:
				if rain_mm is not None:
					rainwarning_time.append((dt_txt, (getWarningRain(rain_mm), rain_mm)))

				if snow_mm is not None:
					snowwarning_time.append((dt_txt, (getWarningSnow(snow_mm), snow_mm)))
			if 'wind' in i.keys():
				r = getWarningWind(float(i['wind']['speed']), float(i['wind']['gust'])) 
				if r[0]:
					windwarning_time.append((dt_txt, r[1:]))	

			r = getWarningTemp(float(m['temp']), dt_txt)
			if r[0]:
				tempwarning_time.append((dt_txt, r[1:]))		
		

			if tdregex.match(dt_txt):
				if self.minDTemp is None:
					self.minDTemp = float(m['temp'])
				elif float(m['temp']) < self.minDTemp:
					self.minDTemp = float(m['temp'])

				if self.maxDTemp is None:
					self.maxDTemp = float(m['temp'])
				elif float(m['temp']) > self.maxDTemp:
					self.maxDTemp = float(m['temp'])

			if minTemp is None or minTemp > float(m['temp_min']) :
				minTemp = float(m['temp_min'])
			
			if maxTemp is None or maxTemp < float(m['temp_max']) :
				maxTemp = float(m['temp_max'])

			if float(m['temp']) < minTemp:
				minTemp = float(m['temp'])
			
			if float(m['feels_like']) < minTemp:
				minTemp = float(m['feels_like'])

			if float(m['temp']) > maxTemp:
				maxTemp = float(m['temp'])
			
			if float(m['feels_like']) > maxTemp:
				maxTemp = float(m['feels_like'])

			if dt_txt in tkeys:
				if t_minTemp is None or t_minTemp > float(m['temp_min']) :
					t_minTemp = float(m['temp_min'])
				
				if t_maxTemp is None or t_maxTemp < float(m['temp_max']) :
					t_maxTemp = float(m['temp_max'])

				if tf_minTemp is None or tf_minTemp > float(m['temp_min']) :
					tf_minTemp =float(m['temp_min'])
				
				if tf_maxTemp is None or tf_maxTemp < float(m['temp_max']) :
					tf_maxTemp = m['temp_max']

				if float(m['temp']) < t_minTemp:
					t_minTemp = float(m['temp'])
				
				if float(m['feels_like']) < tf_minTemp:
					tf_minTemp = float(m['feels_like'])

				if float(m['temp']) > t_maxTemp:
					t_maxTemp = float(m['temp'])
				
				if float(m['feels_like']) > tf_maxTemp:
					tf_maxTemp = float(m['feels_like'])

		#print(t_minTemp, t_maxTemp, tf_minTemp, tf_maxTemp)
		warning_time_0 = organize_warning(rainwarning_time, reduce_warning_rain)
		warning_time_1 = organize_warning(snowwarning_time, reduce_warning_snow)
		warning_time_2 = organize_warning(tempwarning_time, reduce_warning_temp)
		warning_time_3 = organize_warning(windwarning_time, reduce_warning_wind)

		#tempwarning_time_1 = self._organize_tempwarning(upal_warning_time, False)
		#tempwarning_time_2 = self._organize_tempwarning(mroz_warning_time, True)

		#return_warnings = sumWarnings([warning_time_O, warning_time_1])
		return_warnings = sumWarnings([warning_time_0, warning_time_1, warning_time_2, warning_time_3])
		
		#print(warning_time_O)
		#print(tempwarning_time_1)
		#print(tempwarning_time_2)
		#print(return_warnings)
		if minTemp is None:
			minTemp = 0
		if maxTemp is None:
			maxTemp = 20
			
		return minTemp, maxTemp, keys, pogodaPoints, return_warnings

	def _createWykres(self, minTemp, maxTemp, maxTempG, width, h1deg, im, imL, imI) -> Image.Image:
		height1 = int((maxTemp - minTemp)*h1deg)
		height2 = int(imL.size[1])
		height3 = int(imI.size[1])
		
		height = height1 + height2 + height3
		
		#imB = Image.new("RGB", (width, height), color="black")
		imB = Image.new("RGB", (width, height), color=0)
		boxc = (0, int((maxTempG - maxTemp)* h1deg), width, int((maxTempG - minTemp)* h1deg))
		imc = im.crop(boxc)
		x1, y1 = imc.size
		
		draw = ImageDraw.Draw(imc)
		
		boxp1 = (0, 0, x1, y1)
		imB.paste(imc, boxp1)
		
		x2, y2 = imI.size
		boxp2 = (0, y1+1, x2, y1+1+y2)
		imB.paste(imI, boxp2)
		
		x3, y3 = imL.size
		boxp3 = (0, y1+1+height3, x3, y1+1+height3+height2)
		imB.paste(imL, boxp3)
		
		#fpath = os.path.join("/home/pi/tmp", str(datetime.date.today()).replace(":","_").replace(" ", "_").replace("-","_")) + ".png"
		#print(fpath)
		#imB.save(fpath)
		return imB
		imB.show()
	
	def createImage(self) -> Image.Image:
		width = 1080
		maxTemp = 40
		minTemp = -30
		h1deg = 10
		w3h = 27
		cnth = int(24/3*5)

		minT, maxT, keys, pogodaPoints, events = self._getPoints(cnth)
		#print(f"{width}, {minTemp}, {maxTemp}, {h1deg}, {w3h}, {cnth}, {keys}, {pogodaPoints}")

		wydarzenia : dict[datetime.datetime, list[str]] = getCalendarEvents()
		for w in wydarzenia:
			if w not in events:
				events[w] = []
			else:
				events[w].append("=-=-=-=-=-=-=-=")	
			for e in wydarzenia[w]:
				events[w].append(e)	
		
		im, imL, imI = self._createBackground(width, minTemp, maxTemp, h1deg, w3h, cnth, keys, pogodaPoints, events)
		
		return self._createWykres(minT-2, maxT+2, maxTemp, width, h1deg, im, imL, imI)



#w = Wykres()
#w.createImage().show()
