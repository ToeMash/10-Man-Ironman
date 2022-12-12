import PySimpleGUI as sg
import pyautogui
import time

layout = [
    [sg.Text("Number of players", size=(30, 1)), sg.InputText()],
    [sg.Text("Number of characters", size=(30, 1)), sg.InputText()],
    [sg.Button("Start")],
    [sg.Button("Close")]
]

margins = (10, 10)

window = sg.Window("10 Man Iron Man", layout, margins)

# event loop
while True:
    event, values = window.read()
    if event == "Close" or event == sg.WIN_CLOSED:
        break
    elif event == "Start":
        print("deez")
window.close()