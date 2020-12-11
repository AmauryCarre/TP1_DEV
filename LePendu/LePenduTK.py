#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 08:32:04 2020
problème = pas le temps de régler le problème de texte sur la fenetre tk

attention si vous avez une erreur de type "right_pick += answer[0]" lancé la version non tk et revenez à celle là

@author: amaury
"""
from random import choice

def getanswer(): #récupère un nouveau mot
    fich=open('mots.txt','r')
    words=[]
    for i in fich:
        words.append(i.strip())
    answer = choice(words)
    fich.close()
    return answer
#______necessaire-------
answer=getanswer()
print(answer)  #pour les test
right_pick =""
right_pick += answer[0]

wrong_pick =""
lives=8
#-----------------------

def getdisplay(answer,right_pick): #affiche le mot à trouver
    display = ""
    for i in answer:
        if i in right_pick:
            display += i + " "
        else:
            display += "_ "
    return display

display = getdisplay(answer,right_pick) 


#-----------------------------------------

def MajDuDisplay():          #met à jour la fenetre après chaque clique sur le boutton valider
    n=Champ.get()
    Champ.delete(0,'end')
    
    global right_pick , answer , wrong_pick
    lives = get_lives()
    right_pick += get_right_pick()
    wrong_pick += get_wrong_pick()
    
    if n in wrong_pick:
            proposed=Label(text="vous avez déjà proposé cette lettre")
            proposed.pack(side='top')
            lives += 0
        
    if n in answer:
            right_pick += n
            trouver=Label(text="-> Bien vu!")
            trouver.pack(side='top')
    if n not in answer and n not in wrong_pick:
            lives -= 1
            if lives == 0:
                MyWindow.destroy()
            wrong_pick += n
            nomPhoto = "image/bonhomme"+str(lives)+".gif"
            photo=PhotoImage(file=nomPhoto)
            image_pendu.configure(image=photo)
            image_pendu.image = photo
            VieRestante=Label(MyWindow, text=("votre nombre de vie restante:",lives))
            VieRestante.pack(side='top',padx=5,pady=5)
            return photo
    
    display2 = getdisplay(answer,right_pick)
    MotEnCour.configure(text=display2)
    
    mot = MotEnCour['text']
    if "_" not in mot:
            print (">>>Gagné!<<<")
            MyWindow.after(1500)
            MyWindow.destroy()
    

def get_right_pick():   #lettres correctes
    global answer
    right_pick=""
    right_pick += answer[0]
    n=Champ.get()
    if n in answer:
        right_pick += n
    return right_pick

def get_wrong_pick():   #lettres fausses
    global answer
    wrong_pick=""
    n=Champ.get()
    if n not in answer:
        wrong_pick += n
    return wrong_pick
    
def get_lives():        #décompte des vies 
    lives=8
    lives-=len(wrong_pick)
    return lives
    
    
#-----------------------------TKinter----------------------------
from tkinter import Tk, Label, StringVar, Entry, Button, Canvas, PhotoImage, Frame

MyWindow=Tk()
MyWindow.title('Le Jeu du Pendu')

zone2 = Frame(MyWindow)
zone2.pack(side='bottom',padx=5,pady=5)

canevas = Canvas(MyWindow, bg='white', height=300, width=320)
canevas.pack(side='top')

Proposition= StringVar()
Champ=Entry(zone2, textvariable = Proposition, bg='light sky blue')
Champ.pack(side='bottom',padx=5,pady=5)

MotEnCour=Label(MyWindow, text=display)
MotEnCour.pack(side='left',padx=10,pady=10)
VotreLettre=Label(zone2, text="Proposez une lettre :")
VotreLettre.pack(side='left',padx=5,pady=5)

boutonVal=Button(zone2, text ='Valider', command=MajDuDisplay)
boutonVal.pack(side='bottom', padx=5, pady=5)

boutonQuit=Button(MyWindow, text ='Abandonner', command=MyWindow.destroy)
boutonQuit.pack(side='right', padx=5, pady=5)

photo=PhotoImage(file="image/bonhomme8.gif")
image_pendu = Label(canevas, image=photo, border=0)
image_pendu.pack()

MyWindow.mainloop()
MyWindow.destroy()



