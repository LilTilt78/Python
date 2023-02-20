import time
from datetime import datetime

from owm import OpenWeatherMap
from gw import GoogleWeather
from wu import WeatherUnderground

class Countdown:
    """Class Countdown funguje jako samostatný celek od mainu a obsahuje funkci countdown"""
    def countdown():
        """Funkce countdown odpočítává čas a na jeho konci se provede odebrání vzorků ze všech třech zdrojů
            a provede se zápis zjištěných dat do databáze.
            Funkce běží automaticky sama po celou dobu, co je program spuštěný a místo odebírání vzorku je nastaveno 
            defaultně na město Brno
        """
        while True:
            t = 600 # odpovídá 10 minutám
            while t:
                mins, secs = divmod(t, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)
                print(timer, end="\r")
                time.sleep(1)
                t -= 1
            
            OpenWeatherMap.getWeather("Brno")
            GoogleWeather.getGW("Brno")
            WeatherUnderground.getWU("Brno", "cz")
            sample_time = datetime.now()
            daytime = sample_time.strftime("%d/%m/%Y %H:%M:%S")
            print('The sample was taken and entered into the database! - ' + daytime)

    countdown()