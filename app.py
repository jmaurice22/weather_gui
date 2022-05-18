import tkinter as tk
from tkinter import *
import datetime as dt
from PIL import ImageTk, Image
import geocoder
import requests
import re

# Method to request server for weather data
def get_weather():
    city = entry.get()
    degree_sign = u"\N{DEGREE SIGN}"
    # API KEY
    api_key = 'f0d6ab958d9c3097d6dcbaf7427c4ec4'
    # BASE URL
    base_url = 'https://api.openweathermap.org/data/2.5/weather?'
    # FULL URL
    full_url = base_url + 'q=' + city + '&' + 'units=imperial' + '&appid=' + api_key
    # REQUEST TO SERVER
    response = requests.get(full_url)
    # check for successful response code (200)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temp = main['temp']
        temp = int(temp)
        weather = data['weather']
        description = weather[0]['description']
        temp_label = tk.Label(data_frame, text=f"{temp}{degree_sign}F", font=font_tuple, bg='#a8d5e5')
        temp_label.grid(row=2, column=0, sticky='nsew')
        city_label = tk.Label(data_frame, text=city.upper(), font=('calibre', 10, 'bold'), bg='#a8d5e5')
        city_label.grid(row=1, column=1)
        description_label = tk.Label(data_frame, text=description, font=('calibre', 10, 'bold'), bg='#a8d5e5')
        description_label.grid(row=2, column=2)
        entry.delete(0, END)
        show_image(description)
    else:
        # ERROR HANDLING
        temp_label = tk.Label(data_frame, text="Not Found", font=font_tuple, bg='#a8d5e5')
        temp_label.grid(row=2, column=0, sticky='nsew')
        city_label = tk.Label(data_frame, text="", font=('calibre', 10, 'bold'), bg='#a8d5e5')
        city_label.grid(row=1, column=1)
        entry.delete(0, END)

# Method to display corresponding images
def show_image(description):
    if description == "clear sky":
        image_label = tk.Label(data_frame, image=sunny, bg='#a8d5e5')
        image_label.grid(row=2, column=1)
    elif description == "broken clouds" or description == "few clouds" or description == "scattered clouds" \
            or description == "broken clouds":
        image_label = tk.Label(data_frame, image=broken_clouds, bg='#a8d5e5')
        image_label.grid(row=2, column=1)
    elif description == "snow":
        image_label = tk.Label(data_frame, image=snow, bg='#a8d5e5')
        image_label.grid(row=2, column=1)
    elif description == "rain" or description == "shower rain":
        image_label = tk.Label(data_frame, image=rain, bg='#a8d5e5')
        image_label.grid(row=2, column=1)

# Method to get Geolocation lat & long coordinates
def geolocation():
    degree_sign = u"\N{DEGREE SIGN}"
    g = geocoder.ip('me')
    latitude = g.lat
    longitude = g.lng
    try:
        # API KEY
        api_key = 'f0d6ab958d9c3097d6dcbaf7427c4ec4'
        res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&units=imperial&appid={api_key}").json()
        main = res['main']
        temp = main['temp']
        temp = int(temp)
        weather = res['weather']
        description = weather[0]['description']
        temp_label = tk.Label(data_frame, text=f"{temp}{degree_sign}F", font=font_tuple, bg='#a8d5e5')
        temp_label.grid(row=2, column=0, sticky='nsew')
        description_label = tk.Label(data_frame, text=description, font=('calibre', 10, 'bold'), bg='#a8d5e5')
        description_label.grid(row=2, column=2)
        show_image(description)
    except:
        pass

# create a window
window = tk.Tk()
window.title("Weather")
window.geometry('450x300')
window.iconbitmap('app_icon.ico')


# Date variables
date = dt.datetime.now()
format_date = f"{date:%a, %b %d %Y}"

# frame for heading
header_frame = tk.Frame(window, bg='#4f524f')
header_frame.pack(fill=tk.BOTH)
# Label in main window
title = tk.Label(header_frame, text="Forecast", fg="White", bg='#4f524f', font=('calibre', 18, 'bold'))
title.pack()



# Images for different weather conditions
# image size is 64px
sunny = ImageTk.PhotoImage(Image.open("D:\Python_Projects\weather_gui\images\sunny.png"))
broken_clouds = ImageTk.PhotoImage(Image.open("D:\Python_Projects\weather_gui\images\\broken_clouds.png"))
snow = ImageTk.PhotoImage(Image.open("D:\Python_Projects\weather_gui\images\snow.png"))
rain = ImageTk.PhotoImage(Image.open("D:\Python_Projects\weather_gui\images\\rain.png"))

# frame for the entry and json response
frame = tk.Frame(window, bg='#a8d5e5')
frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

search_frame = tk.Frame(frame, bg='#a8d5e5')
search_frame.pack(pady=3)
search_frame.rowconfigure(0)
search_frame.columnconfigure([0, 1, 2], minsize=50)


# label for entry field
entry_label = tk.Label(search_frame, text="Search", font=('calibre', 10, 'bold'), bg='#a8d5e5')
entry_label.grid(row=0, column=0)

# entry for the city search
entry = tk.Entry(search_frame, relief=tk.GROOVE, bd=5)
entry.grid(row=0, column=1)

# search button
button = tk.Button(search_frame, text='Enter', bg="#21cf2d", fg="white", relief=tk.RAISED, font=('calibre', 9, 'bold'),
                   command=get_weather)
button.grid(row=0, column=2)

# frame to display temperature and icon
data_frame = tk.Frame(frame,  bg='#a8d5e5')
data_frame.rowconfigure([0, 1, 2], minsize=50)
data_frame.columnconfigure([0, 1, 2, 3], minsize=100)
data_frame.pack(padx=1, fill=tk.BOTH, expand=True)
font_tuple = ("Comic Sans MS", 24, "bold")
date = tk.Label(data_frame, text=format_date, font=('Comic Sans MS', 10, 'bold'), bg='#a8d5e5')
date.grid(row=0, column=0)

# Run the application
if __name__ == '__main__':
    geolocation()
    window.mainloop()
