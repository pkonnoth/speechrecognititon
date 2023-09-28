
import speech_recognition as sr
import pyttsx3
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
    """"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt='You said: ' + text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    ).choices[0].text
    """

    print("Assistant: " + text)
    engine = pyttsx3.init()
    engine.say(text)

    engine.runAndWait()


if __name__ == "__main__":
    while True:
        listen_for_speech()
