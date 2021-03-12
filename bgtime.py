#!/usr/bin/env python

# Imports
from datetime import datetime
from pyowm.owm import OWM
import os

# Times of day
morning = False
afternoon = False
evening = False
night = False


def main():
	current_weather = getWeather()
	current_time = int(getTime())
	current_pic = setWallpaper(current_time, current_weather)

	setBG(current_pic)


def getWeather():
	"""
	Gets current weather from OWN data, i.e "Clouds"
	"""
	owm = OWM("2e17a4229ccfbd3e5a13a8c5b26954bb")
	mgr = owm.weather_manager()
	observation = mgr.weather_at_place('Bergen,NO')
	weather = observation.weather
	return weather.status


def getTime():
	"""
	Gets current hour from system time
	"""
	return datetime.now().hour



def setWallpaper(time, weather):
	"""
	Chooses image to use based on weather/time data
	"""
	pic = ""

	if weather == "Rain" or weather == "Snow":
		if time >= 6 and time < 12:
			pic = "rain-morning.jpeg"
		elif time >= 12 and time < 18:
			pic = "rain-afternoon.jpg"
		elif time >= 18 and time < 22:
			pic = "rain-evening.jpg"
		else:
			pic = "rain-night.jpg"

	if weather == "Clear":
		if time >= 6 and time < 12:
			pic = "clear-morning.jpg"
		elif time >= 12 and time < 18:
			pic = "clear-afternoon.jpg"
		elif time >= 18 and time < 22:
			pic = "clear-evening.jpg"
		else:
			pic = "clear-night.jpg"

	if weather == "Clouds":
		if time >= 6 and time < 12:
			pic = "cloud-morning.jpg"
		elif time >= 12 and time < 18:
			pic = "cloud-afternoon.jpg"
		elif time >= 18 and time < 22:
			pic = "cloud-evening.jpg"
		else:
			pic = "cloud-night.jpg"

	return pic


def setBG(pic):
	os.system("gsettings set org.gnome.desktop.background picture-uri file:///home/danj/Documents/bgpy/wallpapers/" + pic)


if __name__ == "__main__":
    main()
