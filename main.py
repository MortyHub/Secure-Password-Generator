import random
import string
import os
import time

lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)

Symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "[", "]", "{", "}", "\\", "|", "<", ">", ",", ".", "/", "?" ,"'", "\"", "`", "~"]

CustomSym = ["𝓮", "❥", "𝓢", "𝓲", "𝓡", "✞", "𒆩", "𝓜","꧂", "꧁", "【", "】", "☻", "●", "𒆨", "➳", "✈", "ꕤ"]

Wants = [False, False, False, False]

def start():
    password = ""
    past = ""
    if input("Upper Case Letters? (y/n) >> ") == "y":
        Wants[0] = True
    if input("LowerCase Letters? (y/n) >> ") == "y":
        Wants[1] = True
    if input("Symbols? (y/n) >> ") == "y":
        Wants[2] = True
    if input("Custom Symbols? (y/n) >> ") == "y":
        Wants[3] = True
    try:
        for i in range(int(input("How many Characters? >>"))):
            print(password)
            time.sleep(0.1)
            os.system("clear")
            
            char = random.randrange(1,4)

            if Wants[0] == True:
                if char == 1:
                    passs = random.choice(lowercase)
                    while passs == past:
                        passs = random.choice(lowercase)
                    password += passs
                    past = passs

            if Wants[1] == True:
                if char == 2:
                    passs = random.choice(uppercase)
                    while passs == past:
                        passs = random.choice(lowercase)
                    password += passs
                    past = passs

            if Wants[2] == True:
                if char == 3:
                    passs = random.choice(Symbols)
                    while passs == past:
                        passs = random.choice(Symbols)
                    password += passs
                    past = passs

            if Wants[3] == True:
                if char == 4:
                    passs = random.choice(lowercase)
                    while passs == past:
                        passs = random.choice(lowercase)
                    password += passs
                    past = passs

        print(f"Your Password Is: {password}")          

            
    except:
        print("Thats not a digit!")
        start()

start()