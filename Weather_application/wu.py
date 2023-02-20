from requests_html import HTMLSession
from datetime import datetime

from add_to_database import Database

class WeatherUnderground:
    """Obsahuje funkci getWU"""
    def getWU(city, state):
        """Funkce pro extrakci dat z portálu Weather Underground, jejich uspořádání a příprava k zobrazení"""
        sample_time = datetime.now()
        daytime = sample_time.strftime("%d/%m/%Y %H:%M:%S")
        session = HTMLSession()
        url3 = f'https://www.wunderground.com/weather/{state}/{city}'
        request = session.get(url3, headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'})

        tempf_wun = request.html.find("div.current-temp", first = True).find("span.wu-value.wu-value-to", first = True).text

        tempc_wun = (float(tempf_wun) - 32) / 1.8
        tempc_wun = '{:.2f}'.format(tempc_wun)
        tempc_wun = str(tempc_wun)

        desc_wun = request.html.find("div.data-module.additional-conditions", first = True).find("span.wx-value", first = True).text

        feelslike_wun = request.html.find("div.region-content-main", first = True).find("span.temp", first = True).text

        humidity_wun = request.html.find("span.test-false.wu-unit.wu-unit-humidity.ng-star-inserted", first = True).find("span.wu-value.wu-value-to", first = True).text

        visibilitym_wun = request.html.find("span.test-false.wu-unit.wu-unit-distance.ng-star-inserted", first = True).find("span.wu-value.wu-value-to", first = True).text
        visibilitykm_wun = float(visibilitym_wun) * 1.609
        visibilitykm_wun = '{:.2f}'.format(visibilitykm_wun)
        visibilitykm_wun = str(visibilitykm_wun)

        weather_underground_data = {'tempc_wun':tempc_wun, 'tempf_wun':tempf_wun, 'desc_wun':desc_wun, 'feelslike_wun':feelslike_wun, 'humidity_wun':humidity_wun, 'visibilitykm_wun':visibilitykm_wun}
        Database.addToDB(Database.id, "WeatherUndeground", daytime, city, tempc_wun, tempf_wun, desc_wun, feelslike_wun, "", humidity_wun, visibilitykm_wun)
        Database.id += 1
        return weather_underground_data