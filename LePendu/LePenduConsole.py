#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 08:15:18 2020

Le Pendu

to do:
    fonction
    best score
    
@author: amaury
"""
from random import choice

def getanswer():                      #récupère un nouveau mot
    fich=open('mots.txt','r')
    words=[]
    for i in fich:
        words.append(i.strip())
    answer = choice(words)
    fich.close()
    return answer

answer=getanswer()
print(answer)  #pour les test

lives = 8
right_pick = ""
right_pick += answer[0]
wrong_pick = ""

def getdisplay(answer,right_pick):   #affiche le mot à trouver
    display = ""
    for i in answer:
        if i in right_pick:
            display += i + " "
        else:
            display += "_ "
    return display

display = getdisplay(answer,right_pick)   

def Pendu(lives,right_pick,wrong_pick,answer,display):    # réalise le pendu mais pas propre
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
        
        display = getdisplay(answer,right_pick)
        
        if "_" not in display:
            print(">>> Gagné! <<<")
            break
    #la partie de dessous représente le choix de rejouer (pas propre)
    answer=getanswer()
    print(answer)  #pour les test
    lives = 8
    right_pick = ""
    right_pick += answer[0]
    wrong_pick = ""
    display = getdisplay(answer,right_pick)
    
    r=input("veux tu rejouer? oui ou non? ")
    if r=="oui":
        Pendu(lives,right_pick,wrong_pick,answer,display)
    elif r=="non":
        print("Dommage")
        

Pendu(lives,right_pick,wrong_pick,answer,display)










