import pyttsx3 #pip install pyttsx3 , to convert text to speech, also works offline unlike gTTS
engine = pyttsx3.init()
engine.say('This is JARVIS, How can i help you ?')
engine.runAndWait()

#TODO explore pyttsx3 and why it needs a engine to run 