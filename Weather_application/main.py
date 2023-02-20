import tkinter as tk
from tkinter import messagebox
from turtle import width

from owm import OpenWeatherMap
from gw import GoogleWeather
from wu import WeatherUnderground

def search():
    """Funkce pro vyhledání a vypsání údajů do okna aplikace,
        nelze oddělit od zbytku mimo funkci do samostatného souboru, protože poté vzniká Error Circular Import
    """
    canvas.delete("all")
    canvas.create_image(0, 0, image = bg_image, anchor = "nw")
    canvas.create_text(265, 18, text = zadej_lbl['text'], font = ('Verdana', 12), fill = 'white')
    canvas.create_text(810, 18, text = example_lbl['text'], font = ('Verdana', 10, 'italic'), fill = 'white')
    canvas.create_text(160, 210, text = "Data from OpenWeatherMap:", font = ('Verdana', 15), fill = 'white')
    canvas.create_text(470, 210, text = "Data from Google Weather:", font = ('Verdana', 15), fill = 'white')
    canvas.create_text(800, 210, text = "Data from Weather Underground:", font = ('Verdana', 15), fill = 'white')
    city = city_text.get()
    state = state_text.get()
    result = OpenWeatherMap.getWeather(city)
    if result:
        #OpenWeatherMap údaje
        location_lbl['text'] = '{},{}'.format(result[0], result[1])
        canvas.create_text(470, 100, text = location_lbl['text'], font = ('Verdana', 25, 'bold'), fill = 'white')
        img['file'] = 'icons/{}.png'.format(result[4])
        canvas.create_image(420, 100, image = img, anchor = "nw")
        temperaturec_lbl['text'] = '{:.2f} °C'.format(result[2])
        canvas.create_text(150, 250, text = temperaturec_lbl['text'], font = ('Verdana', 15, 'bold'), fill = 'white')
        temperaturef_lbl['text'] = '{:.2f} °F'.format(result[3])
        canvas.create_text(150, 270, text = temperaturef_lbl['text'], font = ('Verdana', 15, 'bold'), fill = 'white')
        weather_lbl['text'] = result[5]
        canvas.create_text(150, 290, text = weather_lbl['text'], font = ('Verdana', 15, 'bold'), fill = 'white')
        feelslike_lbl['text'] = 'Feels like: {:.2f} °C'.format(result[6])
        canvas.create_text(150, 330, text = feelslike_lbl['text'], font = ('Verdana', 15, 'bold'), fill = 'white')
        windspeed_lbl['text'] = 'Wind speed: {:.2f} km/h'.format(result[7])
        canvas.create_text(150, 350, text = windspeed_lbl['text'], font = ('Verdana', 15, 'bold'), fill = 'white')
        humidity_lbl['text'] = 'Humidity: {:.2f} %'.format(result[8])
        canvas.create_text(150, 370, text = humidity_lbl['text'], font = ('Verdana', 15, 'bold'), fill = 'white')
        visibility_lbl['text'] = 'Visibility: {:.2f} km'.format(result[9])
        canvas.create_text(150, 390, text = visibility_lbl['text'], font = ('Verdana', 15, 'bold'), fill = 'white')
            
        #Google weather údaje
        google_wether_data = GoogleWeather.getGW(city)
        tempc_goo_lbl['text'] = google_wether_data['tempc_goo'] + " °C"
        canvas.create_text(470, 250, text = tempc_goo_lbl['text'], font = ('Verdana', 15, 'bold'), fill = 'white')
        tempf_goo_lbl['text'] = google_wether_data['tempf_goo'] + " °F"
        canvas.create_text(470, 270, text = tempf_goo_lbl['text'], font = ('Verdana', 15, 'bold'), fill = 'white')
        desc_goo_lbl['text'] = google_wether_data['desc_goo']
        canvas.create_text(470, 290, text = desc_goo_lbl['text'], font = ('Verdana', 15, 'bold'), fill = 'white')
        wind_goo_lbl['text'] = "Wind speed: " + google_wether_data['wind_goo']
        canvas.create_text(470, 350, text = wind_goo_lbl['text'], font = ('Verdana', 15, 'bold'), fill = 'white')
        humi_goo_lbl['text'] = "Humidity: " + google_wether_data['humidity_goo']
        canvas.create_text(470, 370, text = humi_goo_lbl['text'], font = ('Verdana', 15, 'bold'), fill = 'white')

        #Weather Underground údaje
        weather_underground_data = WeatherUnderground.getWU(city, state)
        tempf_wun_lbl['text'] = weather_underground_data['tempf_wun'] + " °F"
        canvas.create_text(800, 270, text = tempf_wun_lbl['text'], font = ('Verdana', 15, 'bold'), fill = 'white')
        tempc_wun_lbl['text'] = weather_underground_data['tempc_wun'] + " °C"
        canvas.create_text(800, 250, text = tempc_wun_lbl['text'], font = ('Verdana', 15, 'bold'), fill = 'white')
        desc_wun_lbl['text'] = weather_underground_data['desc_wun']
        canvas.create_text(800, 290, text = desc_wun_lbl['text'], font = ('Verdana', 15, 'bold'), fill = 'white')
        feelslike_wun_lbl['text'] = "Feels like: " + weather_underground_data['feelslike_wun'] + "F"
        canvas.create_text(800, 330, text = feelslike_wun_lbl['text'], font = ('Verdana', 15, 'bold'), fill = 'white')
        humi_wun_lbl['text'] = "Humidity: " + weather_underground_data['humidity_wun'] + "%"
        canvas.create_text(800, 370, text = humi_wun_lbl['text'], font = ('Verdana', 15, 'bold'), fill = 'white')
        visibility_wun_lbl['text'] = "Visibility: " + weather_underground_data['visibilitykm_wun'] + " km"
        canvas.create_text(800, 390, text = visibility_wun_lbl['text'], font = ('Verdana', 15, 'bold'), fill = 'white')

    else:
        messagebox.showerror('Error', "City {} was not founded".format(city))

# Vytvoření nového okna aplikace
app = tk.Tk()
app.title("Weather App")
app.geometry('1000x500')
app.configure(bg = 'white')

bg_image = tk.PhotoImage(file = 'bg_image.png')

# Vytvoření Canvas
canvas = tk.Canvas(app, width = 1000, height = 500)
canvas.pack(fill = "both", expand = True)

# Nastavení obrázku do Canvasu
canvas.create_image(0, 0, image = bg_image, anchor = "nw")

zadej_lbl = tk.Label(app, text = "Please enter name of the city:                            and state: ", font = ('Verdana', 12))
canvas.create_text(265, 18, text = zadej_lbl['text'], font = ('Verdana', 12), fill = 'white')

example_lbl = tk.Label(app, text = "(e.g.: cz, de, us/fl, us/ny, at, sk, etc.)", font = ('Verdana', 10))
canvas.create_text(810, 18, text = example_lbl['text'], font = ('Verdana', 10, 'italic'), fill = 'white')

city_text = tk.StringVar()
city_entry = tk.Entry(app, textvariable=city_text)
city_entry.place(x = 270, y = 6, height = 25, width = 150)

state_text = tk.StringVar()
state_entry = tk.Entry(app, textvariable=state_text)
state_entry.place(x = 520, y = 6, height = 25, width = 150)

search_btn = tk.Button(app, text = "Search weather", font = ('Verdana', 12) ,width = 15, command = search)
search_btn.place(x = 395, y = 35, height = 30, width = 150)
search_btn.configure(bg = '#f722f2', fg = 'black')

img = tk.PhotoImage(file = '')
image = tk.Label(app, image = img)
canvas.create_image(200, 120, image = img, anchor = "nw")

location_lbl = tk.Label(app, text = "", font = ('Verdana', 25))

### OpenWeatherMap ###
canvas.create_text(160, 210, text = "Data from OpenWeatherMap:", font = ('Verdana', 15), fill = 'white')
temperaturec_lbl = tk.Label(app, text = "temp C opm", font = ('Verdana', 12))
temperaturef_lbl = tk.Label(app, text = "temp F opm", font = ('Verdana', 12))
weather_lbl = tk.Label(app, text = "description opm", font = ('Verdana',12))
feelslike_lbl = tk.Label(app, text = "feels like opm", font = ('Verdana', 12))
windspeed_lbl = tk.Label(app, text = "wind  opm", font = ('Verdana', 12))
humidity_lbl = tk.Label(app, text = "humidity opm", font = ('Verdana', 12))
visibility_lbl = tk.Label(app, text = "visibility opm", font = ('Verdana', 12))

### Google Weather ###
canvas.create_text(470, 210, text = "Data from Google Weather:", font = ('Verdana', 15), fill = 'white')
tempc_goo_lbl = tk.Label(app, text = "temp C google", font = ('Verdana', 12))
tempf_goo_lbl = tk.Label(app, text = "temp F google", font = ('Verdana', 12))
desc_goo_lbl = tk.Label(app, text = "description google", font = ('Verdana', 12))
wind_goo_lbl = tk.Label(app, text = "wind google", font = ('Verdana', 12))
humi_goo_lbl = tk.Label(app, text = "humidity google", font = ('Verdana', 12))

### Weather Underground ###
canvas.create_text(800, 210, text = "Data from Weather Underground:", font = ('Verdana', 15), fill = 'white')
tempc_wun_lbl = tk.Label(app, text = "temp C under", font = ('Verdana', 12))
tempf_wun_lbl = tk.Label(app, text = "temp F under", font = ('Verdana', 12))
desc_wun_lbl = tk.Label(app, text = "description under", font = ('Verdana', 12))
feelslike_wun_lbl = tk.Label(app, text = "feels like under", font = ('Verdana', 12))
humi_wun_lbl = tk.Label(app, text = "humidity under", font = ('Verdana', 12))
visibility_wun_lbl = tk.Label(app, text = "visibility under", font = ('Verdana', 12))

app.mainloop()