import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print ("Say Something")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print ("You said", text)
except:
    print ("Translation Failed")
