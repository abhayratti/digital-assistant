import speech_recognition
import pyttsx3

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
    
while True:
    user_sentence = audio_to_text(listen())
    print(user_sentence)
    
    if user_sentence == "goodbye":
        speak("See ya later!")
        quit()
    else: 
        speak(user_sentence)