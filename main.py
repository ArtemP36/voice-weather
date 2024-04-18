import pyttsx3 
import speech_recognition as sr 
import requests 
 
engine = pyttsx3.init() 
 
def speak(audio): 
    engine.say(audio) 
    engine.runAndWait() 
 
def welcome(): 
    print("Welcome back sir!") 
    speak("Welcome back sir!") 
 
def get_weather(city): 
    api_key = '64f60853740a1ee3ba20d0fb595c97d5' 
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric' 
    response = requests.get(base_url) 
    data = response.json() 
    if data['cod'] == 200: 
        weather_description = data['weather'][0]['description'] 
        temperature = data['main']['temp'] 
        speak(f"The weather in {city} is {weather_description} with a temperature of {temperature} degrees Celsius.") 
        print(f"The weather in {city} is {weather_description} with a temperature of {temperature} degrees Celsius.") 
    else: 
        speak("Sorry, I couldn't retrieve the weather information.") 
        print("Sorry, I couldn't retrieve the weather information.") 
 
def takecommand(): 
    r = sr.Recognizer() 
    with sr.Microphone() as source: 
        print("Listening...") 
        r.pause_threshold = 1 
        audio = r.listen(source) 
    try: 
        print("Recognizing...") 
        query = r.recognize_google(audio, language="en-in") 
        print(query) 
    except Exception as e: 
        print(e) 
        speak("Please say that again") 
        print("Please say that again") 
        return "Try Again" 
    return query 
 
if __name__ == "__main__": 
    welcome() 
    while True: 
        query = takecommand().lower() 
        if "weather in" in query: 
            city = query.split("in")[-1].strip() 
            get_weather(city) 
 
        else: 
            speak("I didn't understand") 
            print("I didn't understand")
