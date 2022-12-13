import random
import os

#list of ssbu characters
list_of_characters = ['Mario', 'Donkey Kong', 'Link', 'Samus', 'Dark Samus', 'Yoshi', 'Kirby', 'Fox', 'Pikachu', 'Luigi', 'Ness', 'Captain Falcon', 'Jigglypuff', 'Peach', 'Daisy', 'Bowser', 'Ice Climbers', 'Sheik', 'Zelda', 'Dr. Mario', 'Pichu', 'Falco', 'Marth', 'Lucina', 'Young Link', 'Ganondorf', 'Mewtwo', 'Roy', 'Chrom', 'Mr. Game & Watch', 'Meta Knight', 'Pit', 'Dark Pit', 'Zero Suit Samus', 'Wario', 'Snake', 'Ike', 'Pokemon Trainer', 'Diddy Kong', 'Lucas', 'Sonic', 'King Dedede', 'Olimar', 'Lucario', 'R.O.B.', 'Toon Link', 'Wolf', 'Villager', 'Mega Man', 'Wii Fit Trainer', 'Rosalina & Luma', 'Little Mac', 'Greninja', 'Mii Brawler', 'Mii Swordfighter', 'Mii Gunner', 'Palutena', 'Pac-man', 'Robin', 'Shulk', 'Bowser Jr.', 'Duck Hunt', 'Ryu', 'Ken', 'Cloud', 'Corrin', 'Bayonetta', 'Inkling', 'Ridley', 'Simon', 'Richter', 'King K. Rool', 'Isabelle', 'Incineroar', 'Piranha Plant', 'Joker', 'Hero', 'Banjo & Kazooie', 'Terry', 'Byleth', 'Min Min', 'Steve', 'Sephiroth', 'Pyra-Mythra', 'Kazuya', 'Sora']

#returns list of characters for a player
def char_lineup(num_characters):
    #player's characters
    lineup = []

    #seed
    random.seed()

    #build list
    loc = list_of_characters.copy()
    for i in range(num_characters):
        chosen_character = random.randrange(0, len(loc))
        name = loc[chosen_character]
        loc.remove(name)
        lineup.append(name)

    return lineup

def gen_personal(filename):
    tierDict = {}
    tiers = ['S', 'A', 'B', 'C', 'D', 'F']

    f = open(filename, "r")
    for x in f:
        tierDict[tiers[int(x)]] = x.split('_')
    return tierDict


def gen_global(directory):
    dictOut = {}
    for f in os.listdir(directory):
        dictOut[f.split('.')[0]] = gen_personal(f)
    return dictOut

def print_dict(dictionary):
    print(dictionary)

