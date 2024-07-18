### README

# Jarvis Virtual Assistant

This project implements a virtual assistant named Jarvis, which can perform various tasks such as opening websites, playing music, and fetching news headlines using voice commands. It utilizes speech recognition, text-to-speech, and the OpenAI GPT-3.5 model for natural language processing.

## Features

- Open popular websites (Google, WhatsApp, YouTube)
- Play music from a predefined music library
- Fetch and read top news headlines
- Process general queries using OpenAI's GPT-3.5 model

## Requirements

- Python 3.6 or higher
- Required Python libraries:
  - `requests`
  - `speech_recognition`
  - `webbrowser`
  - `pyttsx3`
  - `openai`

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/deveshyaara/jarvis-assistant.git
   cd jarvis-assistant
   ```

2. **Install dependencies:**
   ```sh
   pip install requests speechrecognition pyttsx3 openai
   ```

3. **Install PyAudio:**
   - On Windows:
     ```sh
     pip install pyaudio
     ```
   - On macOS/Linux, you might need additional steps. Refer to [PyAudio documentation](https://people.csail.mit.edu/hubert/pyaudio/) for instructions.

4. **Set your API keys:**
   - Replace `YOUR_NEWS_API_KEY` with your actual News API key.
   - Replace `YOUR_OPENAI_API_KEY` with your actual OpenAI API key.

## Usage

1. **Create a music library:**
   - Ensure you have a `musicLibrary` dictionary with song names and their respective URLs. Example:
     ```python
     musicLibrary = {
         "songname": "https://www.example.com/song.mp3"
     }
     ```

2. **Run the script:**
   ```sh
   python main.py
   ```

3. **Interacting with Jarvis:**
   - Say "Jarvis" to activate the assistant.
   - Give commands such as "open Google", "open WhatsApp", "play [songname]", or "news".

## Example Code

```python
import requests
import speech_recognition as sr
import webbrowser 
import pyttsx3
from openai import OpenAI

# Replace with your actual API key
apikey = "YOUR_NEWS_API_KEY"
openai_api_key = "YOUR_OPENAI_API_KEY"

# Ensure you have a module or dictionary named musicLibrary with a music dictionary
musicLibrary = {
    "songname": "https://www.example.com/song.mp3"
}

r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    client = OpenAI(api_key=openai_api_key)
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud"},
            {"role": "user", "content": command}
        ]
    )
    response = completion.choices[0].message.content
    print(response)
    return response

def processCommand(c):
    print(c)
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://web.whatsapp.com/")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")
    elif c.lower().startswith("play"):
        song = c.lower().split("play ", 1)[1]
        link = musicLibrary.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak("Sorry, I couldn't find the song.")
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={apikey}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles',[])
            for article in articles:
                speak(article['title'])
        else:
            speak("Unable to fetch news at the moment.")
    else:
        output = aiProcess(c)
        speak(output)

if __name__== "__main__":
    speak("Initializing Jarvis.....")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening.....")
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
            print("Recognizing.....")
            command = r.recognize_google(audio)
            if(command.lower()=="jarvis"):
                speak("Yes Boss")
                with sr.Microphone() as source:
                    print("Jarvis active.....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)
        except sr.UnknownValueError:
            print("Jarvis could not understand audio")
        except sr.RequestError as e:
            print(f"Jarvis error; {e}")
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start")
```

## Notes

- Ensure your microphone is properly connected and working.
- Adjust `timeout` and `phrase_time_limit` values if you encounter issues with speech recognition.
- You can expand the `musicLibrary` dictionary with more songs and their URLs as needed.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

Feel free to customize and extend the functionalities of Jarvis as per your requirements. Happy coding!
