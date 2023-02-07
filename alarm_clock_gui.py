from tkinter import *  
import datetime as dt  
import time  
import winsound as ws


def alarm(setAlarmTimer):  
    while True:  
        time.sleep(1)  
        actualTime = dt.datetime.now()
        currentTime = actualTime.strftime("%I : %M : %S")  
        currentDate = actualTime.strftime("%d / %m / %Y")  
        the_message = "Current Time: " + str(currentTime)  
        print(the_message)
        if currentTime == setAlarmTimer:  
            wakeUp = Label(  
                        alarmWin,  
                        text = "Wake Up Prathmesh !!!",  
                        fg = "white",  
                        bg = "#36486B",  
                        font = ("Arial", 15)  
                        ).place(x = 140, y = 120)
            ws.PlaySound("Alarm10.wav", ws.SND_ASYNC)
            print("Wake Up Prathmesh !!!")
            break  

def getAlarmTime():  
    alarmSetTime = f"{hour.get()} : {minute.get()} : {second.get()}"  
    print(alarmSetTime.isalnum())
    print(alarmSetTime)
    print(hour.get())
    type(hour.get())
    alarm(alarmSetTime)  

alarmWin = Tk()  
alarmWin.title("The Alarm Clock")  
alarmWin.geometry("475x260")
alarmWin.config(bg = "dark grey")  

timeFormat = Label(  
    alarmWin,  
    text = "Set time in 12-hour format !!!",  
    fg = "white",  
    bg = "#36486B",  
    font = ("Arial", 15)  
    ).place(x = 100, y = 160)  
   
add_time = Label(  
    alarmWin,  
    text = "Hour         Minute         Second",  
    font = 60,  
    fg = "black",
    bg="dark grey" 
    ).place(x = 240, y = 10)  
  
setAlarm = Label(  
    alarmWin,  
    text = "Set Time for Alarm: ",  
    fg = "black",  
    bg = "#034F84",  
    relief = "solid",  
    font = ("Helevetica", 13, "bold")  
    ).place(x = 20, y = 50)  
   
hour = StringVar()  
minute = StringVar()  
second = StringVar()  
   
hourTime = Entry(  
    alarmWin,  
    textvariable = hour,  
    bg = "#FEFBD8",  
    width = 6,  
    font = (20)  
    ).place(x = 220, y = 53)


minuteTime = Entry(  
    alarmWin,  
    textvariable = minute,  
    bg = "#FEFBD8",  
    width = 6,  
    font = (20)  
    ).place(x = 297, y = 53)

secondTime = Entry(  
    alarmWin,  
    textvariable = second,  
    bg = "#FEFBD8",  
    width = 6,  
    font = (20)  
    ).place(x = 390, y = 53)  


submit = Button(  
    alarmWin,  
    text = "Set The Alarm",  
    fg = "Black",  
    bg = "#82B74B",  
    width = 15,  
    command = getAlarmTime,  
    font = (20)  
    ).place(x = 160, y = 100)  

myName = Label(  
    alarmWin,  
    text = "Developer: Prathmesh Mohan Chaudhari",  
    fg = "white",  
    bg = "#36486B",  
    font = ("Arial", 10)  
    ).place(x = 110, y = 200)

alarmWin.mainloop() 