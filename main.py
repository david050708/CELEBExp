import speech_recognition as sr
import pyttsx3
import wikipedia


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
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'CelebExp' in command:
                command = command.replace('CelebExp', '')
                print(command)
    except:
        pass
    return command


def run_CelebExp():
    command = take_command()
    print(command)
    if 'who is' in command:
        person = command.replace('who the is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'bye' in command:
        talk("Ok then, see you later")
        print("Ok then, see you later") 

    else:
        talk("I didn't get that clearly, please repeat it")
   
while True:
    run_CelebExp()
