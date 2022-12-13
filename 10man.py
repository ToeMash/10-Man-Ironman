import PySimpleGUI as sg
import time
from lib_10man import char_lineup
from PIL import Image
import os


sz = 0
 
col1=[[sg.Text('Player 1', background_color='black', size=sz)],
      [[sg.Image(imOut),] for i in range(sz)]]
col2=[[sg.Text('Player 2', background_color="black", size=sz)],
      [[sg.Image(imOut),] for i in range(sz)]]

layout = [
    [sg.Text("Number of players", size=(30, 1)), sg.InputText()],
    [sg.Text("Number of characters", size=(30, 1)), sg.InputText()],
    [sg.Column(col1, key='-IMAGEOUT-')],
    [sg.Column(col2, key='-IMAGEOUT-')],
    [sg.Image("chars/Mario.png")],
    [sg.Button("Start")],
    [sg.Button("Close")]
]

margins = (10, 10)

window = sg.Window("10 Man Iron Man", layout, margins)

charList = []

# event loop
while True:
    event, values = window.read()
    if event == "Close" or event == sg.WIN_CLOSED:
        break
    elif event == "Start":
        sz = int(values[1])
        for x in range(int(values[0])):
            charList.append(char_lineup(sz))
        for x in range(int(values[0])):
            for y in range(sz):
                imOut = "chars/" + charList[x][y] + ".png"
                window.Element("-IMAGEOUT-").update(imOut)
        window.refresh()
window.close()
