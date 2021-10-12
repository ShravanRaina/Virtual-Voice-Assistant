from os import terminal_size
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyjokes
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def WishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        print("Good Morning!")
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        print("Good Afternoon!")
        speak("Good Afternoon!")
    else:
        print("Good Evening!")
        speak("Good Evening!")

    print("Hi! I am your Voice Assistant, How may I help you?")
    speak("Hi! I am your Voice Assistant, How may I help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        speak("User said" + query)

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    WishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            
            print('Searching Wikipedia...')
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
          
            print("According to Wikipedia...")
            speak("According to Wikipedia...")
            print(results)
            speak(results)

        elif 'open beginners book' in query:
            print("Opening beginners book...")
            speak("Opening beginners book...")
            webbrowser.open("beginnersbook.com")

        elif 'open whatsapp web' in query:
            print("Opening Whatsapp Web...")
            speak("Opening Whatsapp Web...")
            webbrowser.open("web.whatsapp.com")

        elif 'open flipkart' in query:
            print("Opening Flipkart...")
            speak("Opening Flipkart...")
            webbrowser.open("flipkart.com")

        elif 'open geeks for geeks' in query:
            print("Opening Geeks for Geeks...")
            speak("Opening Geeks for Geeks...")
            webbrowser.open("https://www.geeksforgeeks.org/")

        elif 'play music' in query:
            music_dir = " "  // Give the path of your music folder
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'exit' in query:
            print("Exited...")
            exit()

        elif 'how are you' in query:
            print("I am fine, Thank you")
            speak("I am fine, Thank you")
            print("How are you, Sir")
            speak("How are you, Sir")

        elif 'fine' in query:
            print("It's good to know that you are fine!")
            speak("It's good to know that you are fine!")

        elif 'open youtube' in query:
            print("Here you go to youtube\n")
            speak("Here you go to youtube\n")
            webbrowser.open("https://www.youtube.com/")
        
        elif 'open gmail' in query:
            print("Here you go to gmail\n")
            speak("Here you go to gmail\n")
            webbrowser.open("https://mail.google.com/mail/")

        
        elif 'joke' in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)

        elif "don't listen" in query or "stop listening" in query:
            print("For how much time you want to stop me from listening commands?")
            speak("For how much time you want to stop me from listening commands?")
            a = int(takeCommand())
            time.sleep(a)
            print(a)
            speak(a)

        elif "what's your name" in query or "What is your name" in query:
            print("My friends call me Voice assistant")
            speak("My friends call me voice assistant")

        elif 'open google web page' in query:
            print("Here you go to Google\n")
            speak("Here you go to Google\n")
            webbrowser.open("google.com")

        elif 'open instagram' in query:
            print("Opening Instagram...")
            speak("Opening Instagram...")
            webbrowser.open("instagram.com")

        elif 'open twitter' in query:
            print("Opening Twitter...")
            speak("Opening Twitter...")
            webbrowser.open("twitter.com")

        elif 'open linkedin' in query:
            print("Opening LinkedIn...")
            speak("Opening LinkedIn...")
            webbrowser.open("linkedin.com")

        elif 'open facebook' in query:
            print("Opening Facebook...")
            speak("Opening Facebook...")
            webbrowser.open("facebook.com")

        elif 'open opera' in query:
            print("Opening Opera...")
            speak("Opening Opera...")
            webbrowser.open("opera.com")

        elif 'open discord' in query:
            print("Opening discord...")
            speak("Opening discord...")
            webbrowser.open("https://discord.com/")

        elif 'open yahoo' in query:
            print("Opening yahoo...")
            speak("Opening yahoo...")
            webbrowser.open("https://in.yahoo.com/")

        elif 'open python' in query:
            print("Opening python...")
            speak("Opening python...")
            webbrowser.open("https://www.python.org/")

        elif 'open google meet' in query:
            print("Opening Google Meet...")
            speak("Opening Google Meet...")
            webbrowser.open("https://meet.google.com/")

        elif 'open Paytm' in query:
            print("Opening PAYTM...")
            speak("Opening PAYTM...")
            webbrowser.open("https://paytm.com//")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The time is {strTime}")
            speak(f"The time is {strTime}")

        elif "who made you" in query or "who created you" in query:
            print("I have been created by Group I9 from Vishwakarma Institute of Technology.")
            speak("I have been created by Group I9 from Vishwakarma Institute of Technology.")

        elif 'open snakify' in query:
            webbrowser.open('https://snakify.org/en/')
            print("Opening Snakify...")
            speak("Opening Snakify...")
        
        elif 'open hackerrank' in query:
            webbrowser.open('https://www.hackerrank.com/')
            print("Opening HackerRank...")
            speak("Opening HackerRank...")
        
        elif 'open google drive' in query:
            webbrowser.open('https://drive.google.com')
            print("Opening Google Drive...")
            speak("Opening Google Drive...")
        
        
