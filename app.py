import tkinter as tk
from tkinter import *
import datetime as dt

import snow as snow
from PIL import ImageTk, Image
import requests


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
        temp_label = tk.Label(data_frame, text=f"{temp}{degree_sign}F", font=font_tuple)
        temp_label.grid(row=2, column=0, sticky='nsew')
        city_label = tk.Label(data_frame, text=city.upper(), font=('calibre', 10, 'bold'))
        city_label.grid(row=1, column=1)
        description_label = tk.Label(data_frame, text=description, font=('calibre', 10, 'bold'))
        description_label.grid(row=2, column=2)
        entry.delete(0, END)
        show_image(description)
    else:
        # ERROR HANDLING
        temp_label = tk.Label(data_frame, text="Not Found", font=font_tuple)
        temp_label.grid(row=2, column=0, sticky='nsew')
        city_label = tk.Label(data_frame, text="", font=('calibre', 10, 'bold'))
        city_label.grid(row=1, column=1)
        entry.delete(0, END)


def show_image(description):
    if description == "clear sky":
        image_label = tk.Label(data_frame, image=sunny)
        image_label.grid(row=2, column=1)
    elif description == "broken clouds":
        image_label = tk.Label(data_frame, image=broken_clouds)
        image_label.grid(row=2, column=1)
    elif description == "snow":
        image_label = tk.Label(data_frame, image=snow)
        image_label.grid(row=2, column=1)
    elif description == "rain":
        image_label = tk.Label(data_frame, image=rain)
        image_label.grid(row=2, column=1)


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

# declaring string variable
# for storing city value
# city = tk.StringVar()

# Images for different weather conditions
# image size is 64px
sunny = ImageTk.PhotoImage(Image.open("D:\Python_Projects\weather_gui\images\sunny.png"))
broken_clouds = ImageTk.PhotoImage(Image.open("D:\Python_Projects\weather_gui\images\\broken_clouds.png"))
snow = ImageTk.PhotoImage(Image.open("D:\Python_Projects\weather_gui\images\snow.png"))
rain = ImageTk.PhotoImage(Image.open("D:\Python_Projects\weather_gui\images\\rain.png"))

# frame for the entry and json response
frame = tk.Frame(window)
frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

search_frame = tk.Frame(frame)
search_frame.pack(pady=3)
search_frame.rowconfigure(0)
search_frame.columnconfigure([0, 1, 2], minsize=50)

# label for entry field
entry_label = tk.Label(search_frame, text="Search", font=('calibre', 10, 'bold'), fg='#1bd90d')
entry_label.grid(row=0, column=0)

# entry for the city search
entry = tk.Entry(search_frame, relief=tk.GROOVE, bd=5)
entry.grid(row=0, column=1)

# search button
button = tk.Button(search_frame, text='Enter', bg="#21cf2d", fg="white", relief=tk.RAISED, font=('calibre', 9, 'bold'),
                   command=get_weather)
button.grid(row=0, column=2)

# frame to display temperature and icon
data_frame = tk.Frame(frame)
data_frame.rowconfigure([0, 1, 2], minsize=50)
data_frame.columnconfigure([0, 1, 2, 3], minsize=100)
data_frame.pack(padx=1)
font_tuple = ("Comic Sans MS", 24, "bold")
date = tk.Label(data_frame, text=format_date, font=('Comic Sans MS', 10, 'bold'))
date.grid(row=0, column=0)

# Run the application
window.mainloop()
