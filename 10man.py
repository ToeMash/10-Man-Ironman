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
#    [sg.Text("Number of players", size=(30, 1)), sg.InputText()],
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
        #player_num = int(values[0])
        character_num = int(values[0])
        if values[1]:
            matched_random = True
        else:
            matched_random = False
        if character_num <= 0 or character_num > 10:    #player_num less than or equal to 0
            sys.exit("inputed values are invalid")
        print("worked")
        break
window.close()

#refresh characters
charList = []
def refresh_characters():
#event loop
    #player1
    charList = char_lineup(character_num)
    for i in range(len(charList)):
        tier_color = tiers_color_dict[get_tier(player_one, charList[i], dic)]
        imOut = "chars/" + charList[i] + ".png"
        window2["-IMG-" + str(i)].update(imOut)
        window2["-IMG-" + str(i)].ParentRowFrame.config(background = tier_color)
        window2["col1_" + str(i)].update(visible = True)
        window2["col1_" + str(i)].Widget.config(background = tier_color)
    #player2
    if matched_random:
        charList = gen_matched_list(player_one, player_two, dic, charList)
        for i in range(len(charList)):
            tier_color = tiers_color_dict[get_tier(player_two, charList[i], dic)]
            imOut = "chars/" + charList[i] + ".png"
            window2["-IMG2-" + str(i)].update(imOut)
            window2["-IMG2-" + str(i)].ParentRowFrame.config(background = tier_color)
            window2["col2_" + str(i)].update(visible = True)
            window2["col2_" + str(i)].Widget.config(background = tier_color)
    else:
        charList = char_lineup(character_num)
        for i in range(len(charList)):
            filler = get_tier(player_two, charList[i], dic)
            tier_color = tiers_color_dict[filler]
            imOut = "chars/" + charList[i] + ".png"
            window2["-IMG2-" + str(i)].update(imOut)
            window2["-IMG2-" + str(i)].ParentRowFrame.config(background = tier_color)
            window2["col2_" + str(i)].update(visible = True)
            window2["col2_" + str(i)].Widget.config(background = tier_color)

#setup layout for window 2
col1_s = [
    [sg.Frame('', [[sg.Image(key="-IMG-"+str(i))]], background_color = "grey",
    visible = False, key = "col1_"+str(i)), 
    sg.Frame('', [[sg.Image(key="-IMG-"+str(i+1))]], background_color = "grey",
    visible = False, key = "col1_"+str(i+1))] for i in range(0,10,2)
]

col1=[
    [sg.Text('Player 1', background_color='black', font = ["Ariel", 50])],
    [sg.Column(col1_s, element_justification='c')]
]

col2_s = [
    [sg.Frame('', [[sg.Image(key="-IMG2-"+str(i))]], background_color = "grey",
    visible = False, key = "col2_"+str(i)), 
    sg.Frame('', [[sg.Image(key="-IMG2-"+str(i+1))]], background_color = "grey",
    visible = False, key = "col2_"+str(i+1))] for i in range(0,10,2)
]

col2=[
    [sg.Text('Player 2', background_color="black", font = ["Ariel", 50])],
    [sg.Column(col2_s, element_justification='c')]
]

layout2 = [
    [sg.Column(col1, element_justification='c'),
    sg.VSeparator(),
    sg.Column(col2, element_justification='c')],
    [sg.Button("Close"), sg.Button("Retry")]
]

#show produced characters

window2 = sg.Window("The Ironman", layout2, margins, location = (400,0))

while True:
    event, values = window2.read()
    if event == "Close" or event == sg.WIN_CLOSED:
        break
    elif event == "Retry":
        refresh_characters()
        window2.refresh()
window2.close()
