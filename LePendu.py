#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 08:15:18 2020

Le Pendu
@author: amaury
"""
from random import choice


fich=open('mots.txt','r')
words=[i.strip() for i in fich]
answer = choice(words)
fich.close()

lives = 8
display = ""
right_pick = ""
right_pick += answer[0]
wrong_pick = ""

for i in answer:
    if i in right_pick:
        display += i + " "
    else:
        display += "_ "

while lives > 0:
    print("Le mot à deviner est : ", display)
    n=input("Proposez une lettre : ")
    
    if n in wrong_pick:
        print("vous avez déjà proposé cette lettre")
        lives += 1
    
    if n in answer:
        right_pick += n
        print("-> Bien vu!")
    else:
        lives -= 1
        wrong_pick += n
        print("-> Nope")
        print("votre nombre de vie", lives, "\n")
    
    display = ""
    for i in answer:
        if i in right_pick:
            display += i + " "
        else:
            display += "_ "

    if "_" not in display:
        print(">>> Gagné! <<<")
        break




