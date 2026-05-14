# Import the required module for text 
# to speech conversion
from gtts import gTTS
import time 
# This module is imported so that we can 
# play the converted audio
import os

# The text that you want to convert to audio
l =['Ali','shahry baby','sail is dog.Dafa ho.']


# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
for i in l:
    myobj = gTTS(text=f'Hallo {i}', lang='en')
    # Saving the converted audio in a mp3 file named
    # welcome 
    myobj.save('a.mp3')
    # Playing the converted file
    os.system("start a.mp3")    
    # Wait for a few seconds to allow the audio to finish playing
    time.sleep(1)  # Adjust the sleep time as needed


