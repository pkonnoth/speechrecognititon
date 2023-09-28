import speech_recognition as sr
from gtts import gTTS
import os
import openai

openai.api_key = "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"


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

    # Use gTTS to convert the text to speech
    tts = gTTS(text)
    tts.save("output.mp3")

    # Play the generated audio using a command-line player (e.g., mpg123)
    os.system("mpg123 output.mp3")


if __name__ == "__main__":
    while True:
        listen_for_speech()
