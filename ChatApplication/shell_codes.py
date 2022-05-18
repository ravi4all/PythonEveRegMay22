Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
names = ["Mac", "Sam", "Tom", "John"]
"Tom" in names
True
"Peter" in names
False
import datetime
print(datetime.datetime.now())
2022-05-18 21:28:50.180180
print(datetime.datetime.now().date())
2022-05-18
print(datetime.datetime.now().time())
21:29:07.522678
from datetime import datetime as dt
print(dt.now().date())
2022-05-18
date = dt.now().date()
time = dt.now().time()
date.strftime("%d/%m/%y")
'18/05/22'
date.strftime("%d,%m,%y")
'18,05,22'
date.strftime("%d %b,%y")
'18 May,22'
date.strftime("%d %b %Y")
'18 May 2022'
date.strftime("%d %b %Y, %p")
'18 May 2022, AM'
date.strftime("%d %b %Y, %a")
'18 May 2022, Wed'
date.strftime("%d %b %Y, %A")
'18 May 2022, Wednesday'
time.strftime("%H:%M:%S")
'21:35:13'
time.strftime("%H:%M:%S,%p")
'21:35:13,PM'
time.strftime("%I:%M:%S,%p")
'09:35:13,PM'
time.strftime("%I:%M:%S,%p")
'09:35:13,PM'
time = dt.now().time()
time.strftime("%I:%M:%S,%p")
'09:38:41,PM'
import os
os.startfile('C:\Users\asus\Music\Songs\FadedCopy.mp3')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
path = "C:\new\songs\tollywood\new_songs"
print(path)
C:
ew\songs	ollywood
ew_songs
path = "C:\\new\\songs\\tollywood\\new_songs"
print(path)
C:\new\songs\tollywood\new_songs
path = "C:/new/songs/tollywood/new_songs"
print(path)
C:/new/songs/tollywood/new_songs
path = r"C:\new\songs\tollywood\new_songs"
print(path)
C:\new\songs\tollywood\new_songs
path
'C:\\new\\songs\\tollywood\\new_songs'
#r - raw string
os.startfile(r'C:\Users\asus\Music\Songs\FadedCopy.mp3')
path = 'C:\Users\asus\Music\Songs'
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
path = r'C:\Users\asus\Music\Songs'
os.getcwd()
'C:\\Python310'
os.chdir(path)
os.getcwd()
'C:\\Users\\asus\\Music\\Songs'
os.listdir()
['bang-bang.mp3', 'Faded.mp3', 'FadedCopy.mp3', 'fifa world cup.mp3', 'song.mp3', 'songCopy.mp3']
songs = os.listdir()
songs
['bang-bang.mp3', 'Faded.mp3', 'FadedCopy.mp3', 'fifa world cup.mp3', 'song.mp3', 'songCopy.mp3']
import random
song = random.choice(songs)
os.startfile(song)
song = random.choice(songs)
os.startfile(song)
path = r"D:\Batches\Songs"
os.chdir(path)
os.listdir()
['bang-bang.mp3', 'exception_hierarchy.png', 'Faded.mp3', 'FadedCopy.mp3', 'fifa world cup.mp3', 'file_handling_1.png', 'file_handling_2.png', 'song.mp3', 'songCopy.mp3']
file = os.listdir()
os.startfile(file)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    os.startfile(file)
TypeError: startfile: filepath should be string, bytes or os.PathLike, not list
os.startfile(random.choice(file))
os.startfile(random.choice(file))
os.startfile(random.choice(file))
os.startfile(random.choice(file))
import glob
glob.glob("*.mp3")
['bang-bang.mp3', 'Faded.mp3', 'FadedCopy.mp3', 'fifa world cup.mp3', 'song.mp3', 'songCopy.mp3']
glob.glob("*.png")
['exception_hierarchy.png', 'file_handling_1.png', 'file_handling_2.png']
files = glob.glob("*.mp3")
os.startfile(random.choice(files))
os.startfile(random.choice(files))
