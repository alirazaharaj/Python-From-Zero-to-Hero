from gtts import gTTS
import os
import time

myobj = gTTS(text='Hallo Ali Please drink water', lang='en')
myobj.save('my.mp3')
while True:
    os.system('my.mp3')
    time.sleep(10)

