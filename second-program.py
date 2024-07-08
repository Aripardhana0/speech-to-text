# Importing the library
from gtts import gTTS
import os

# Providing the text file
f = open("text.txt", "r")
# reading the file
input_text = f.read().replace("\n", " ")

# Setting the language
language = "en"

# Passing to gtts engine
voice = gTTS(text=input_text, lang=language, slow=False)

# Creating and saving the audio file
voice.save("second.mp3")

# Playing the file
os.system("start second.mp3")