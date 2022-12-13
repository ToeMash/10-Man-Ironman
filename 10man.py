import PySimpleGUI as sg
import time
from lib_10man import char_lineup
from PIL import Image
import os
import sys

#theme
sg.theme('DarkAmber')

#player_num = 0      #number of players
character_num = 0   #number of characters

layout = [
#    [sg.Text("Number of players", size=(30, 1)), sg.InputText()],
    [sg.Text("Number of characters", size=(30, 1)), sg.InputText()],
    [sg.Button("Start")],
    [sg.Button("Close")]
]

margins = (10, 10)

window = sg.Window("10 Man Iron Man", layout, margins)

#gather information
#event loop
while True:
    event, values = window.read()
    if event == "Close" or event == sg.WIN_CLOSED:
        sys.exit("program exited")
    elif event == "Start":
        #get the values
        #player_num = int(values[0])
        character_num = int(values[0])
        if character_num <= 0 or character_num > 10:    #player_num <= 0
            sys.exit("inputed values are invalid")
        print("worked")
        break
window.close()

#show produced characters

col1=[
    [sg.Text('Player 1', background_color='black', size=0)],
    [sg.Image(key="-IMG-0")],
    [sg.Image(key="-IMG-1")],
    [sg.Image(key="-IMG-2")],
    [sg.Image(key="-IMG-3")],
    [sg.Image(key="-IMG-4")],
    [sg.Image(key="-IMG-5")],
    [sg.Image(key="-IMG-6")],
    [sg.Image(key="-IMG-7")],
    [sg.Image(key="-IMG-8")],
    [sg.Image(key="-IMG-9")]
]
col2=[
    [sg.Text('Player 2', background_color="black", size=0)],
    [sg.Image(key="-IMG2-0")],
    [sg.Image(key="-IMG2-1")],
    [sg.Image(key="-IMG2-2")],
    [sg.Image(key="-IMG2-3")],
    [sg.Image(key="-IMG2-4")],
    [sg.Image(key="-IMG2-5")],
    [sg.Image(key="-IMG2-6")],
    [sg.Image(key="-IMG2-7")],
    [sg.Image(key="-IMG2-8")],
    [sg.Image(key="-IMG2-9")]
]

layout2 = [
    [sg.Column(col1, element_justification='c'),
    sg.Column(col2, element_justification='c')],
    [sg.Button("Close")]
]

window2 = sg.Window("The Ironman", layout2, margins)
window2.read()

charList = []

#player1
charList = char_lineup(character_num)
for i in range(len(charList)):
    imOut = "chars/" + charList[i] + ".png"
    window2["-IMG-" + str(i)].update(imOut)
    window2.refresh()

#player2
charList = char_lineup(character_num)
for i in range(len(charList)):
    imOut = "chars/" + charList[i] + ".png"
    window2["-IMG2-" + str(i)].update(imOut)
    window2.refresh()

while True:
    event, values = window2.read()
    if event == "Close" or event == sg.WIN_CLOSED:
        break
window2.close()
