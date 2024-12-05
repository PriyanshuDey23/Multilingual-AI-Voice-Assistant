import speech_recognition as sr
import google.generativeai as genai
from dotenv import load_dotenv
import os
from gtts import gTTS

# Load environment variables from .env file
load_dotenv()

# Set up the API key for Google Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))



# Voice input
def voice_input():
    r=sr.Recognizer()

    # Take the input form microphone
    with sr.Microphone() as source:
        print("listening...")
        audio=r.listen(source)

    try:
        text=r.recognize_google(audio) # Convert audio to text
        print("you said: ", text)
        return text
    except sr.UnknownValueError:
        print("sorry, could not understand the audio")
    except sr.RequestError as e:
        print("could not request result from google speech recognition service: {0}".format(e))
    


# Function for converting text to speech
def text_to_speech(text):
    tts=gTTS(text=text, lang="en")
    
    #save the speech from the given text in the mp3 format
    tts.save("speech.mp3")

# Function to get a response from the Gemini model
def llm_model(user_text):   
    model = genai.GenerativeModel('gemini-1.5-flash-8b')
    response=model.generate_content(user_text)
    return response.text