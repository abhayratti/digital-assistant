import speech_recognition
import pyttsx3
from assistant import Assistant

ENGINE = pyttsx3.init()

def listen():
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        return audio
        
def audio_to_text(audio):
    recognizer =  speech_recognition.Recognizer()
    try: 
        text = recognizer.recognize_google(audio)
        return text    
    except:
        return ""
    
def speak(text):
    ENGINE.say(text) # add to queue
    ENGINE.runAndWait() # go through queue

assistant = Assistant("config/api_keys.json")
    
while True:
    user_sentence = audio_to_text(listen())
    print(user_sentence)

    if user_sentence == "":
        continue

    if user_sentence == "goodbye":
        speak("See ya later!")
        quit()

    prompt = user_sentence
    assistant_response = assistant.get_response(prompt)
    print(f"Responding: {assistant_response}")

    speak(assistant_response)
