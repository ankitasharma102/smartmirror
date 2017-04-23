import requests


class getweather:
	def __init__(self,city,api):
		self.city=city
		self.api=api

	def descntemp(self):
		r = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+self.city+"&appid="+self.api)
		weather=r.json()
		print("http://api.openweathermap.org/data/2.5/weather?q="+self.city+"&appid="+self.api)
		temperature=weather['main']['temp']-273.15
		desc=weather['weather'][0]['main']
		return desc, temperature



