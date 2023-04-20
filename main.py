import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia

listener=sr.Recognizer()
def speaks(texts):
    engine = pyttsx3.init()  # object creation
    engine.setProperty('rate', 125)
    engine.setProperty('volume', 1.0)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(texts)
    engine.runAndWait()
    engine.stop()
def listen():
    try:
        with sr.Microphone() as source:
        print("listeninig......")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        #command = input("bot : ")
        command = command.lower()
        if "bot" in command:
            command = command.replace("bot ", " ")
            speaks(command)
        return command


    except:

        print("there is error in vive")
def run_command():
    commands = listen()
    print(commands)
    if 'play' in commands:
        commands=commands.replace("play","")
        print("playing")
        pywhatkit.playonyt(commands)

    elif 'time' in commands:
        time=datetime.datetime.now().strftime('%H:%M %p')
        print(time)
        speaks("the time is "+ time)
    elif 'who is' in commands:
        try:
            person = commands.replace('who is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            speaks(info)
        except:
            speaks("i don't understand "+person)

    elif "are you singe" in commands:
        speaks("i am bot  ")
    elif "who are you" in commands:
        speaks("i a'm chat bot is a piece of software that interacts with a human through written language")
    else:
        speaks("i don't understand what you mean ")



run_command()