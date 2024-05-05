import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox


import pyttsx3
import os
from PIL import ImageTk,Image

root = Tk()
root.title("Text to speech")
root.geometry("900x450+100+100")
root.resizable(False,False)
root.configure(bg="#305065")


# Icon
image_icon = PhotoImage(file="tspeech.png")
root.iconphoto(False,image_icon)


engine = pyttsx3.init()

def speaknow():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if gender == 'Male':
            engine.setProperty('voice',voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            engine.say(text)
            engine.runAndWait()
    if text:
        if speed == 'Fast':
            engine.setProperty('rate',250)
            setvoice()
        elif speed == 'Normal':
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()
def download():
    op = messagebox.askyesno("Save","Do you want to save the file into MP3")
    if op == 1:
        text = text_area.get(1.0, END)
        gender = gender_combobox.get()
        speed = speed_combobox.get()
        voices = engine.getProperty('voices')

        def setvoice():
            if gender == 'Male':
                engine.setProperty('voice', voices[0].id)
                path = filedialog.askdirectory()
                os.chdir(path)
                engine.save_to_file(text,'text.mp3')
                engine.runAndWait()
            else:
                engine.setProperty('voice', voices[1].id)
                path = filedialog.askdirectory()
                os.chdir(path)
                engine.save_to_file(text,'text.mp3')
                engine.runAndWait()

        if text:
            if speed == 'Fast':
                engine.setProperty('rate', 250)
                setvoice()
            elif speed == 'Normal':
                engine.setProperty('rate', 130)
                setvoice()
            else:
                engine.setProperty('rate', 60)
                setvoice()
    else:
        return



def about():

    def close():
        ab_top.destroy()

    ab_top = Toplevel()
    frame1 = Frame(ab_top,bg="white",width=420,height=100).place(x=0,y=0)
    ab_top.title("About")
    ab_image_icon = PhotoImage(file="tspeech.png")
    ab_top.iconphoto(False, ab_image_icon)
    ab_top.geometry("420x175")
    ab_top.resizable(False, False)
    ab_top.configure(bg="#305065")
    Label(ab_top, text="J-Tech Software Developer Company \n   contact : 9890873444",font=("Britannic",15),bg="white",fg="#305065").place(x=20,y=20)
    button = Button(ab_top,text="Close",width=10, font=("Arial",15),command=close).place(x=130,y=120)






# Top Frame
Top_frame = Frame(root,bg="white",width=900,height=100)
Top_frame.place(x=0,y=0)

Logo = ImageTk.PhotoImage(Image.open("speech.jpg"))
Label(Top_frame, image=Logo, bg="white").place(x=10,y=5)

Label(Top_frame, text="TEXT TO SPEECH",font=("Britannic",20,"bold"),bg="White",fg="#305065").place(x=130,y=30)
Label(Top_frame, text="Powerd by J-Tech",font=("Britannic",10,"bold"),bg="white",fg="#305065").place(x=400,y=40)
# text area

text_area = Text(root, font=("Robote",20,),bg="white",relief=GROOVE,wrap=WORD)
text_area.place(x=10,y=150,width=500,height=250)

Label(root, text="VOICE",font=("Arial",14,"bold"),bg="#305065",fg="White").place(x=580,y=160)
Label(root, text="SPEED",font=("Arial",14,"bold"),bg="#305065",fg="White").place(x=730,y=160)

gender_combobox = Combobox(root, values=["Male","Female"],font=("Britannic",14),state='r',width=10)
gender_combobox.place(x=550,y=200)
gender_combobox.set("Male")

speed_combobox = Combobox(root, values=["Fast","Normal","Slow"],font=("Britannic",14),state='r',width=10)
speed_combobox.place(x=730,y=200)
speed_combobox.set("Normal")


imageicon = ImageTk.PhotoImage(Image.open("icon.jpg"))
bnt = Button(root, text="  Speak",compound=LEFT,image=imageicon,width=140,font=("Britannic",14,"bold"),command=speaknow)
bnt.place(x=550,y=280)

imageicon1 = ImageTk.PhotoImage(Image.open("download.png"))
bnt = Button(root, text="Download",compound=LEFT,image=imageicon1,bg="white",width=150,font=("Britannic",14,"bold"),command=download)
bnt.place(x=730,y=280)

imageicon2 = ImageTk.PhotoImage(Image.open("about.png"))
bnt = Button(root, text="About",compound=LEFT,bg="White",image=imageicon2,width=150,font=("Britannic",14,"bold"),fg="Black",command=about)
bnt.place(x=630,y=360)








root.mainloop()
