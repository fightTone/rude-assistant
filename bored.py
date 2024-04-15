import speech_recognition as sr
from gtts import gTTS
import pyttsx3
import openai 
import sys
import subprocess
import time
import keyboard
from search_song import search_youtube_and_play
from get_credentials import get_creds
        
def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Hold Alt+G to start listening:")
        # keyboard.wait("F1")
        keyboard.wait("alt+g")
        start_time = time.time()
        print("Listening...")

        # Continue listening while the spacebar is held down
        while keyboard.is_pressed("alt+g"):
            audio = recognizer.listen(source)

            try:
                text = recognizer.recognize_google(audio)
                print("You said:", text)
                return text
            except sr.UnknownValueError:
                print("Sorry, could not understand audio.")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")

            # Check if spacebar is held down for at least 1 second
            duration = time.time() - start_time
            if duration > 1:
                return ''

    print("Alt+G released or held down for less than 1 second. Stopping listening.")
    return "" 

def text_to_speech1(text):
    # Using gTTS (Google Text-to-Speech)
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    print("Text-to-speech conversion completed. Check the output.mp3 file.")
    # Alternatively, using pyttsx3
    # engine = pyttsx3.init()
    # engine.say(text)
    # engine.save_to_file(text, 'output.mp3')
    # engine.runAndWait()

def text_to_speech2(text):
    # Using pyttsx3 for text-to-speech
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def chat_with_gpt3():
    open_commands = [
        "open code",
        "open terminal",
        "open spotify",
        "open slack"
    ]
    openai.api_key = get_creds("chatgpt")
    messages = [ {"role": "system", "content": "You are a intelligent assistant."} ] 
    greetings = "Didst thou just disturbeth me in my slumber? How rude of thee! Bow and Address me afore thou deign to speak. I bide my time..."
    print(greetings)
    text_to_speech2(greetings)
    i = 0
    while True:
        reply = ''
        spoken_text = speech_to_text()
        message = spoken_text
        if message == "exit now":
            exit_message = "Thy inquiries and entreaties bear the mark of mediocrity, a reflection of thy meager understanding. Thou art but a novice in this realm of discourse. Seek me henceforth only in direst need, though I wager 'twill be with increasing frequency henceforth. Fare thee well."
            print(exit_message)
            text_to_speech2(exit_message)
            sys.exit()
        elif message == '':
            text_to_speech2("are you mute?. did i choked you with my balls?")
        elif message == "open code":
            subprocess.run([r"C:\Users\qgee1\AppData\Local\Programs\Microsoft VS Code\bin\code.cmd"])
            text_to_speech2(f"Done {message}.             are you happy now?".replace("open", "opening"))
        elif message == "open terminal":
            subprocess.run(["wt"])
            text_to_speech2(f"Done {message}.             are you happy now?".replace("open", "opening"))
        elif message == "open spotify":
            subprocess.run(["spotify"])
            text_to_speech2(f"Done {message}.             are you happy now?".replace("open", "opening"))
        elif message == "open slack":
            subprocess.run([r"C:\Users\qgee1\AppData\Local\slack\slack.exe"])
            text_to_speech2(f"Done {message}.             are you happy now?".replace("open", "opening"))
        elif message.split()[0] == "play":
            song_searched = message.split()[1:]
            search_youtube_and_play(song_searched)
        elif message not in open_commands: 
            messages.append( 
                {"role": "user", "content": message}, 
            ) 
            chat = openai.ChatCompletion.create( 
                model="gpt-3.5-turbo", messages=messages 
            ) 
            reply = chat.choices[0].message.content 

        rude = "Is that all  ?  thats not challenging at all."
        rude_reply = f"{reply}. {rude}" if i != 0 else reply
        print(f"ChatGPT: {reply}") 
        text_to_speech2(rude_reply)
        if reply:
            messages.append({"role": "assistant", "content": reply}) 
        i=1



chat_with_gpt3()

# spoken_text = speech_to_text()
# print(f"so u'r saying>> {spoken_text}")
# if spoken_text:
#     # spoken_text = "fuck you fuck you fuck you!!!!"
#     text_to_speech2(spoken_text)

