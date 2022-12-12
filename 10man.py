import PySimpleGUI as sg
import pyautogui
import time
import 10manlibrary
from PIL import Image
import os

folder = 
imageList = [f for f in folder]

for i in 
col1=[[sg.Text('Player 1')],
      [sg.Image(imOut)]]
col2=[[sg.Text('Player 2')],
      [sg.Image(imOut)]]

layout = [
    [sg.Text("Number of players", size=(30, 1)), sg.InputText()],
    [sg.Text("Number of characters", size=(30, 1)), sg.InputText()],
    [sg.Column(col1, size=sz)],
    [sg.Column(col2, size=sz)],
    [sg.Button("Start")],
    [sg.Button("Close")]
]

margins = (10, 10)

window = sg.Window("10 Man Iron Man", layout, margins)

charList = 10manlibrary.list_of_characters

# event loop
while True:
    event, values = window.read()
    if event == "Close" or event == sg.WIN_CLOSED:
        break
    elif event == "Start":
        sz = values[1]
        for x in range(values[0]):
            charArray[x] = 10manlibrary.pc(sz)
        for x in range(values[0]):
            for y in range(sz):
                image = Image.open(charArray[x][y])
                window["10 Man Iron Man"].update(
window.close()
