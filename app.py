import tkinter as tk
from tkinter import *
import datetime as dt
from PIL import ImageTk, Image
import requests


# Date Function
def get_date(city):
    pass


# create a window
window = tk.Tk()
window.title("Current Weather")
window.geometry('450x300')
window.iconbitmap('app_icon.ico')

# Date variables
date = dt.datetime.now()
format_date = f"{date:%a, %b %d %Y}" + " " + f"{date:%X}"

# frame for heading
header_frame = tk.Frame(window, bg='#4f524f')
header_frame.pack(fill=tk.BOTH)
# Label in main window
title = tk.Label(header_frame, text="Daily Forecast", fg="White", bg='#4f524f', font=('calibre', 18, 'bold'))
title.pack()

# declaring string variable
# for storing city value
city = tk.StringVar()

# Images for different weather conditions
# image size is 64px
sunny = ImageTk.PhotoImage(Image.open("D:\Python_Projects\weather_gui\sunny.png"))

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
button = tk.Button(search_frame, text='Enter', bg="#21cf2d", fg="white", relief=tk.RAISED, font=('calibre', 12, 'bold'))
button.grid(row=0, column=2)

# frame to display temperature and icon
data_frame = tk.Frame(frame)
data_frame.rowconfigure([0, 1, 2], minsize=100)
data_frame.columnconfigure([0, 1, 2, 3], minsize=200)
data_frame.pack(padx=1)
font_tuple = ("Comic Sans MS", 24, "bold")
date = tk.Label(data_frame, text=format_date, font=('Comic Sans MS', 10, 'bold'))
date.grid(row=0, column=0)
temp_label = tk.Label(data_frame, text="100 F", font=font_tuple)
temp_label.grid(row=1, column=0, sticky='nsew')
image_label = tk.Label(data_frame, image=sunny)
image_label.grid(row=1, column=1)
# Run the application
window.mainloop()
