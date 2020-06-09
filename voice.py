import re
import speech_recognition

recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Hello, what's your name?")
    audio = recognizer.listen(source)

words = recognizer.recognize_google(audio)

matches = re.search("my name is (.*)",words)
if matches:
    print(f"hey,{matches[1]}.")
elif re.search('hello',words):
    print("what's your name")
else:
    print('bye')