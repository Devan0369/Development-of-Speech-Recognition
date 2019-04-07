import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print ("Say Something")
    audio = r.listen(source)

with open("alfwavaudio.wav", "wb") as f:
    f.write(audio.get_wav_data())
