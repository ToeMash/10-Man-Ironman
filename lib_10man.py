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
    counter = 0

    f = open("Players/" + filename, "r")
    for x in f:
        tierDict[tiers[counter]] = x.strip().split('_')
        counter = counter + 1
    return tierDict


def gen_global(directory):
    dictOut = {}
    for f in os.listdir(directory):
        dictOut[f.split('.')[0]] = gen_personal(f)
    return dictOut

def get_tier(player, character, dic):
    for x in dic[player]:
        for y in dic[player][x]:
            if character == y:
                return x
    return None

def get_rand_char_from_tier(player, tier, dic):
    return dic[player][tier][random.randrange(0, len(dic[player][tier]), 1)]

def gen_matched_list(player1, player2, dic, p1List):
    p2List = []
    for x in p1List:
        p2List.append(get_rand_char_from_tier(player2, get_tier(player1, x, dic), dic))
    return p2List

def print_dict(dictionary):
    print(dictionary)

print_dict(gen_global("Players"))
print("\nThomas' Meta Knight rating: " + get_tier("Thomas", "Meta Knight", gen_global("Players")))
print("\nRandom character from thomas s tier: " + get_rand_char_from_tier("Thomas", "S", gen_global("Players")))
