import re
import speech_recognition

recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("say something")
    audio = recognizer.listen(source)

words = recognizer.recognize_google(audio)

matches = re.search("my name is (.*)",words)
if matches:
    print(f"hey,{matches[1]}.")
elif words == "hello":
    print("hey you.")
else:
    print("I CANT HEAR YOU")