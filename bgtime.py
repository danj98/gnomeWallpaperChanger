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
	owm = OWM("TOKEN HERE")
	mgr = owm.weather_manager()
	observation = mgr.weather_at_place("LOCATION")
	weather = observation.weather
	return weather.status


def getTime():
	"""
	Gets current hour from system time
	"""
	return datetime.now().hour

# Add you own images as filepath:
rain_morning = "folder/example.jpg"
rain_afternoon = ""
rain_evening = ""
rain_night = ""

clear_morning = ""
clear_afternoon = ""
clear_evening = ""
clear_night = ""

clouds_morning = ""
clouds_afternoon = ""
clouds_evening = ""
clouds_night = ""

def setWallpaper(time, weather):
	"""
	Chooses image to use based on weather/time data
	"""
	pic = ""

	if weather == "Rain" or weather == "Snow":
		if time >= 6 and time < 12:
			pic = rain_morning
		elif time >= 12 and time < 18:
			pic = rain_afternoon
		elif time >= 18 and time < 22:
			pic = rain_evening
		else:
			pic = rain_night

	if weather == "Clear":
		if time >= 6 and time < 12:
			pic = clear_morning
		elif time >= 12 and time < 18:
			pic = clear_afternoon
		elif time >= 18 and time < 22:
			pic = clear_evening
		else:
			pic = clear_night

	if weather == "Clouds":
		if time >= 6 and time < 12:
			pic = cloud_morning
		elif time >= 12 and time < 18:
			pic = cloud_afternoon
		elif time >= 18 and time < 22:
			pic = cloud_evening
		else:
			pic = cloud_night

	return pic


def setBG(pic):
	os.system("gsettings set org.gnome.desktop.background picture-uri file:///home/danj/Documents/bgpy/wallpapers/" + pic)


if __name__ == "__main__":
    main()
