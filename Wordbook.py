from tkinter import *
from tkinter import messagebox
import json
import pyttsx3
from difflib import get_close_matches
from PIL import ImageTk, Image
import os, sys

engine = pyttsx3.init()


def wordaudio():
    voices: object = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(enterwordentry.get())
    engine.runAndWait()


def  meaningaudio():
    voices: object = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(textarea.get(1.0, END))
    engine.runAndWait()


def iexit():
    res = messagebox.askyesno('Confirm', 'Do you want to exit?')
    if res == True:
        root.destroy()
    else:
        pass


def clear():
    textarea.config(state=NORMAL)
    enterwordentry.delete(0, END)
    textarea.delete(1.0, END)
    textarea.config(state=DISABLED)
    try:
        imgLabel.destroy()
    except Exception as e:
        pass
    try:
        imgLabelexception.destroy()
    except Exception as e:
        pass


def search():
    data = json.load(open('data.json'))
    word = enterwordentry.get()
    word = word.lower()

    if word in data:
        meaning = data[word]

        textarea.config(state=NORMAL)
        textarea.delete(1.0, END)
        imgdisplay()
        for item in meaning:
            textarea.insert(END, u'\u2022' + item + '\n\n')

        textarea.config(state=DISABLED)

    elif len(get_close_matches(word, data.keys())) > 0:

        close_match = get_close_matches(word, data.keys())[0]

        res = messagebox.askyesno('Confirm', 'Did you mean ' + close_match + ' instead?')

        if res == True:

            meaning = data[close_match]
            textarea.delete(1.0, END)
            enterwordentry.delete(0, END)
            enterwordentry.insert(END, close_match)
            textarea.config(state=NORMAL)
            imgdisplay()
            for item in meaning:
                textarea.insert(END, u'\u2022' + item + '\n\n')
            textarea.config(state=DISABLED)

        else:
            textarea.delete(1.0, END)
            messagebox.showinfo('Information', 'Please type a correct word')
            enterwordentry.delete(0, END)

    else:
        messagebox.showerror('Error', 'The word doesnt exist.Please double check it.')
        enterwordentry.delete(0, END)

def imgdisplay():
    try:
        global imgLabel
        Word = enterwordentry.get()
        Word.lower()
        imgname = Word + ".jpg"
        imgfile = os.path.join('ScrapedImages', imgname)
        img = ImageTk.PhotoImage(Image.open(imgfile))
        imgLabel = Label(root, image=img, anchor=NW)
        imgLabel.image = img
        imgLabel.place(x=80, y=100)
        #imgLabel.config(image=img)
    except Exception as e:
        global imgLabelexception
        imgLabelexception = Label(root, height=10, width=20, text="Image not availabe! :(")
        imgLabelexception.place(x=80, y=100)
        pass
    return


root = Tk()
root.geometry('1000x626+100+50')
root.title('Wordbook: Text-to-Speech Dictionary')

root.resizable(0, 0)

bgimage = PhotoImage(file='bg.png')

bgLabel = Label(root, image=bgimage)
bgLabel.place(x=0, y=0)

enterwordLabel = Label(root, text='Enter Word', font=('castellar', 29, 'bold'), fg='red3', bg='whitesmoke')
enterwordLabel.place(x=570, y=20)

enterwordentry = Entry(root, font=('arial', 23, 'bold'), bd=8, relief=GROOVE, justify=CENTER)
enterwordentry.place(x=510, y=80)

enterwordentry.focus_set()

searchimage = PhotoImage(file='search.png')
searchButton = Button(root, image=searchimage, bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2',
                      command=search)
searchButton.place(x=620, y=150)

micimage = PhotoImage(file='mic.png')
micButton = Button(root, image=micimage, bd=0, bg='whitesmoke', activebackground='whitesmoke',
                   cursor='hand2', command=wordaudio)
micButton.place(x=710, y=153)

meaninglabel = Label(root, text='Meaning', font=('castellar', 29, 'bold'), fg='red3', bg='whitesmoke')
meaninglabel.place(x=580, y=240)

textarea = Text(root, font=('arial', 18, 'bold'), height=8, width=34, bd=8, relief=GROOVE, wrap='word')
textarea.place(x=460, y=300)

audioimage = PhotoImage(file='microphone.png')
audioButton = Button(root, image=audioimage, bd=0, bg='whitesmoke', activebackground='whitesmoke',
                     cursor='hand2', command=meaningaudio)
audioButton.place(x=530, y=555)

clearimage = PhotoImage(file='clear.png')
clearButton = Button(root, image=clearimage, bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2'
                     , command=clear)
clearButton.place(x=660, y=555)

exitimage = PhotoImage(file='exit.png')
exitButton = Button(root, image=exitimage, bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2',
                    command=iexit)
exitButton.place(x=790, y=555)

root.mainloop()
