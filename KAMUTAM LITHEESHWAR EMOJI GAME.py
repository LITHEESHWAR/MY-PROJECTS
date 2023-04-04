from tkinter import *
from tkinter.messagebox import Message
TIME_TO_WAIT =4000 # in milliseconds 
from random import *
w=Tk()
w.config(background="Lavender")
w.title("EMOJI GAME--KAMUTAM LITHEESHWAR")
w.geometry("2000x2000")
l=['\U0001F604','\U0001F970','\U0001F607','\U0001F644','\U0001F621']
r=0;s=0;n=0;c=0;p=0;q=0#GLOBALS
def continuee():
    e2.delete(0,END)
    e3.delete(0,END)
    global r
    global s
    global n
    r=randint(0,4)
    s=selection(r)
    n=0
def exite():
    global n 
    n=0
    global p
    global q
    p=q=0
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e1.pack_forget()
    e2.pack_forget()
    e3.pack_forget()
    b1.pack_forget()
    b2.pack_forget()
    b3.pack_forget()
    b4.pack_forget()
    b5.pack_forget()
    be1.pack_forget()
    be2.pack_forget()
    b.pack(expand=True)
def click(e):
    global s
    global p
    global q
    global n
    global TIME_TO_WAIT
    if(n==0):
        p=p+1
        if(e in s):
            q=q+1
            t="YOU WIN "
            e2.insert(0,t)
        else:
            t="YOU LOST"
            e2.insert(0,t)
        t="Computer Selected:"+str(s)+" You Selected:"+str(list(e))+"."
        e3.insert(0,t)
        z=Tk()
        z.withdraw()
        z.after(TIME_TO_WAIT,z.destroy) 
        Message(title="SCORE", message=f"YOUR SCORE: {q} {e} \n NUMBER OF TRIALS: {p} {s}", master=z).show()
        n=n+1   
def selection(r):
    s=l[r]
    s=s*2
    return list(s)
def onentrye1():
    b.pack_forget()
    e1.pack(expand=True)
    e2.pack(expand=True)
    e3.pack(expand=True)
    b1.pack()
    b2.pack()
    b3.pack()
    b4.pack()
    b5.pack()
    be1.pack(side=LEFT)
    be2.pack(side=RIGHT)
    t="2 Emojis selected by System. Please select an Emoji that exactly Matches the System's Emoji"
    e1.insert(0,t)
    global r
    global s
    r=randint(0,4)
    s=selection(r)
e1=Entry(w,width=100,font=("ArialBlack",20),bg="White",fg="HotPink",justify=CENTER)
e2=Entry(w,width=80,font=("ArialBlack",20),bg="White",fg="DodgerBlue",justify=CENTER)
e3=Entry(w,width=60,font=("ArialBlack",20),bg="White",fg="MediumVioletRed",justify=CENTER)
b1=Button(w,text="\U0001F604",font=90,padx=30,height=3,activebackground="Cyan",activeforeground="Yellow",bg="white",fg="Black",pady=10,command=lambda:click('\U0001F604'))
b2=Button(w,text="\U0001F970",font=90,padx=30,height=3,activebackground="Cyan",activeforeground="Yellow",bg="white",fg="Black",pady=10,command=lambda:click('\U0001F970'))
b3=Button(w,text="\U0001F607",font=90,padx=30,height=3,activebackground="Cyan",activeforeground="Yellow",bg="white",fg="Black",pady=10,command=lambda:click('\U0001F607'))
b4=Button(w,text="\U0001F644",font=90,padx=30,height=3,activebackground="Cyan",activeforeground="Yellow",bg="white",fg="Black",pady=10,command=lambda:click('\U0001F644'))
b5=Button(w,text="\U0001F621",font=90,padx=30,height=3,activebackground="Cyan",activeforeground="Yellow",bg="white",fg="Black",pady=10,command=lambda:click('\U0001F621'))
be1=Button(w,text="Click Here To Continue",padx=30,pady=10,font=("Arial",15),activebackground="White",activeforeground="Black",bg='Black',fg='White',command=continuee)
be2=Button(w,text="Click Here To Exit",padx=30,pady=10,font=("Arial",15),activebackground="White",activeforeground="Black",bg='Black',fg='White',command=exite)
b=Button(w,text="Click Here To Start",padx=30,pady=10,font=("Arial",15),activebackground="White",activeforeground="Black",bg='Black',fg='White',command=onentrye1)
b.pack(expand=True)
w.mainloop()
