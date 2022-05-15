import tkinter as tk
import datetime as dt
import requests
date = dt.datetime.now()
format_date = f"{date:%a, %b %d %Y}"

# create a window
window = tk.Tk()
window.title("Current Weather")
window.geometry('350x200')

# frame for heading
header_frame = tk.Frame(window, bg='#4f524f')
header_frame.pack(fill=tk.BOTH)
# Label in main window
title = tk.Label(header_frame, text="Daily Forecast", fg="White", bg='#4f524f', font=('calibre', 18, 'bold'))
title.pack()

# declaring string variable
# for storing city value
city = tk.StringVar()

# frame for the entry and json response
frame = tk.Frame(window)
frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

search_frame = tk.Frame(frame)
search_frame.pack(pady=3)

# label for entry field
entry_label = tk.Label(search_frame, text="Search", font=('calibre', 10, 'bold'), fg='#1bd90d')
entry_label.grid(row=0, column=0)

# entry for the city search
entry = tk.Entry(search_frame, relief=tk.GROOVE, bd=5)
entry.grid(row=0, column=1)

# frame to display temperature and icon
data_frame = tk.Frame(frame)
data_frame.rowconfigure([0, 1], minsize=50)
data_frame.columnconfigure([0, 1, 2, 3], minsize=50)
data_frame.pack()
font_tuple = ("Comic Sans MS", 20, "bold")
date = tk.Label(data_frame, text=format_date, font=('Comic Sans MS', 10, 'bold'))
date.grid(row=0, column=0)
temp_label = tk.Label(data_frame, text="100 F", font=font_tuple)
temp_label.grid(row=1, column=0)
bar = tk.Label(data_frame, text="|", font=font_tuple)
bar.grid(row=1,column=1)
# Run the application
window.mainloop()
