import speech_recognition as sr
import pyttsx3
import requests
import translators as ts
import os
import webbrowser

engine = pyttsx3.init()
voices = engine.getProperty("voices")
recognizer = sr.Recognizer()
engine.setProperty('voice', voices[1].id)

# def cmd():
#     with sr.Microphone() as source:
#         print("Katakan perintah anda!")
#         recognizer.pause_threshold = 3
#         recognizer.adjust_for_ambient_noise(source)
#         recorderaudio = recognizer.listen(source, timeout=2, phrase_time_limit=5)
#     try:
#         print('Loading...')
#         command = recognizer.recognize_google(recorderaudio, language='id').lower()
#         print('Perintah:', str(command))

#         if 'jam' in command:
#             time = datetime.datetime.now().strftime('%I:%M %p')
#             print(time)
#             engine.say(time)
#             engine.runAndWait()
#         elif "keluar" in command:
#             engine.say("Perintah diterima!")
#             engine.runAndWait()
#             exit()
#         else:
#             engine.say("Tidak ada perintah seperti itu.")
#             engine.runAndWait()
#             exit()
#     except sr.UnknownValueError:
#         engine.say("Maaf, saya tidak bisa mengerti apa yang Anda katakan. Silakan coba lagi.")
#         engine.runAndWait()
#     except sr.RequestError:
#         engine.say("Maaf, saya mengalami masalah saat mengakses layanan Google Speech Recognition.")
#         engine.runAndWait()
#     except Exception as ex:
#         print(ex)

# while True:
#     cmd()
def user():
    with sr.Microphone() as source: 
        print("Katakan sesuatu!")
        recognizer.pause_threshold = 3
        recognizer.adjust_for_ambient_noise(source)
        recorderaudio = recognizer.listen(source, timeout=1, phrase_time_limit=5)
        engine.runAndWait()
    try:
        print('Loading...')
        command = recognizer.recognize_google(recorderaudio, language='id').lower()
        print('User:', str(command))

        if "hai" in command:
            api_key = "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"
            url = "https://api.groq.com/openai/v1/chat/completions"
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
            data = {
                "model": "mixtral-8x7b-32768",
                "messages": [{"role": "user", "content": command.replace("hai", "")}]
            }
            response = requests.post(url, headers=headers, json=data)
            get__data = response.json()['choices'][0]['message']['content']
            res = ts.translate_text(get__data, to_language='id')
            print("Bot:", res)
            engine.say(res)
            engine.runAndWait()
        elif "buka" in command:
            if "notepad" in command:
                os.startfile('C:\\Windows\\notepad.exe')
            if "cmd" in command:
                os.startfile('C:\\Users\\rimur\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.exe')
        elif "keluar" in command:
            print("Bot: Perintah Diterima")
            engine.say("Perintah diterima!")
            engine.runAndWait()
            os.system('cls')
            exit()
        else:
            engine.say("Tidak ada perintah seperti itu.")
            engine.runAndWait()
    except sr.UnknownValueError:
        engine.say("Maaf, saya tidak bisa mengerti apa yang Anda katakan. Silakan coba lagi.")
        engine.runAndWait()
    except sr.RequestError:
        engine.say("Maaf, saya mengalami masalah saat mengakses layanan Google Speech Recognition.")
        engine.runAndWait()
    except Exception as ex:
        print(ex)

while True:
    user()