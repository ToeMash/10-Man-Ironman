import PySimpleGUI as sg
import time
from lib_10man import char_lineup, gen_global, gen_matched_list, get_tier, tiers_color_dict
from PIL import Image
import os
import sys

#theme
sg.theme('DarkAmber')

#player_num = 0      #number of players
character_num = 0   #number of characters
matched_random = True

layout = [
##    [sg.Text("Number of players", size=(30, 1)), sg.InputText()],
    [sg.Text("Number of characters", size=(30, 1)), sg.InputText()],
    [sg.Checkbox("Matched random", default=True)],
    [sg.Button("Start")],
    [sg.Button("Close")]
]

margins = (10, 10)
dic = gen_global("Players")
player_one = "Brendan"        #defualt tier list
player_two = "Thomas"         #default tier list
tier_color = "grey"

window = sg.Window("10 Man Iron Man", layout, margins)

#gather information
while True:
    event, values = window.read()
    if event == "Close" or event == sg.WIN_CLOSED:
        sys.exit("program exited")
    elif event == "Start":
        #get the values
        ##player_num = int(values[0])
        character_num = int(values[0])
        if values[1]:
            matched_random = True
        else:
            matched_random = False
        if character_num <= 0 or character_num > 10:    #player_num less than or equal to 0
            sys.exit("inputed values are invalid")
        ##print("worked")
        break
window.close()

seen = {}
saw = []

#refresh characters
charList = []
def refresh_characters():
    saw.clear()
    #player1
    charList = char_lineup(character_num)
    for i in range(len(charList)):
        tier_color = tiers_color_dict[get_tier(player_one, charList[i], dic)]
        imOut = "chars/" + charList[i] + ".png"
        #img = img_base64(imOut)
        window2["-IMG1-" + str(i)].update(image_filename = imOut)
        window2["-IMG1-" + str(i)].update(button_color = tier_color)
        window2["-IMG1-" + str(i)].ParentRowFrame.config(background = "grey")
        window2["f-IMG1-" + str(i)].update(visible = True)
        window2["f-IMG1-"+str(i)].Widget.config(background = "gold")
        seen["-IMG1-"+str(i)] = tier_color
    #player2
    if matched_random:
        charList = gen_matched_list(player_one, player_two, dic, charList)
    else:
        charList = char_lineup(character_num)

    for i in range(len(charList)):
        tier_color = tiers_color_dict[get_tier(player_two, charList[i], dic)]
        imOut = "chars/" + charList[i] + ".png"
        #img = img_base64(imOut)
        window2["-IMG2-" + str(i)].update(image_filename = imOut),
        window2["-IMG2-" + str(i)].update(button_color = tier_color)
        window2["-IMG2-" + str(i)].ParentRowFrame.config(background = "grey")
        window2["f-IMG2-" + str(i)].update(visible = True)
        window2["f-IMG2-"+str(i)].Widget.config(background = "gold")
        seen["-IMG2-"+str(i)] = tier_color

#setup layout for window 2
col1_s = [
    [sg.Frame('', [[sg.Button(key="-IMG1-"+str(i))]],
    background_color = "gold", visible = False, key="f-IMG1-"+str(i)),
    sg.Frame('', [[sg.Button(key="-IMG1-"+str(i+1))]],
    background_color = "gold", visible = False, key="f-IMG1-"+str(i+1))] for i in range(0,10,2)
]

col2_s = [
    [sg.Frame('', [[sg.Button(key="-IMG2-"+str(i))]],
    background_color = "gold", visible = False, key="f-IMG2-"+str(i)),
    sg.Frame('', [[sg.Button(key="-IMG2-"+str(i+1))]],
    background_color = "gold", visible = False, key="f-IMG2-"+str(i+1))] for i in range(0,10,2)
]

col1=[
    [sg.Text('Player 1', background_color='black', font = ["Ariel", 30])],
    [sg.Column(col1_s, element_justification='c')]
]

col2=[
    [sg.Text('Player 2', background_color="black", font = ["Ariel", 30])],
    [sg.Column(col2_s, element_justification='c')]
]

layout2 = [
    [sg.Column(col1, element_justification='l'),
    sg.VSeparator(p=(30,0)),
    sg.Column(col2, element_justification='r')],
    [sg.Button("Close"), sg.Button("Retry")]
]

#show produced characters

window2 = sg.Window("The Ironman", layout2, margins, location = (400,0), element_justification = 'c', element_padding = 1)

but_ton = []
for i in range(1,3,1):
    for j in range(10):
        but_ton.append("-IMG"+str(i)+"-"+str(j))

while True:
    event, values = window2.read()
    print(event)
    if event == "Close" or event == sg.WIN_CLOSED:
        break
    elif event == "Retry":
        refresh_characters()
        window2.refresh()
    elif event in but_ton:
        print("event found in but_ton")
        if event in saw:
            tier_color = seen[event]
            window2[event].update(button_color = tier_color)
            window2["f"+event].Widget.config(background = "gold")
            saw.remove(event)
            print(saw)
        else:
            window2[event].update(button_color = "grey")
            #window2[event].ParentRowFrame.config(background = "grey")
            window2["f"+event].Widget.config(background = "grey")
            saw.append(event)
            print(saw)
window2.close()
