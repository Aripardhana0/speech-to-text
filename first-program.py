from gtts import gTTS
import os

# Providing the text
input_text = "Hello, I am the first program. In this program, you will convert the text within this program into speech. In the second program, you will convert the text from a .txt file into speech."

# Setting the language
language = "en"

# Passing to gtts engine
voice = gTTS(text=input_text, lang=language, slow=False)

# Creating and saving the audio file
voice.save("first.mp3")

# Playing the file
os.system("start first.mp3")