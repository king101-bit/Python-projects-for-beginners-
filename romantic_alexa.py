import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):


engine.say('I am your assistant')
engine.say('What can i do for you today?')
engine.runAndWait()
try:
    with sr.Microphon() as source:
        print('Listening....')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'alexa' in command:
        print(command)
except:
    pass
