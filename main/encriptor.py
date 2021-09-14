# This file contains all the python functions for the encriptor
import environ

from random import random, shuffle
import mysql.connector

env = environ.Env()
environ.Env.read_env()

MASTER_STRING_LIST = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J","K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ",", ".", "?", "!", "@", "#", "$", "%", "^", "*", "(", ")", "-", "_", "=", "+", "{", "}", "[", "]", ";", ":", "<", ">"]

USER_INPUTS = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J","K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ",", ".", "?", " ", "\n"]

used_combo_list_temp = []

def shuffle_list():
    global MASTER_STRING_LIST

    listt = MASTER_STRING_LIST
    shuffle(listt)              # shuffles original list
   
    return listt

def combo_list_for_letter(char_list):
    '''
    This function creates a unique list of unique combination of 2 char, the length of the list will be 10
    '''
    global used_combo_list_temp

    out = []

    j = int(random()*10)
    
    i = 0
    while i < 10:
        if j >= len(char_list):
                j = 0
        combo = str(i) + char_list[j]
        if combo in used_combo_list_temp:
            j += 1
            i -= 1
        else:
            used_combo_list_temp.append(combo)
            out.append(combo)
            j += 1
        i += 1

    return out


def dict_creator():

    '''
    This function creates a unique dictionary for the user, in the form of {letter1:[combo1, combo2,.....combo9]}
    '''
    global USER_INPUTS
    global used_combo_list_temp

    used_combo_list_temp = []

    shuffled_list = shuffle_list()
    out = {}
    
    for item in USER_INPUTS:
        
        out[item] = combo_list_for_letter(shuffled_list)
        
    return out

def encript(inp, dictt):
    '''
    This function replace every char of "inp" by encripted char with the help of "dictt"
    '''

    i = 0
    out = ""
    while i < len(inp):
        if len(str(i)) > 1:
            i_mod = i%10
        else:
            i_mod = i
        try:
            out += dictt[inp[i]][i_mod]
        except:
            out = f"SORRY '{inp[i]}' IS NOT ALLOWED AS A INPUT FOR ENCRIPTION"
            break
        i += 1
    return out

def decript(inp, dictt):
    '''
    This function returns the decripted string with the help of "dictt"
    '''

    out = ""
    for i in range(0, len(inp), 2):
        char = ''.join(inp[i:i+2])
        for key, val in dictt.items():
            if char in val:
                out += key
                break
    return out


def connect_db():
    db = mysql.connector.connect(
    port = "3307",
    host = "localhost",
    user = env('USER'),
    passwd = env('PASSWORD'),
    database = "textencriptor"
    )
    return db

