<<<<<<< HEAD
import os
import speech_recognition as sr
=======

import os
import speech_recognition as sr

>>>>>>> 0b42833416bf8e8fa7b99b623143f63649108da2
import pyttsx3 as py
import datetime as dt
import wikipedia as wiki
import webbrowser as wb
import pyjokes as pj

import google.generativeai as gen

<<<<<<< HEAD
gen.configure(api_key='Your_api_key' )
=======
gen.configure(api_key="Your_Api_Key")

>>>>>>> 0b42833416bf8e8fa7b99b623143f63649108da2

def gemini_reply(prompt):
    model = gen.GenerativeModel("gemini-1.5-flash")  # Fast & free
    response = model.generate_content(prompt)
    return response.text
<<<<<<< HEAD
=======

>>>>>>> 0b42833416bf8e8fa7b99b623143f63649108da2
# Predefined common sites
sites = {
    "youtube": "https://youtube.com",
    "google": "https://google.com",
    "facebook": "https://facebook.com",
    "instagram": "https://instagram.com",
    "twitter": "https://twitter.com",
    "github": "https://github.com",
    "linkedin": "https://linkedin.com",
}

def open_website(query):
    for name, url in sites.items():
        if name in query:
            wb.open(url)
            return f"Opening {name}..."
    # If not in dictionary, try guessing
    words = query.split()
    for word in words:
        if word not in ["open", "website"]:
            wb.open(f"https://{word}.com")
            return f"Opening {word}.com ..."
    return "Sorry, I couldn't figure out which website to open."

<<<<<<< HEAD
=======

>>>>>>> 0b42833416bf8e8fa7b99b623143f63649108da2
def speak(text):
    print(f"Assistant: {text}")
    try:
        engine = py.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.say(text)
        engine.runAndWait()
    except:
        print("Speech output not supported in Colab.")

def greet():
    hour = int(dt.datetime.now().hour)
    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your voice assistant. How can I help you today?")

<<<<<<< HEAD
=======


>>>>>>> 0b42833416bf8e8fa7b99b623143f63649108da2
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            return r.recognize_google(audio).lower()
        except:
            return "Sorry, I didn't catch that."

def write_query(query):
    print(f"User query : {query}")


def open_app(query):
    if "notepad" in query:
        os.system("notepad")
        return "Opening Notepad..."
    elif "calculator" in query:
        os.system("calc")
        return "Opening Calculator..."
    else:
        return "Sorry, I don't know that app."
<<<<<<< HEAD

=======
>>>>>>> 0b42833416bf8e8fa7b99b623143f63649108da2

def run():
    greet()
    while True:
<<<<<<< HEAD

=======
>>>>>>> 0b42833416bf8e8fa7b99b623143f63649108da2
        query = listen()
        write_query(query)

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                result = wiki.summary(query, sentences=2)
                speak("According to Wikipedia:")
                speak(result)
            except:
                speak("Sorry, I couldn't find anything.")

<<<<<<< HEAD
        elif "open" in query and "website" in query :
            response = open_website(query)
            speak(response)
=======
        elif "open" in query and "website" in query or "open" in query:
            response = open_website(query)
            speak(response)

>>>>>>> 0b42833416bf8e8fa7b99b623143f63649108da2

        elif 'time' in query:
            strTime = dt.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {strTime}")

        elif 'joke' in query:
            joke = pj.get_joke()
            speak(joke)

        elif "learn" in query:
            speak("learn anything.......")
            wb.open('https://learn-anything.xyz/')

        elif "open" in query:
            response = open_app(query)
            speak(response)
<<<<<<< HEAD

=======
>>>>>>> 0b42833416bf8e8fa7b99b623143f63649108da2
        elif 'exit' in query or 'bye' in query:
            speak("Goodbye! Have a nice day!")
            break

        else:
<<<<<<< HEAD
=======
            speak("Let me think...")
>>>>>>> 0b42833416bf8e8fa7b99b623143f63649108da2

            answer=gemini_reply(query)
            speak(answer)
run()
<<<<<<< HEAD
=======

>>>>>>> 0b42833416bf8e8fa7b99b623143f63649108da2
