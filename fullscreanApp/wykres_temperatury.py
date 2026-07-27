#-*- encoding : utf-8 -*-
import sys, os
import datetime
import math

from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageColor


import numpy as np
from scipy.interpolate import splrep, splev

from urllib.request import urlopen
import json

font = ImageFont.truetype("/home/pi/fullscreanApp/fonts/roboto-slab/Roboto-Slab-Regular.ttf", 14)
daysName = [u'Niedziela',u'Poniedziałek',u'Wtorek',u'Środa',u'Czwartek',u'Piątek',u'Sobota']
fontW = ImageFont.truetype("/home/pi/fullscreanApp/fonts/weathericons-regular-webfont.ttf", 20)
fontS = ImageFont.truetype("/home/pi/fullscreanApp/fonts/weathericons-regular-webfont.ttf", 14)

iconMap = {}
iconMap["01d"]="\uf00d" #"wi-day-sunny",
iconMap["02d"]="\uf002" #"wi-day-cloudy",
iconMap["03d"]="\uf013" #"wi-cloudy",
iconMap["04d"]="\uf012" #"wi-cloudy-windy",
iconMap["09d"]="\uf01a" #"wi-showers",
iconMap["10d"]="\uf019" #"wi-rain",
iconMap["11d"]="\uf01e" #"wi-thunderstorm",
iconMap["13d"]="\uf01b" #"wi-snow",
iconMap["50d"]="\uf014" #"wi-fog",
iconMap["01n"]="\uf02e" #"wi-night-clear",
iconMap["02n"]="\uf031" #"wi-night-cloudy",
iconMap["03n"]="\uf031" #"wi-night-cloudy",
iconMap["04n"]="\uf031" #"wi-night-cloudy",
iconMap["09n"]="\uf037" #"wi-night-showers",
iconMap["10n"]="\uf036" #"wi-night-rain",
iconMap["11n"]="\uf03b" #"wi-night-thunderstorm",
iconMap["13n"]="\uf038" #"wi-night-snow",
iconMap["50n"]="\uf023" #"wi-night-alt-cloudy-windy"

def getDaysName(days):
	dt = datetime.datetime.now()
	d1 = dt.date()
	d2 = d1 + datetime.timedelta(days)
	return "%s,  %d-%s" % ([u'poniedzialek',u'wtorek',u'sroda',u'czwartek',u'piatek',u'sobota',u'niedziela'][d2.weekday()],
					  d2.day, 
					  ['','I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII'][d2.month])

def createBackground(width, minTemp, maxTemp, h1deg, w3h, cnth, keys, pogodaPoints):
	
	height = (maxTemp - minTemp) * h1deg + 16
	margin = int((width-(cnth*w3h)) / 2)

	im = Image.new("RGB", (width, height), color="black")
	draw = ImageDraw.Draw(im)
	
	im2 = Image.new("RGB", (width, 50), color="black")
	draw2 = ImageDraw.Draw(im2)
	
	im3 = Image.new("RGB", (width, w3h), color="black")
	draw3 = ImageDraw.Draw(im3)

	hdeszcz = 50
	im4 = Image.new("RGB", (width, hdeszcz), color="black")
	draw4 = ImageDraw.Draw(im4)
	
	for i in range(int(cnth)+1) :
		if i % 2 == 0:
			c = (40, 40, 40)
			if i == cnth:
				draw2.text((margin + w3h*i - 5, 0), "24", font=font, fill="white")
			else:
				draw2.text((margin + w3h*i, 0), "%d" % ((i*3) % 24), font=font, fill="white")
		else:
			c = (0, 0, 0)
		if int(i/8) % 2 == 1:
			c = (c[0]+20, c[1]+20, c[2]+20)
		draw.rectangle((margin + w3h*i, 0, margin + w3h*i+w3h*8, height), fill=c, outline=c, width=1)
		draw4.rectangle((margin + w3h*i, 0, margin + w3h*i+w3h*8, height), fill=c, outline=c, width=1)

		if i % 8 == 0 and i < 5*8:
			draw2.text((margin + w3h*i, 16), getDaysName(int(i/8)), font=font, fill="white")

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
		draw.text((0, ypos), "%d %s C" % (temp,'\u00B0'), font=font, fill="white")
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
		tempmin = pogodaPoints[k]['temp_min']
		tempmax = pogodaPoints[k]['temp_max']
		feelstemp = pogodaPoints[k]['feels_like']

		x0 = margin + w3h*x -1 -3
		y0 = (maxTemp-temp) * h1deg +1 -3
		x1 = x0 + 3
		y1 = y0 + 3
		draw.ellipse((x0, y0, x1, y1), fill='white', outline='red', width=2)
		points1.append((margin + w3h*x , (maxTemp-tempmin) * h1deg))
		points2.append((margin + w3h*x , (maxTemp-tempmax) * h1deg))
		points3.append((margin + w3h*x , (maxTemp-feelstemp) * h1deg))
		points4.append((margin + w3h*x , (maxTemp-temp) * h1deg))
		draw3.text((x0,  y0), "%2.1f" % temp, font=fontS, fill="white")
		
		draw3.text((margin + w3h*x, 0), iconMap[pogodaPoints[k]['icon']], font=fontW, fill="white")
		
		
		
	x1 = np.array([p[0] for p in points1])
	y1 = np.array([p[1] for p in points1])

	x2 = np.array([p[0] for p in points2])
	y2 = np.array([p[1] for p in points2])

	x3 = np.array([p[0] for p in points3])
	y3 = np.array([p[1] for p in points3])

	x4 = np.array([p[0] for p in points4])
	y4 = np.array([p[1] for p in points4])

	spl_1 = splrep(x1, y1)
	f_1 = splev(x1, spl_1)

	spl_2 = splrep(x2, y2)
	f_2 = splev(x2, spl_2)

	spl_3 = splrep(x3, y3)
	f_3 = splev(x3, spl_3)

	spl_4 = splrep(x4, y4)
	f_4 = splev(x4, spl_4)

	x_new1 = np.linspace(points1[0][0], points1[-1][0], (cnth+1)*w3h)
	y_new1 = splev(x_new1, spl_1)

	x_new2 = np.linspace(points2[0][0], points2[-1][0], (cnth+1)*w3h)
	y_new2 = splev(x_new2, spl_2)
	
	x_new3 = np.linspace(points3[0][0], points3[-1][0], (cnth+1)*w3h)
	y_new3 = splev(x_new3, spl_3)

	x_new4 = np.linspace(points4[0][0], points4[-1][0], (cnth+1)*w3h)
	y_new4 = splev(x_new4, spl_4)

	poly = []
	for i in range(len(x_new1)):
		poly.append((x_new1[i], y_new1[i]))

	for i in range(len(x_new2)):
		poly.append((x_new2[len(x_new2)-i-1], y_new2[len(x_new2)-i-1]))
	
	points3fix = []
	for i in range(len(x_new3)):
		points3fix.append((x_new3[i], y_new3[i]))

	points4fix = []
	for i in range(len(x_new4)):
		points4fix.append((x_new4[i], y_new4[i]))

	#draw.polygon(poly, fill="green", outline="green", width=3)
	#draw.polygon(poly, fill="green", outline="green", width=3)
	draw.line(points3fix, fill="red", width=2)
	draw.line(points4fix, fill="green", width=2)

	return (im, im2, im3)

def getPoints(cnth):
	dt = datetime.date.today() 
	dta = datetime.datetime(dt.year, dt.month, dt.day, 0, 0, 0)
	keys = []
	pogodaPoints = {}
	for i in range(cnth+1):
		keys.append(str(dta))
		dta = dta + datetime.timedelta(hours=3)
		pogodaPoints[dta] = None
	#print (keys)
	url = "https://api.openweathermap.org/data/2.5/forecast?appid=b176485875db690244cb8acf93637572&id=7532279&lang=pl&units=metric"
	response = urlopen(url)
	data_json = json.loads(response.read().decode('utf-8'))
	
	cnt_items = int(data_json["cnt"]) or 0
	if cnt_items == 0:
		print("Brak danych")
		return 0, 0, [], []

	items = data_json["list"]
	if items is None:
		print("Brak danych")
		return 0, 0, [], []

	minTemp = None
	maxTemp = None
	idx = 0
	
	for i in items:
		dt_txt = i["dt_txt"]
		#print(dt_txt)
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
		if minTemp is None or minTemp > m['temp_min'] :
			minTemp = m['temp_min']
		
		if maxTemp is None or maxTemp < m['temp_max'] :
			maxTemp = m['temp_max']

		if m['temp'] < minTemp:
			minTemp = m['temp']
		
		if m['feels_like'] < minTemp:
			minTemp = m['feels_like']

		if m['temp'] > maxTemp:
			maxTemp = m['temp']
		
		if m['feels_like'] > maxTemp:
			maxTemp = m['feels_like']
	
	return minTemp, maxTemp, keys, pogodaPoints
	

def createWykres(minTemp, maxTemp, maxTempG, width, h1deg, im, imL, imI):
	height1 = int((maxTemp - minTemp)*h1deg)
	height2 = int(imL.size[1])
	height3 = int(imI.size[1])
	
	height = height1 + height2 + height3
	
	imB = Image.new("RGB", (width, height), color="black")
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
	
	fpath = os.path.join("/home/pi/tmp", str(datetime.date.today()).replace(":","_").replace(" ", "_").replace("-","_")) + ".png"
	print(fpath)
	imB.save(fpath)
	#imB.show()
	

width = 1024
maxTemp = 40
minTemp = -30
h1deg = 10
w3h = 25
cnth = int(24/3*5)

minT, maxT, keys, pogodaPoints = getPoints(cnth)
#print(f"{width}, {minTemp}, {maxTemp}, {h1deg}, {w3h}, {cnth}, {keys}, {pogodaPoints}")
im, imL, imI = createBackground(width, minTemp, maxTemp, h1deg, w3h, cnth, keys, pogodaPoints)
if minT is not None and maxT is not None:
	createWykres(minT-2, maxT+2, maxTemp, width, h1deg, im, imL, imI)






"""


class Wykres:
	def __init__(self):
		self.url = "https://api.openweathermap.org/data/2.5/forecast?appid=b176485875db690244cb8acf93637572&id=7532279&lang=pl&units=metric"
		self.prevday = None
		self.delaySec = 0
		self.nodata = False
		self.minTemp = [None, None, None, None, None, None, None]
		self.maxTemp = [None, None, None, None, None, None, None]
		self.temp = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
		self.tempmin = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
		self.tempmax = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
		self.font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSansBold.ttf", 12)
		self.feelstemp = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
		self.minIdxTemp = [None, None, None, None, None, None, None]
		self.maxIdxTemp = [None, None, None, None, None, None, None]
		self.w3h = 25
		self.h1deg = 10
		self.maxRange = 30
		self.minRange = 10
		self.height = 300
		self.margin = int((1024-(8*5*self.w3h)) / 2)

		self.daysName = [u'Niedziela',u'Poniedzialek',u'Wtorek',u'Sroda',u'Czwartek',u'Piatek',u'Sobota']

	def timeout(self):
		response = urlopen(self.url)
		data_json = json.loads(response.read().decode('utf-8'))

		cnt_items = int(data_json["cnt"]) or 0
		if cnt_items == 0:
			print("Brak danych")
			return

		items = data_json["list"]
		if items is None:
			print("Brak danych")
			return

		self.minTempL = None
		self.maxTempL = None
		idx = 0
		for i in items:

			dt_txt = i["dt_txt"]
			if i["dt_txt"] is None:
				continue
			fd,ft = dt_txt.split(' ')
			year,month,day = fd.split('-')
			hour,minute,second = ft.split(':')
			day = int(day)
			#idt = int(i['dt'])
			#ih = (idt - tdt - offset)/3600
			#idx = ih/3

			m = i['main']
			self.add(idx, int(idx / 8), m['temp'],m['feels_like'],m['temp_min'],m['temp_max'],m['pressure'],m['humidity'])
			idx += 1

		self.show()

	def add(self, idx, day, temp, feelstemp, temp_min, temp_max, pressure, humidity):
		self.temp[int(idx)] = temp
		self.tempmin[int(idx)] = temp_min
		self.tempmax[int(idx)] = temp_max
		self.feelstemp[int(idx)] = feelstemp
		if self.minTemp[day] is None or self.minTemp[day] > temp_min:
			self.minTemp[day] = temp_min
			self.minIdxTemp[day] = idx
		if self.maxTemp[day] is None or self.maxTemp[day] < temp_max:
			self.maxTemp[day] = temp_max
			self.maxIdxTemp[day] = idx

	def show(self):
		width = 1024
		height = 300
		im = Image.new("RGB", (width+2*self.margin, height+100), color="black")
		draw = ImageDraw.Draw(im)

		print((self.margin, 5*self.h1deg, self.margin + width, 5*self.h1deg))
		x = []
		for i in range(8*5+1) :
			if i % 2 == 0:
				c = (40, 40, 40)
				if i == 8*5:
					draw.text((self.margin + self.w3h*i, self.height+16), "24", font=self.font, fill="white")
				else:
					draw.text((self.margin + self.w3h*i, self.height+16), "%d" % ((i*3) % 24), font=self.font, fill="white")
			else:
				c = (0, 0, 0)
			if int(i/8) % 2 == 1:
				c = (c[0]+20, c[1]+20, c[2]+20)
			draw.rectangle((self.margin + self.w3h*i, 0, self.margin + self.w3h*i+self.w3h*8, self.height), fill=c, outline=c, width=1)

			if i % 8 == 0 and i <= 5*8:
				draw.text((self.margin + self.w3h*i, self.height+32), self.daysName[int(i/8) % 7], font=self.font, fill="white")


			#if i > 16:
			#	break
		#im.show()
		#return
		draw.line(((self.margin, 0), (self.margin + width, 0)), fill='gray', width=2)
		draw.text((0, 0), "30", font=self.font, fill="white")
		draw.line(((self.margin, 5*self.h1deg), (self.margin + width, 5*self.h1deg)), fill='gray', width=1)
		draw.text((0, 5*self.h1deg), "25", font=self.font, fill="white")
		draw.line(((self.margin, 10*self.h1deg), (self.margin + width, 10*self.h1deg)), fill='gray', width=2)
		draw.text((0, 10*self.h1deg), "20", font=self.font, fill="white")
		draw.line(((self.margin, 15*self.h1deg), (self.margin + width, 15*self.h1deg)), fill='gray', width=1)
		draw.text((0, 15*self.h1deg), "15", font=self.font, fill="white")
		draw.line(((self.margin, 20*self.h1deg), (self.margin + width, 20*self.h1deg)), fill='gray', width=2)
		draw.text((0, 20*self.h1deg), "10", font=self.font, fill="white")
		draw.line(((self.margin, 25*self.h1deg), (self.margin + width, 25*self.h1deg)), fill='gray', width=1)
		draw.text((0, 25*self.h1deg), "5", font=self.font, fill="white")
		draw.line(((self.margin, 30*self.h1deg), (self.margin + width, 30*self.h1deg)), fill='gray', width=3)
		draw.text((0, 30*self.h1deg), "0", font=self.font, fill="white")
		points1 = []
		points2 = []
		points3 = []

		for x in range(len(self.temp)):
			if self.temp[x] is None:
				continue
			draw.ellipse((self.margin + self.w3h*x -1 , (30-self.temp[x]) * self.h1deg +1, 6, 6), fill='white', outline='red', width=2)
			points1.append((self.margin + self.w3h*x -1 , (30-self.tempmin[x]) * self.h1deg +1))
			points2.append((self.margin + self.w3h*x -1 , (30-self.tempmax[x]) * self.h1deg +1))
			points3.append((self.margin + self.w3h*x -1 , (30-self.feelstemp[x]) * self.h1deg +1))
			#if prev is None:
			#	prev = pos.center()
			#	continue

			#pl = QLineF(prev, pos.center())
			#l = scene.addLine(pl, pen)

			#if prev2 is None:
			#	prev2 = prev
			#	prev = pos.center()
			#	continue

			#if prev2.y() < prev.y()  and prev.y() > pos.center().y():
			#	t = scene.addText("%2.1f" % self.temp[x-1], self.font)
			#	t.setDefaultTextColor(QColor(255, 255, 255))
			#	t.setPos(prev)

			#if prev2.y() > prev.y()  and prev.y() < pos.center().y():
			#	t = scene.addText("%2.1f" % self.temp[x-1], self.font)
			#	t.setDefaultTextColor(QColor(255, 255, 255))
			#	t.setPos(prev - QPointF(0, 32))

			#prev2 = prev
			#prev = pos.center()

		x1 = np.array([p[0] for p in points1])
		y1 = np.array([p[1] for p in points1])

		x2 = np.array([p[0] for p in points2])
		y2 = np.array([p[1] for p in points2])

		x3 = np.array([p[0] for p in points3])
		y3 = np.array([p[1] for p in points3])

		spl_1 = splrep(x1, y1)
		f_1 = splev(x1, spl_1)

		spl_2 = splrep(x2, y2)
		f_2 = splev(x2, spl_2)

		spl_3 = splrep(x3, y3)
		f_3 = splev(x3, spl_3)



# Estimate values
		x_new1 = np.linspace(points1[0][0], points1[-1][0], (5*8+1)*self.w3h)
		y_new1 = splev(x_new1, spl_1)

		x_new2 = np.linspace(points2[0][0], points2[-1][0], (5*8+1)*self.w3h)
		y_new2 = splev(x_new2, spl_2)
		poly = []
		for i in range(len(x_new1)):
			poly.append((x_new1[i], y_new1[i]))

		for i in range(len(x_new2)):
			poly.append((x_new2[len(x_new2)-i-1], y_new2[len(x_new2)-i-1]))

		draw.polygon(poly, fill=(250, 0, 0), outline=(0, 250, 0), width=3)

		draw.line(points3, fill=(0, 0, 250), width=3)
		im.show()

w = Wykres()
#print(str(w))
w.timeout()

#def createZarysWykresu():
#	width = 1024
#	height = 300
#	im = Image.new("RGB", (width, height), color="black")
#	draw = ImageDraw.Draw(im)
#	for x in range(rowmajor):
#		for y in range(cols):
#			for z in range(rowminor):
#				posx = bsize * y + int(0.5* bsize)
#				posy = ( rowminor * x + z ) * bsize + int(0.5* bsize)
#				draw.point((posx,posy), fill="black")
#
#	for y in range(cols+1):
#		draw.line((y*bsize, 0, y*bsize, (rowmajor * rowminor + 1) * bsize), fill="black", width=1)
#
#	for x in range(rowmajor+1):
#		draw.line((0, x*rowminor*bsize, (cols + 1) * bsize, x*rowminor*bsize), fill="black", width=1)
#	im = im.resize((2* im.size[0], 2*im.size[1]), Image.ANTIALIAS)
#	im.show()
#createZarysPlytki()
"""

