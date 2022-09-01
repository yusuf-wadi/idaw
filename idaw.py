from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import speech_recognition as sr
import pyttsx3
#import openai
from gpt_j.Basic_api import simple_completion



# openai.api_key_path = "key.txt"
# cur_model = "text-davinci-002"


# Define Brave path
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser-Nightly/Application/brave.exe"
options = webdriver.ChromeOptions()
options.binary_location = brave_path

# set dl options
prefs = {"download.default_directory": "C:/Users/thewa/Desktop/projects/computational_neuroscience/AI_ML/projects/mun_ching/crawlers/content"}

options.add_experimental_option("prefs", prefs)

# Create new automated instance of Brave
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

with sr.Microphone() as source:
    print('Listening...')
    engine.say("Hey I'm your bot, BOB! What can I do for you today?")
    engine.runAndWait()
    audio = r3.listen(source)

    
# From here
def qCommand(x):

    print('\n' + x + '\n')

    if 'YouTube' in x:
    
            r2 = sr.Recognizer()
            driver.get('https://www.youtube.com/')

            with sr.Microphone() as source:
                engine.say("What do you want to see?")
                engine.runAndWait()
                print('')
                audio = r2.listen(source)
                keyword = r2.recognize_google(audio)
                YOUR_PROMPT = "Extract a search query from the prompt: " + '"' + keyword + '"' 

                # completion = openai.Completion.create(
                #     model=cur_model,
                #     prompt=YOUR_PROMPT,
                #     temperature=0,
                #     frequency_penalty=0.5,
                #     max_tokens=20,


                # )

                # keyword = completion.choices[0].text

     

                elem = driver.find_element('xpath', '//input[@id="search"]')
                elem.click()
                elem.send_keys(response, Keys.RETURN)

                

            try:
                get = r2.recognize_google(audio)
                print(get)
            except sr.UnknownValueError:
                print('Client side error')
            except sr.RequestError:
                print('Error on my side')

            # Till here is the code to run a YouTube vid

    else:
            print("command not recognized")


    
qCommand(r2.recognize_google(audio))
