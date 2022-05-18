# hi / hello / hey / hello there...
# play music / please play music / start song / start music
# tell me date / date / what's the date
# show time
# tell me news
# wether report

from datetime import datetime as dt
import os, random

greetIntent = ["hi", "hello", "hey", "hi there", "hello there", "hey there"]
dateIntent = ["date", "tell me date", "what's the date", "please tell me date"]
timeIntent = ["time", "tell me time", "what's the time", "please tell me time"]
musicIntent = ["play music", "please play music", "music", "start song", "song"]

chat = True
while chat:
    msg = input("Enter your message : ")

    if msg in greetIntent:
        print("Hello User...")
    elif msg in dateIntent:
        currentDate = dt.now().date()
        print("Date is",currentDate.strftime("%d %b, %Y, %a"))
    elif msg in timeIntent:
        currentTime = dt.now().time()
        print("Current Time is",currentTime.strftime("%I:%M:%S,%p"))
    elif msg in musicIntent:
        path = r"C:\Users\asus\Music\Songs"
        os.chdir(path)
        songs = os.listdir()
        song = random.choice(songs)
        os.startfile(song)
    elif msg == "bye":
        print("Bye User...")
        chat = False
        break
    else:
        print("I don't Understand...")