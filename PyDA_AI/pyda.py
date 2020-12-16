#pip install wikipedia
#pip install wolframalpha --> answer engine usually used for mathematical calculation 
#pip install -U wxPython --> to setup GUI

'''
python code to access Wolframalpha
(register and get AppID)
https://account.wolfram.com/login/oauth2/sign-in
https://developer.wolframalpha.com/portal/myapps/
'''

import PySimpleGUI as sg
import wolframalpha
import wikipedia
import pyttsx3


client = wolframalpha.Client("AHP64J-L6XUYL5HUR") #AppID Deactived Hence no peeking! :P

sg.theme('DarkPurple')
# Define the window's contents
layout = [  [sg.Text("Enter a command : ")],     # Each list is a horizontal reference in UI
            [sg.Input()],
            [sg.Button('Ok'),sg.Button('Cancel')] ] #to show buttons on single level horizontally

# Create the window
window = sg.Window('PyDa', layout)      # Window Defintion

# Display and interact with the Window
while True :
    event, values = window.read()    # Event loop or Window.read call
    if event in (None, 'Cancel'):
        break
    res = client.query(values[0])

    print('YOUR TEXT : ', values[0]) 
    engine = pyttsx3.init()
    try : 
        wiki_res = wikipedia.summary(values[0]) #faster and detailed response 
        wolfram_res = next(res.results).text
        #text to speech
        engine.say(wiki_res)
        engine.say(wolfram_res)    
        sg.PopupNonBlocking('WOLFRAM RESULT : '+wiki_res +'\n\nWIKIPEDIA RESULT :'+wolfram_res) #PopupNonBlocking allow to read text and show parallely 
    except wikipedia.exceptions.DisambiguationError:
        wolfram_res = next(res.results).text
        engine.say(wolfram_res)    
        sg.PopupNonBlocking('WIKIPEDIA RESULT :'+wolfram_res)
    except wikipedia.exceptions.PageError:
        wolfram_res = next(res.results).text
        engine.say(wolfram_res)    
        sg.PopupNonBlocking('WIKIPEDIA RESULT :'+wolfram_res)
    except:
        wiki_res = wikipedia.summary(values[0])
        engine.say(wiki_res)    
        sg.PopupNonBlocking('WIKIPEDIA RESULT :'+wiki_res)

    #sg.Popup('WOLFRAM RESULT : '+wiki_res +'\n\nWIKIPEDIA RESULT :'+wolfram_res)
    engine.runAndWait()
    
# Finish up by removing from the screen
window.close()