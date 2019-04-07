#Note you must have installed gTTS
#command for installation
#pip install gTTS

from gtts import gTTS
text=""
with open("alife_tts.txt","r") as file:
    for line in file:
        text=text + line


speech=gTTS(text,'en','slow')

speech.save("hello.mp3")
