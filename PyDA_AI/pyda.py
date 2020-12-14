#pip install wikipedia
#pip install wolframalpha --> answer engine usually used for mathematical calculation 
#pip install -U wxPython --> to setup GUI

'''
python code to access Wolframalpha
(register and get AppID)
https://account.wolfram.com/login/oauth2/sign-in
https://developer.wolframalpha.com/portal/myapps/
'''
'''
import wolframalpha
client = wolframalpha.Client("AHP64J-L6XUYL5HUR")#AppID Deactived 
res = client.query('how many continents in world')
print(next(res.results).text)
'''
import PySimpleGUI as sg

sg.theme('DarkPurple')
# Define the window's contents
layout = [  [sg.Text("What's your name?")],     # Part 2 - The Layout
            [sg.Input()],
            [sg.Button('Ok')] ]

# Create the window
window = sg.Window('Window Title', layout)      # Part 3 - Window Defintion


# Display and interact with the Window
while True :
    event, values = window.read()                   # Part 4 - Event loop or Window.read call
    if event in (None, 'Cancel'):
        break
    # Do something with the information gathered
    print('YOUR TEXT : ', values[0])

# Finish up by removing from the screen
window.close()