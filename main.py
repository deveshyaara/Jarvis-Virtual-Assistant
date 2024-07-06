import speech_recognition as sr
import webbrowser 
import pyttsx3


r = sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    print(c)
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://web.whatsapp.com/")
   
if __name__== "__main__":
    speak("Initializing Jarvis.....")
    while True:
        #Listen for the wake word for jarvis
        # obtain audio from the microphone
        
        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Listening.....")
                audio = r.listen(source, timeout=2,phrase_time_limit=1)
            print("Recognizing.....")
            command = r.recognize_google(audio)
            if(command.lower()=="jarvis"):
                speak("Yessss Bosssssss")
                with sr.Microphone() as source:
                    print("Jarvis active.....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)
        except sr.UnknownValueError:
            print("Jarvis could not understand audio")
        except sr.RequestError as e:
            print("Jarvis error; {0}".format(e))
