import pyttsx3

tts = pyttsx3.init()

tts.say("Hello. My Name Is JARVIS. And Your Name Is?")
tts.runAndWait()

name = input("Your name:")

tts.say("Nice to meet you " + name)
tts.runAndWait()

tts.say("Would you like to be my friend?")
tts.runAndWait()

answer = input("Answer:")

if(answer == "yes"):
    tts.say("Thanks for accepting my friendship!")
else:
    tts.say("Thanks for your answer.")

tts.runAndWait()

if(answer == "yes"):
    tts.say("Would you like to play a game with me?")

tts.runAndWait()

gameRequest = input("Answer:")

if(gameRequest == "yes"):
    tts.say("Ok, Lest go and play a game together.")
else:
    tts.say("Ok, No problem. Anyway i will play alone.")

tts.runAndWait()