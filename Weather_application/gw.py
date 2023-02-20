from requests_html import HTMLSession
from datetime import datetime

from add_to_database import Database

class GoogleWeather:
    """Obsahuje funkci getGW"""
    def getGW(city):
        """Funkce pro extrakci dat z portálu Google Weather, jejich uspořádání a příprava k zobrazení"""
        sample_time = datetime.now()
        daytime = sample_time.strftime("%d/%m/%Y %H:%M:%S")
        session = HTMLSession()
        url2 = f'https://www.google.com/search?q=weather+{city}'
        request = session.get(url2, headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'})
        
        tempc_goo = request.html.find("span#wob_tm", first = True).text
        tempc_goo = float(tempc_goo)
        tempc_goo = str(tempc_goo)
        
        tempf_goo = (float(tempc_goo) * 1.8) + 32
        tempf_goo = '{:.2f}'.format(tempf_goo)
        tempf_goo = str(tempf_goo)

        desc_goo = request.html.find("div.VQF4g", first = True).find("span#wob_dc", first = True).text
        
        wind_goo = request.html.find("div.wtsRwe", first = True).find("span#wob_ws", first = True).text

        humidity_goo = request.html.find("div.wtsRwe", first = True).find("span#wob_hm", first = True).text

        google_weather_data = {'tempc_goo':tempc_goo, 'tempf_goo':tempf_goo, 'desc_goo':desc_goo, 'wind_goo':wind_goo, 'humidity_goo':humidity_goo}
        Database.addToDB(Database.id, "GoogleWeather", daytime, city, tempc_goo, tempf_goo, desc_goo, "", wind_goo, humidity_goo, "")
        Database.id += 1
        return google_weather_data
