import datetime
import pyttsx3
import webbrowser
import speech_recognition as sr
import sounddevice as sd
import os

engine = pyttsx3.init()
engine.setProperty('rate', 180)

def speak(text):
    print(f"JARVIS: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        print("\nListening... (5 sec)")
        fs = 16000
        duration = 5
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
        sd.wait()
        audio_data = sr.AudioData(recording.tobytes(), fs, 2)
        r = sr.Recognizer()
        print("Recognizing...")
        command = r.recognize_google(audio_data)
        print(f"You said: {command}")
        return command.lower()
    except:
        print("Didn't catch that...")
        return ""

speak("Ultimate Safe JARVIS online Boss!")

while True:
    command = listen()
    if command == "": 
        continue

    # Time
    if "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}")

    # Music - play diana hamilton
    elif "play" in command:
        song = command.replace("play", "").strip()
        if song == "":
            song = "diana hamilton"
        speak(f"Playing {song} Boss!")
        webbrowser.open(f"https://www.youtube.com/results?search_query={song}")

    # YouTube
    elif "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    # Google
    elif "google" in command:
        query = command.replace("google", "").strip()
        if query:
            speak(f"Searching Google for {query}")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        else:
            webbrowser.open("https://google.com")

    # Apps
    elif "notepad" in command: 
        os.system("notepad")
    elif "calculator" in command: 
        os.system("calc")
    elif "code" in command or "vs code" in command: 
        os.system("code")
    elif "gmail" in command or "mail" in command:
        webbrowser.open("https://mail.google.com")

    # SAFE SHUTDOWN - needs 2 steps
    elif "shutdown laptop" in command or command == "shutdown":
        speak("Are you sure you want to shutdown? Say yes shutdown to confirm.")
        confirm = listen()
        if "yes" in confirm and "shutdown" in confirm:
            speak("Shutting down in 10 seconds. Say cancel shutdown to stop.")
            os.system("shutdown /s /t 10")
        else:
            speak("Shutdown cancelled.")

    elif "cancel shutdown" in command:
        os.system("shutdown /a")
        speak("Shutdown cancelled!")

    elif "restart" in command:
        speak("Are you sure you want to restart? Say yes restart.")
        confirm = listen()
        if "yes" in confirm:
            os.system("shutdown /r /t 10")
            speak("Restarting in 10 seconds!")
        else:
            speak("Restart cancelled.")

    # Exit JARVIS (not laptop)
    elif command in ["exit", "stop", "bye", "goodbye"]:
        speak("Goodbye Boss!")
        break

    else:
        speak(f"Heard {command}. Try play, time, youtube, google")
