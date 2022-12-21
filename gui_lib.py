import PySimpleGUI as sg
import time
from lib_10man import list_of_characters, list_to_tier, tiers_color_dict
from PIL import Image
import os
import sys


def open_tierMaker(name):
    col = [
    [sg.Button(key="img"+str(i*10+0), button_color = "gold",
    image_filename = "charsl/"+list_of_characters[i*10+0]+".png"),
    sg.Button(key="img"+str(i*10+1), button_color = "gold",
    image_filename = "charsl/"+list_of_characters[i*10+1]+".png"),
    sg.Button(key="img"+str(i*10+2), button_color = "gold",
    image_filename = "charsl/"+list_of_characters[i*10+2]+".png"),
    sg.Button(key="img"+str(i*10+3), button_color = "gold",
    image_filename = "charsl/"+list_of_characters[i*10+3]+".png"),
    sg.Button(key="img"+str(i*10+4), button_color = "gold",
    image_filename = "charsl/"+list_of_characters[i*10+4]+".png"),
    sg.Button(key="img"+str(i*10+5), button_color = "gold",
    image_filename = "charsl/"+list_of_characters[i*10+5]+".png"),
    sg.Button(key="img"+str(i*10+6), button_color = "gold",
    image_filename = "charsl/"+list_of_characters[i*10+6]+".png"),
    sg.Button(key="img"+str(i*10+7), button_color = "gold",
    image_filename = "charsl/"+list_of_characters[i*10+7]+".png"),
    sg.Button(key="img"+str(i*10+8), button_color = "gold",
    image_filename = "charsl/"+list_of_characters[i*10+8]+".png"),
    sg.Button(key="img"+str(i*10+9), button_color = "gold",
    image_filename = "charsl/"+list_of_characters[i*10+9]+".png")]
    for i in range(0,8)
    ]
    layout = [
        [sg.Text("S tiers:", key = "txt_tier", font = ["Ariel", 11]),
        sg.Text("0", key = "charin_tier", font = ["Ariel", 11])],
        [sg.Text("Aim for 14 characters each tier", font = ["Ariel", 11])],
        [sg.Text("86 characters", key = "txt_num_char", font = ["Ariel", 11])],

        [sg.Column(col, key = "col", pad = 0)],
        [sg.Button(key="img80", button_color = "gold",
        image_filename = "charsl/"+list_of_characters[80]+".png"),
        sg.Button(key="img81", button_color = "gold",
        image_filename = "charsl/"+list_of_characters[81]+".png"),
        sg.Button(key="img82", button_color = "gold",
        image_filename = "charsl/"+list_of_characters[82]+".png"),
        sg.Button(key="img83", button_color = "gold",
        image_filename = "charsl/"+list_of_characters[83]+".png"),
        sg.Button(key="img84", button_color = "gold",
        image_filename = "charsl/"+list_of_characters[84]+".png"),
        sg.Button(key="img85", button_color = "gold",
        image_filename = "charsl/"+list_of_characters[85]+".png")],

        [sg.Button("Submit")],
        [sg.Button("Close")]
    ]

    margins = (1,1)
    window = sg.Window("test window", layout, margins, element_justification = 'c')
    new_file = open("Players/" + name + ".txt", "w")
    saw = []
    lst_saw = []
    but_tons = []
    tiers = ['S','A','B','C','D','F']
    line = 0
    num_chars = 86
    karen_tier = 0
    over15 = 0
    over16 = 0
    for i in range(86):
        but_tons.append("img"+str(i))
    while True:
        event, values = window.read()
        if event == "Close" or event == sg.WIN_CLOSED:
            new_file.close()
            os.remove("Players/"+name+".txt")
            break
        elif event in but_tons:
            if event in saw:
                window[event].update(button_color = "gold")
                num_chars += 1
                karen_tier -= 1
                saw.remove(event)
            else:
                window[event].update(button_color = "grey")
                num_chars -= 1
                karen_tier += 1
                saw.append(event)
        elif ((over15 == 1 and len(saw) > 15) or over15 == 2 or over16 == 1) and event == "Submit" and len(saw) > 14:
            print("too many characters")
        elif event == "Submit" and len(saw) >= 14:
            #write the current tier to new_file
            if len(saw) > 16:
                print("too many characters")
                continue
            elif len(saw) == 15:
                over15 += 1
            elif len(saw) == 16:
                over16 += 1
            print("over15:"+str(over15))
            print("over16:"+str(over16))

            for s in saw:
                window[s].update(disabled = True)
                lst_saw.append(list_of_characters[int(s[3:])])
            string = list_to_tier(lst_saw)
            new_file.write(string)
            if line == 5:
                #find a way to make tier after all the saw and tiers are made
                new_file.close()
                break
            line += 1
            window["txt_tier"].update(tiers[line]+" tiers")
            karen_tier = 0
            saw.clear()
            lst_saw.clear()
        window["txt_num_char"].update(str(num_chars)+" characters:")
        window["charin_tier"].update(str(karen_tier))

    window.close()
