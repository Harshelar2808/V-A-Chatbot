import datetime
import wikipedia
import speech_recognition as sr
import pyttsx3
import pywhatkit
import pyjokes_hebrew

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening.......')
            voice = listener.listen(source)
            command = listener.recognize_google_cloud(voice)
            command = command.lower()
            if 'Jarvis' in command:
                command = command.replace('Jarvis', '')
                print(command)
    except:
        pass
    return command


def run_Jarvis():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        print(song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'day' in command:
        day = datetime.datetime.now().strftime('%A')
        print(day)
        talk('Current day is ' + day)
    elif 'date' in command:
        d = datetime.date.today().strftime('%d-%m-%Y')
        print(d)
        talk('Current date is ' + d)
    elif 'tell me about' in command:
        info = command.replace('tell me about', '')
        about = wikipedia.summary(info, 1)
        print(about)
        talk(about)
    elif 'joke' in command:
        talk(pyjokes_hebrew.get_random_joke())
    else:
        talk('Please can you say it again.')


while True:
    run_Jarvis()
