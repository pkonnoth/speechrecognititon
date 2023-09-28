import speech_recognition as sr
from gtts import gTTS
import os


def listen_for_speech():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    print("Listening...")
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
        respond_to_speech(text)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))


def respond_to_speech(text):
    print("Assistant: " + text)
    tts = gTTS(text)
    tts.save("output.mp3")
    os.system("mpg123 output.mp3")  # Use a command-line player to play the audio.


if __name__ == "__main__":
    while True:
        listen_for_speech()
