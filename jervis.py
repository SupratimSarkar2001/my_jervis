import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe(): 
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
         speak("Good Evening!")
    speak("I am Nat sir, please tell how may I help you")               
def takeCommend():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio =r.listen(source)
    try:
        print("recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n") 
    except Exception as e:
        print(e)

        print("see that again...")
        return "None" 
    return query  




if __name__ == "__main__" :
    wishMe()
    while True:  
        query = takeCommend().lower()
        

        if "wikipedia" in query:
            speak("searching wikipedia.....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("Accirding to wikipedia....")
            print(results)
            speak(results)
        elif "open youtube " in query:  
            webbrowser.open("youtube.com") 
        elif "open Google " in query:  
            webbrowser.open("google.com")
        elif "play music"  in query:
            music_dir = "C:\\Users\\Supratim Sarkar\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif "the time " in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
        elif "open code" in query:
            codepath="C:\\Users\\Supratim Sarkar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif "open facebook" in query:
            webbrowser.open("facebook.com")       
                      
           




