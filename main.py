import speech_recognition as sr
from time import ctime

r = sr.Recognizer()


def record_audio():
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            print('Sorry, I did not get that')
        except sr.RequestError:
            print('Sorry, my speech service is down')
        return voice_data


def respond(voice_data):
    if 'what is your name' in voice_data:
        print('My name is Grant')
    if 'what time is it' in voice_data:
        print(ctime())


print('How can I help you?')
voice_data = record_audio()
print(voice_data)
respond(voice_data)
