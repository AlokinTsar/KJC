from tkinter import *
from tkinter import ttk  
from tkinter.ttk import Notebook

import pandas as pd

import random
import time

romaji_data = pd.read_excel(r'A:\KJC\kanji_list.xlsx')
romaji_xlsx = pd.DataFrame(romaji_data, columns= ['RU DEF'])
romaji_list = romaji_xlsx['RU DEF'].values.tolist()

kanji_data = pd.read_excel(r'A:\KJC\kanji_list.xlsx')
kanji_xlsx = pd.DataFrame(romaji_data, columns= ['KANJI DEF'])
kanji_list = kanji_xlsx['KANJI DEF'].values.tolist()

kana_data = pd.read_excel(r'A:\KJC\kanji_list.xlsx')
kana_xlsx = pd.DataFrame(kana_data, columns= ['KANA DEF'])
kana_list = kana_xlsx['KANA DEF'].values.tolist()

#---------------------------------WINDOW-AND-FRAMES---------------------------------

window = Tk()
window.title("KJC Trainer | Лучшее Приложение для Изучения Кандзи!")
window.geometry('650x310')  

kanji_window=Frame(window,bg="#1F1F1F",bd=5)
kanji_window.pack(fill="both")

hiragana_window=Frame(window,bg="#1F1F1F",bd=5)
hiragana_window.pack(fill="both")

#---------------------------------FUNCTIONS---------------------------------

def next_kanji():
	global last_random_index

	random_index = random.randint(0, len(kanji_list) - 1)
	newest_symbol = kanji_list[random_index]
	newest_kana = kana_list[random_index]
	symbol.config(text = newest_symbol)
	kana.config(text = newest_kana)
	last_random_index = random_index

def show_answer():
	answer.configure(text=romaji_list[last_random_index])

def clear_answer():
	answer.configure(text="...")

#---------------------------------KANJI-FRAME---------------------------------
	
symbol = Label(kanji_window, text="", bg="#1F1F1F", fg="white", font=("YasashisaGothicBold-V2", 50))
symbol.pack(side="top")

kana = Label(kanji_window, text="", bg="#1F1F1F", fg="grey", font=("YasashisaGothicBold-V2", 20))
kana.pack(side="top")

answer = Label(kanji_window, text="...", bg="#1F1F1F", fg="white",  font=("Montserrat", 15))
answer.pack(side="top")

space = Label(kanji_window, text="", bg="#1F1F1F", font=("YasashisaGothicBold-V2", 5))
space.pack(side="top")

enter = Entry(kanji_window,width=30,justify=CENTER, bg="white", fg="black", font=("Montserrat", 15),bd=0)  
enter.pack(side="top")

space = Label(kanji_window, text="", bg="#1F1F1F", font=("YasashisaGothicBold-V2", 5))
space.pack(side="top")

show_answer = Button(kanji_window,text="Показать ответ",font=("Montserrat",15),width=15,height=1,bd=0,bg="black",fg="white",command=show_answer)
show_answer.pack(side="top")

space = Label(kanji_window, text="", bg="#1F1F1F", font=("YasashisaGothicBold-V2", 5))
space.pack(side="top")

space = Label(kanji_window, text="", bg="#1F1F1F", font=("YasashisaGothicBold-V2", 5))
space.pack(side="top")

text_bottom = Label(kanji_window, bg="#1F1F1F", fg="white", text="Артём Царюк, 2022",font=("Montserrat",13))
text_bottom.pack(side="top")

#---------------------------------START---------------------------------

next_kanji()

while True:
	window.update()
	if (enter.get() == romaji_list[last_random_index]):
		enter.delete(0, END)
		clear_answer()

		next_kanji()