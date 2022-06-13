import imp
from tkinter import *
from tkinter import ttk
from turtle import left
from PIL import Image, ImageTk

co0 = "#444466"  # Preta
co1 = "#feffff"  # branca
co2 = "#6f9fbd"  # azul
co3 = "#38576b"  # valor
co4 = "#403d3d"  # letra
co5 = "#ef5350"  # vermelha

window = Tk()
window.title('')
window.geometry('550x510')
window.configure(bg=co1)

ttk.Separator(window, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(window)
style.theme_use("clam")

frame_pokemon = Frame(window, width=550, height=290, relief='flat')
frame_pokemon.grid(row=1, column=0)

poke_nome = Label(frame_pokemon, text='Misdreavus', relief='flat', anchor=CENTER, font=('Fixedsys 20'), bg=co1, fg=co0)
poke_nome.place(x=12, y=15)

poke_type = Label(frame_pokemon, text='Fantasma', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co0)
poke_type.place(x=12, y=50)

poke_id = Label(frame_pokemon, text='#200', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co0)
poke_id.place(x=12, y=75)

image_pokemon = Image.open('src/misdreavus.png')
image_pokemon = image_pokemon.resize((238,238))
image_pokemon = ImageTk.PhotoImage(image_pokemon)

pokemon_image = Label(frame_pokemon,image=image_pokemon,  relief='flat', bg=co1, fg=co0)
pokemon_image.place(x=60, y=50)

poke_type.lift()

poke_status = Label(window, text='Status', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
poke_status.place(x=15, y=310)

poke_hp = Label(window, text='HP: 60', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
poke_hp.place(x=15, y=360)

poke_atack = Label(window, text='Ataque: 60', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
poke_atack.place(x=15, y=385)

poke_defense = Label(window, text='Defesa: 60', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
poke_defense.place(x=15, y=410)

poke_speed = Label(window, text='Velocidade: 85 ', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
poke_speed.place(x=15, y=435)

poke_total = Label(window, text='Total: 265', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
poke_total.place(x=15, y=460)

poke_abilities = Label(window, text='Habilidades', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
poke_abilities.place(x=180, y=310)

poke_abilities = Label(window, text='Levitar', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
poke_abilities.place(x=195, y=360)

image_pokemon_1 = Image.open('src/misdreavusicon.png')
image_pokemon_1 = image_pokemon_1.resize((40,40))
image_pokemon_1 = ImageTk.PhotoImage(image_pokemon_1)

pokemon_button = Button(window,image=image_pokemon_1, text= 'Misdreavus', width=150, relief='raised',overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
pokemon_button.place(x=375, y=10)

image_pokemon_2 = Image.open('src/bellossomicon.png')
image_pokemon_2 = image_pokemon_2.resize((40,40))
image_pokemon_2 = ImageTk.PhotoImage(image_pokemon_2)

pokemon_button = Button(window,image=image_pokemon_2, text= 'Bellessom', width=150, relief='raised',overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
pokemon_button.place(x=375, y=65)

image_pokemon_3 = Image.open('src/dittoicon.png')
image_pokemon_3 = image_pokemon_3.resize((40,40))
image_pokemon_3 = ImageTk.PhotoImage(image_pokemon_3)

pokemon_button = Button(window,image=image_pokemon_3, text= 'Ditto', width=150, relief='raised',overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
pokemon_button.place(x=375, y=120)

image_pokemon_4 = Image.open('src/gorebyssicon.png')
image_pokemon_4 = image_pokemon_4.resize((40,40))
image_pokemon_4 = ImageTk.PhotoImage(image_pokemon_4)

pokemon_button = Button(window,image=image_pokemon_4, text= 'Gorebyss', width=150, relief='raised',overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
pokemon_button.place(x=375, y=175)

image_pokemon_5 = Image.open('src/kabutopicon.png')
image_pokemon_5 = image_pokemon_5.resize((40,40))
image_pokemon_5 = ImageTk.PhotoImage(image_pokemon_5)

pokemon_button = Button(window,image=image_pokemon_5, text= 'Kabuto', width=150, relief='raised',overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
pokemon_button.place(x=375, y=230)

image_pokemon_6 = Image.open('src/porygonicon.png')
image_pokemon_6 = image_pokemon_6.resize((40,40))
image_pokemon_6 = ImageTk.PhotoImage(image_pokemon_6)

pokemon_button = Button(window,image=image_pokemon_6, text= 'Porygon', width=150, relief='raised',overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
pokemon_button.place(x=375, y=285)



window.mainloop()
