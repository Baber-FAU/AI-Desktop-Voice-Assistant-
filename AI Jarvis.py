import pyttsx3  # Text-to-speech library
import speech_recognition as sr  # Speech recognition library
import datetime  # For handling date and time
import wikipedia  # Wikipedia API
import webbrowser  # To open web browsers
import os  # To interact with the operating system

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')  # Use Windows built-in voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Set the voice property

def speak(audio):
    """Convert text to speech."""
    engine.say(audio)            
    engine.runAndWait()  # Run the speech engine

def wishMe():
    """Wish the user based on the time of day."""
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:  # Morning
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:  # Afternoon
        speak("Good Afternoon")
    else:  # Evening
        speak("Good Evening!")

    speak("I am Jarvis, sir. Please tell me how may I help you")

def takeCommand():
    """Take audio input from the user and return recognized text."""
    r = sr.Recognizer()  # Create a recognizer instance
    with sr.Microphone() as source:  # Use the microphone as the source
        print("Listening...")  # Indicate that the assistant is listening
        r.pause_threshold = 1  # Set the threshold for pauses
        audio = r.listen(source)  # Listen for audio input

    try:  # Try to recognize the speech
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Recognize speech using Google API
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")  # Error handling
        return "None"  # Return "None" if recognition fails
    return query  # Return the recognized text

def search_wikipedia(query):
    """Search Wikipedia for the given query."""
    speak('Searching Wikipedia...')
    query = query.replace("wikipedia", "")  # Remove 'wikipedia' from the query
    results = wikipedia.summary(query, sentences=2)  # Get summary from Wikipedia
    speak("According to Wikipedia")
    print(results)
    speak(results)  # Speak the results

def open_website(website):
    """Open the specified website in a web browser."""
    webbrowser.open(website)  # Open the website

def play_music():
    """Play music from the specified directory."""
    music_dir = 'C:\\music'  # Path to the music directory
    songs = os.listdir(music_dir)  # List all songs in the directory
    if songs:  # Check if there are any songs
        os.startfile(os.path.join(music_dir, songs[0]))  # Play the first song
    else:
        speak("No music files found in the directory.")  # Handle case with no music files

if __name__ == "__main__":
    wishMe()  # Greet the user
    while True:
        query = takeCommand().lower()  # Take command and convert to lowercase

        # Logic for executing tasks based on the recognized query
        if 'wikipedia' in query:
            search_wikipedia(query)  # Search Wikipedia

        elif 'open youtube' in query:
            open_website("youtube.com")  # Open YouTube
            
        elif 'open google' in query:
            open_website("google.com")  # Open Google
            
        elif 'open stackoverflow' in query:
            open_website("stackoverflow.com")  # Open Stack Overflow
        
        elif 'open whatsapp' in query:
            open_website("whatsapp.com")  # Open WhatsApp
        
        elif 'open facebook' in query:
            open_website("facebook.com")  # Open Facebook
        
        elif 'play music' in query:  # Play music
            play_music()  # Call the play_music function

        elif 'the time' in query:  # Check the time
            strTime = datetime.datetime.now().strftime("%H:%M:%S")  # Get current time
            speak(f"Sir, the time is {strTime}")  # Speak the time

        elif 'open code' in query:  # Open Visual Studio Code
            codePath = "C:\\Users\\Baber ALI\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)  # Launch Visual Studio Code
            
        elif 'word' in query:  # Open Microsoft Word
            codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(codePath)  # Launch Microsoft Word

        elif 'stop' in query:  # Exit the loop if the user says "stop"
            speak("Goodbye!")  # Say goodbye
            break  # Break the loop
