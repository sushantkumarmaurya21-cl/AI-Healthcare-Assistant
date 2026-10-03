import speech_recognition as sr


def recognize_voice():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak now...")

        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            return text

        except Exception:
            return "Could not recognize voice"