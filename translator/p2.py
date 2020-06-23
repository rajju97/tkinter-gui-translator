import top as top
from translate import *
from tkinter import *
from gtts import *
from PIL import *
from os import *
#translater funcyion
def translate():
    trans=Translator(from_lang=lan1.get(),to_lang=lan2.get())
    translation=trans.translate(var.get())
    var1.set(translation)
def assistant():
    language="en"
    out=gTTS(text=var.get(),lang=language,slow=False)
    out.save("rajju.mp3")
    system("start rajju.mp3")

#tkinder window with title
win=Tk()
win.title("Translator")
#creating frame and grid to hold the content
fram=Frame(win)
fram.grid(column=0,row=0,sticky=(N,W,E,S))
fram.columnconfigure(0,weight=1)
fram.rowconfigure(0,weight=1)
fram.pack(pady=100,padx=100)
photo=PhotoImage(file="water.png")
img=Label(image=photo)
img.pack()
#var for dropdown list
lan1=StringVar(win)
lan2=StringVar(win)
#choices to show
ch={"English","Hindi","Spanish","German","French","Gujarati","Japanese","Marathi","Nepali","Polish","Portuguese","Russian","Tamil","Urdu","Chinese"}
#default selection
lan1.set("English")
lan2.set("Hindi")
#creating dropdown and arranging inna grid
lanmenu1=OptionMenu(fram,lan1,*ch,)
Label(fram,text="select language",fg="blue").grid(row=0,column=1)
lanmenu1.grid(row=1,column=1)
lanmenu2=OptionMenu(fram,lan2,*ch,)
Label(fram,text="select a language",fg="blue").grid(row=0,column=2)
lanmenu2.grid(row=1,column=2)
#text boxes for input
Label(fram,text="enter text",fg="RED").grid(row=2,column=0)
var=StringVar()
text=Entry(fram,textvariable=var,fg="red",bd=6,bg="yellow",font="TimesNewRoman 13 bold").grid(row=2,column=1)
#textbox to show output
Label(fram,text="translate output",fg="red").grid(row=2,column=2)
var1=StringVar()
text1=Entry(fram,textvariable=var1,fg="red",bd=6,bg="yellow",font="TimesNewRoman 13 bold").grid(row=2,column=3)
#creating a button to call translator
b=Button(fram,text="Translate",command=translate,bd=7,activebackground="yellow").grid(row=3,column=3,columnspan=3)
tts=Button(fram,text="text to speech",command=assistant,bd=7,activebackground="yellow").grid(row=3,column=1)
win.mainloop()


