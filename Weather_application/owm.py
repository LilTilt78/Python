from configparser import ConfigParser
from pip._vendor import requests
from datetime import datetime

from add_to_database import Database

# Konfigurace API klíče
config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']

class OpenWeatherMap:
    """Obsahuje funkci getWeather"""
    url1 = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

    def getWeather(city):
        """Funkce pro extrakci dat z portálu OpenWeatherMap, jejich uspořádání a příprava k zobrazení"""
        sample_time = datetime.now()
        daytime = sample_time.strftime("%d/%m/%Y %H:%M:%S")
        demand = requests.get(OpenWeatherMap.url1.format(city, api_key))
        if demand:
            json = demand.json()
            # City, Country, temp_celsius, temp_fahrenheit, icon, weather, feels_like ,wind_speed, humidity, visibility
            city = json['name']
            country = json['sys']['country']
            temp_kelvin = json['main']['temp']
            temp_celsius = temp_kelvin - 273.15
            temp_fahrenheit = (temp_celsius * 1.8) + 32
            icon = json['weather'][0]['icon']
            weather = json['weather'][0]['main']
            feels_like_k = json['main']['feels_like']
            feels_like = feels_like_k - 273.15
            wind_speedm = json['wind']['speed']
            wind_speedkm = wind_speedm * 3.6
            humidity = json['main']['humidity']
            visibility_m = json['visibility']
            visibility_km = visibility_m / 1000
            result = (city, country, temp_celsius, temp_fahrenheit, icon, weather, feels_like, wind_speedkm, humidity, visibility_km)
            Database.addToDB(Database.id, "OpenWeatherMap", daytime, city, temp_celsius, temp_fahrenheit, weather, feels_like, wind_speedkm, humidity, visibility_km)
            Database.id += 1
            return result
        else:
            return None
                
    
        