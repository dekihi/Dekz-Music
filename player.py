from tkinter import*

#importar imagens

from PIL import Image, ImageTk

#import pygame
import pygame
from pygame import mixer

import os

#cores
cor0 = "#0a0b0c" #cinza
cor1 = "#fefffd" #branco
cor2 = "#391740" #roxo
cor3 = "#000000" #prto
cor4 = "#0b0a17" #preto azulado
cor5 = "#6e0119" #vinho

#janela

janela = Tk ()
janela.title ("Dekz Music")
janela.geometry('352x255')
janela.configure(background=cor4)
janela.resizable(width=FALSE, height=FALSE)

#frames

frame_esquerda = Frame(janela,width=150 ,height=150,bg=cor0)
frame_esquerda.grid(row=0,column=0,pady=1,padx=1,sticky=NSEW)

frame_direita = Frame(janela,width=250 ,height=150,bg=cor0)
frame_direita.grid(row=0,column=1,pady=1,padx=0,sticky=NSEW)

frame_baixo = Frame(janela,width=150 ,height=150,bg=cor0)
frame_baixo.grid(row=1,column=0,columnspan=3,pady=1,padx=0,sticky=NSEW)

#frame esquerda

img_1 = Image.open('iconPrincipal.png')
img_1 = img_1.resize((130,130))
img_1 = ImageTk.PhotoImage(img_1)

l_logo = Label(frame_esquerda, height=130, image=img_1, compound=LEFT, padx=0,anchor='nw',font=('ivy 16 bold'), bg=cor0, fg=cor1)
l_logo.place(x=5, y=15)

#function
def play_musica():
    play = listbox.get(ACTIVE)
    l_play['text'] = play
    mixer.music.load(play)
    mixer.music.play()
    
#pause
def pause_musica():
    mixer.music.pause()
    
#continuar
def continue_musica():
    mixer.music.unpause()
    
#parar
def parar_musica():
    mixer.music.stop()
    
#avancar
def avancar_musica():
    tocando = l_play['text']
    index = musicas.index(tocando)
    novo_index = index + 1
    tocando = musicas[novo_index]
    mixer.music.load(tocando)
    mixer.music.play()
    
    #delet element
    listbox.delete(0,END)
    
    mostrar()
    
    listbox.select_set(novo_index)
    listbox.config(selectmode=SINGLE)
    l_play['text'] = tocando
    
#retornar

def retornar_musica():
    tocando = l_play['text']
    index = musicas.index(tocando)
    novo_index = index - 1
    tocando = musicas[novo_index]
    mixer.music.load(tocando)
    mixer.music.play()
    
    #delet element
    listbox.delete(0,END)
    
    mostrar()
    
    listbox.select_set(novo_index)
    listbox.config(selectmode=SINGLE)
    l_play['text'] = tocando



#frame direita

lista = ['a','b','c']

listbox = Listbox (frame_direita,width=22,height=10, selectmode=SINGLE,font=('arial 9 bold'), bg=cor0, fg=cor1)
listbox.grid(row=0,column=0)

s = Scrollbar(frame_direita)
s.grid(row=0,column=1, sticky=NSEW)

listbox.config(yscrollcommand=s.set)
s.config(command=listbox.yview)

#frame baixo

l_play = Label(frame_baixo,text='Escolha a musica da lista', width=44, justify=LEFT,anchor='nw',font=('ivy 10'), bg=cor1, fg=cor5)
l_play.place(x=0, y=1)

#button

img_2 = Image.open('retornar.png')
img_2 = img_2.resize((30,30))
img_2 = ImageTk.PhotoImage(img_2)

b_voltar = Button(frame_baixo, width=40,command=retornar_musica,height=40,image=img_2, font=('ivy 10'),relief=RAISED, overrelief=RIDGE, bg=cor3, fg=cor5)
b_voltar.place(x=35, y=35)

img_3 = Image.open('play.png')
img_3 = img_3.resize((30,30))
img_3 = ImageTk.PhotoImage(img_3)

b_play = Button(frame_baixo, width=40,command=play_musica,height=40,image=img_3, font=('ivy 10'),relief=RAISED, overrelief=RIDGE, bg=cor3, fg=cor5)
b_play.place(x=82, y=35)

img_4 = Image.open('avancar.png')
img_4 = img_4.resize((30,30))
img_4 = ImageTk.PhotoImage(img_4)

b_avancar = Button(frame_baixo, command=avancar_musica, width=40,height=40,image=img_4, font=('ivy 10'),relief=RAISED, overrelief=RIDGE, bg=cor3, fg=cor5)
b_avancar.place(x=130, y=35)

img_5 = Image.open('iconPause.png')
img_5 = img_5.resize((30,30))
img_5 = ImageTk.PhotoImage(img_5)

b_pause= Button(frame_baixo, command=pause_musica,width=40,height=40,image=img_5, font=('ivy 10'),relief=RAISED, overrelief=RIDGE, bg=cor3, fg=cor5)
b_pause.place(x=178, y=35)

img_6 = Image.open('continuar.png')
img_6 = img_6.resize((30,30))
img_6 = ImageTk.PhotoImage(img_6)

b_continuar = Button(frame_baixo,command=continue_musica, width=40,height=40,image=img_6, font=('ivy 10'),relief=RAISED, overrelief=RIDGE, bg=cor3, fg=cor5)
b_continuar.place(x=225, y=35)


img_7 = Image.open('parar.png')
img_7 = img_7.resize((30,30))
img_7 = ImageTk.PhotoImage(img_7)

b_parar = Button(frame_baixo,command=parar_musica, width=40,height=40,image=img_7, font=('ivy 10'),relief=RAISED, overrelief=RIDGE, bg=cor3, fg=cor5)
b_parar.place(x=272, y=35)


os.chdir(r'C:\Users\Pichau\Desktop\Music')
musicas = os.listdir()

def mostrar():
    for i in musicas:
        listbox.insert(END,i)
        
mostrar()



#iniciar
mixer.init()

janela.mainloop()