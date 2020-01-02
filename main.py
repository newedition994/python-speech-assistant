import speech_recognition as sr
from time import ctime
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS

# some issues with pyaudio for the speech recognition but should work

r = sr.Recognizer()


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            grant_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            grant_speak('Sorry, I did not get that')
        except sr.RequestError:
            grant_speak('Sorry, my speech service is down')
        return voice_data


def grant_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound((audio_file))
    print(audio_string)
    os.remove(audio_file)


def respond(voice_data):
    if 'what is your name' in voice_data:
        grant_speak('My name is Grant')
    if 'what time is it' in voice_data:
        grant_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want search')
        url = 'http://google.com/search?q=' + search
        webbrowser.get().open(url)
        grant_speak('Here is what I found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('What is the location')
        url = 'http://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        grant_speak('Here is what I found for ' + location)
    if 'exit' in voice_data:
        exit()


time.sleep(1)
grant_speak('How can I help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)
