import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import sys



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.getProperty('voices')


def speak(audio):
  engine.say(audio)
  engine.runAndWait()

def wishMe():
  hour = int(datetime.datetime.now().hour)
  if hour>=0 and hour<12:
    speak("Good morning sir !")
  elif hour>=12 and hour<16:
    speak("Good afternoon sir!")
  elif hour>=16 and hour<20:
    speak("Good evening sir!")
  else:
    speak("Good night sir!")

  speak("I am matho, How can i help you!")

def takeCommand():
  r = sr.Recognizer()
  with sr.Microphone() as source:
    print("Listening ......")
    r.pause_threshold = 1
    audio = r.listen(source)
  try:
    print("Recognizing...")
    query = r.recognize_google(audio, language='en-in')
  except Exception as e:
    print(e)
    speak("Say that again please...")
    return "none"
  return query



if __name__ == "__main__":
  wishMe()
  while True:
    query = takeCommand().lower()
    if 'wikipedia' in query:
      speak("searching wikipedia...")
      query = query.replace("wikipedia","")
      results = wikipedia.summary(query, sentences=2)
      speak("According to wikipedia")
      speak(results)
    elif 'open youtube' in query:
      webbrowser.open("youtube.com")
    elif 'open google' in query:
      webbrowser.open('https://www.google.com')
    elif 'play music' in query:
      music_dir = 'E:\\mymind'
      songs = os.listdir(music_dir)
      os.startfile(os.path.join(music_dir,songs[1]))
    elif 'the time' in query:
      strTime = datetime.datetime.now().strftime("%H:%M:%S")
      speak("sir the time is")
      speak(strTime)
    elif 'what is your name' in query:
      speak("I am Matho")
    elif 'who create' in query:
      speak("rohit kumar mishra creates me")
    elif 'coders' in query:
      speak("sarscoders is a coding team of government  polytechnic koderma. which is created by Abhisek Yadav and suman raj patel from batch 2K16 19. current member of sarscoders is rajnish raj, Abhishek Yadav, suman raj patel and rohit Kumar mishra.")
    elif 'play something' in query:
        music_dir = 'E:\\myfavmusic'
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[0]))
    elif 'search' in query:
      query = query.replace("search", "")
      webbrowser.open('https://www.google.com/search?q=' + query)
    elif 'video' in query:
      query = query.replace("video", "")
      webbrowser.open('https://www.youtube.com/results?search_query='+query)
    elif 'friends' in query:
      speak("sab chutiye hai sale")
    elif "ok done" in query:
      speak("thank you sir")
      sys.exit(0)