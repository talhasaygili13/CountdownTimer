import datetime
import tkinter as tk
from win11toast import toast
def get_user_input():
    year = int(entry_year.get())
    month = int(entry_month.get())
    day = int(entry_day.get())
    hour = int(entry_hour.get())
    minute = int(entry_minute.get())

    target_datetime = datetime.datetime(year, month, day, hour, minute)
    start_countdown(target_datetime)

def start_countdown(target_datetime):
    time = target_datetime - datetime.datetime.now()
    days = time.days
    hours, rem = divmod(time.seconds, 3600)
    minutes, seconds = divmod(rem, 60)

    text = fillzero(str(hours)) + ":" + fillzero(str(minutes)) + ":" + fillzero(str(seconds))
    label.config(text=text)

    if int(seconds) < 1:
        toast('Alarm', 'Time is up!')
    else:
        label.after(1000, start_countdown, target_datetime)

def fillzero(s):
    return s.zfill(2)



root = tk.Tk()
root.title("Countdown Timer")

frame = tk.Frame(root)
frame.pack()

label = tk.Label(frame, font=('Helvetica', 24))
label.pack()

entry_year = tk.Entry(frame, width=6, font=('Helvetica', 18))
entry_year.insert(0, str(datetime.datetime.now().year))
entry_year.pack(side=tk.LEFT)

entry_month = tk.Entry(frame, width=4, font=('Helvetica', 18))
entry_month.insert(0, "01")
entry_month.pack(side=tk.LEFT)

entry_day = tk.Entry(frame, width=4, font=('Helvetica', 18))
entry_day.insert(0, "01")
entry_day.pack(side=tk.LEFT)

entry_hour = tk.Entry(frame, width=4, font=('Helvetica', 18))
entry_hour.insert(0, "00")
entry_hour.pack(side=tk.LEFT)

entry_minute = tk.Entry(frame, width=4, font=('Helvetica', 18))
entry_minute.insert(0, "00")
entry_minute.pack(side=tk.LEFT)

start_button = tk.Button(root, text="Start Countdown", command=get_user_input)
start_button.pack()

root.mainloop()
