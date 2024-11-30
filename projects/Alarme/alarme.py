#Importing all the necessary libraries to form the alarm clock:
from tkinter import *
import datetime
import time
import winsound



def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("A data escolhida foi:",date)
        print(now)
        if now == set_alarm_timer:
            print("Tempo de acordar!"*5)
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

clock = Tk()
clock.title("Alarme - Tomás")
clock.geometry("400x200")
clock.configure(bg="#F7DC6F")
time_format=Label(clock, text= "Escreve no formato 24H!", fg="blue", font="Helevetica").place(x=60,y=120)
addTime = Label(clock,text = "Hora  Min   Seg",font=60).place(x = 110)
setYourAlarm = Label(clock,text = "Quando te acordo?",fg="blue",relief = "solid",font=("Helevetica",7,"bold")).place(x=0, y=29)

# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()

#Time required to set the alarm clock:
hourTime= Entry(clock,textvariable = hour,bg = "#C5CAE9",width = 15).place(x=110,y=30)
minTime= Entry(clock,textvariable = min,bg = "#C5CAE9",width = 15).place(x=150,y=30)
secTime = Entry(clock,textvariable = sec,bg = "#C5CAE9",width = 15).place(x=200,y=30)

#To take the time input by user:
submit = Button(clock,text = "Definir Alarme",fg="red",width = 10,command = actual_time).place(x =110,y=70)

clock.mainloop()