from configparser import ConfigParser
from tkinter import *
import requests

app = Tk()
app.title('Weather App')
app.geometry('600x500')

def format_response(weather):
    try:
        name = weather['name']
        country = weather['sys']['country']
        description = weather['weather'][0]['description']
        temperature = weather['main']['temp']

        final_str = 'City: %s \nCountry: %s \nConditions: %s \nTemperature (°C): %s' % (name, country, description, temperature)
    except:
        final_str = 'Sorry! There was a problem \nretrieving the information'

    return final_str

def get_weather(city):
    config_file = 'config.ini'
    config = ConfigParser()
    config.read(config_file)
    weather_key = config['api_key']['key']
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)


background_image = PhotoImage(file='landscape.png')
background_label = Label(app, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = Frame(app, bg='aqua', bd=3)
frame.place(relx=0.5, rely=0.1, relheight=0.1, relwidth=0.75, anchor='n')

entry = Entry(frame, font=('courier', 14))
entry.place(relheight=1, relwidth=0.65)

button = Button(frame, text='Get Weather', font=('Times New Roman', 15), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = Frame(app, bg='aqua', bd=8)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = Label(lower_frame, font=('monospace', 15), anchor='nw', justify='left', bd=3)
label.place(relheight=1, relwidth=1)


app.mainloop()