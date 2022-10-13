from tkinter import*
from PIL import Image,ImageTk
import tkinter.font
from timeit import default_timer as timer
import random
from tkinter import messagebox
from time import time,strftime  
import time
root=Tk()
root.geometry("950x550")
root.maxsize(950, 550)
root.minsize(950, 550)
x = 0
score=0
currentQ = ''
currentA = ''
score = 0
word = 0
i=0
root.config(background="white")

entry=StringVar(root,value="")

ewords =["blue","sky","draw","word","yolk","light","cinema","action","music","green","baby","door","python","coding"]
mwords=["move on","cucumber","pineapple","according","milkeyway","flawless","growth","blackberry","butterscotch"]
hwords=["dictionaries","lifesaver","slow down","charging port","individually"," adminstration","quarantine","hypermetropia","divided by","sillicon valley"]
timeLeft = {'min':0, 'sec':40 }
high_score1=open('easyhighscore.txt','r+')
hs1=int(high_score1.readline())
high_score2=open('mediumhighscore.txt','r+')
hs2=int(high_score2.readline())
high_score3=open('hardhighscore.txt','r+')
hs3=int(high_score3.readline())
    
def easygame():
    global i,currentQ,x2,b2, currentA,word,groot,word_entry,image,photo,ph_label,image2,photo2,ph_label2,showtime,timeshow,timeLeft,eresult,eroot,image3,photo3,ph_label3,r1,f2,easyhighscore
    if i==0:
        eroot.destroy()
        i=i+1
    
    def eresult():
        def quit1():
            erroot.destroy()
        groot.destroy()
        global erroot,image3,photo3,ph_label3,r1,f2,score,hs1,easyhighscore
        erroot=Tk()
        erroot.geometry("750x450")
        erroot.maxsize(750, 450)
        erroot.minsize(750, 450)
        erroot.title("easy test result")
        image3=Image.open("result.jpg")
        image3 = image3.resize((750, 450),Image.ANTIALIAS)
        photo3=ImageTk.PhotoImage(image3)
        ph_label3=Label(image=photo3)
        ph_label3.place(x=0,y=30)
        f2=Frame(erroot,bg="gold")
        f2.pack(side=TOP,fill="x")
        if score>hs1:
             high_score1.seek(0)
             hs1=score
             file=open("easyhighscore.txt","w")
             file.write(str(hs1))
             #high_score1.write(str(hs1))
             
        r1=Label(f2,text="YOUR SCORE IS {}".format(score),font=("Comic Sans MS",30,'bold'),fg="black",bg="gold")
        r1.pack(pady=5)
        r2=Label(erroot,text="HIGHSCORE {}".format(str(hs1)),font=("Comic Sans MS",25,'bold'),fg="black",bg="gold")
        r2.place(x=250,y=380)
        r3=Label(erroot,text="EASY LEVEL",font=("Comic Sans MS",15,'bold'),fg="black",bg="gold")
        r3.place(x=20,y=80)
        b2 = Button(erroot, text="QUIT",font=("Comic Sans MS",15,'bold'),command=quit1,width=5, fg='gold',bg='black')
        b2.place(x=650, y=380)
        
           
    def timeshow():
         
         global i, timeLeft,showtime,groot,word_entry,x2,currentQ,eresult
         

         if timeLeft['sec']>0:    
                timeLeft['sec']-=1
                showtime.config(text='Time Left: {}min:{}sec'.format(timeLeft['min'],timeLeft['sec']))
                showtime.after(1000, timeshow) 
         elif timeLeft['min']==0 and timeLeft['sec']==0:
                messagebox.showwarning("TIME UP!","YOUR TIME IS UP!" )
                eresult()
                
                
    
    def la():
         global x2,word_entry,currentQ,score,f,x4,start,end,timeshow,timeLeft,hs1
         f=0
         if word_entry.get() == currentQ:
                score=score+1
                
                
                
         else:
            
            messagebox.showerror("showerror", "WRONG INPUT!")
         
         ewords.remove(currentQ)
         x2.destroy()
         
         
         word_entry.delete(0, 'end')
         l()
         
    def l():
        global word_entry,x2,currentQ,start,end,timeshow,timeLeft
        
        if len(ewords)>0:
                
                currentQ = random.choice(ewords)
                x3 = Label(groot, text="START TYPING THE WORD",fg="white", font=("Comic Sans MS",30),bg="black")
                x3.place(x=150, y=10)
                word_entry = Entry(groot,text=" ", font=("Comic Sans MS",20))
                word_entry.place(x=350, y=110,height=50,width=350)
                x2 = Label(groot, text=currentQ,fg="white", font=("Comic Sans MS",30),bg="black")
                x2.place(x=100, y=100)
                b2 = Button(groot, text="DONE",font=("Comic Sans MS",15),command=la,width=5, bg='white')
                b2.place(x=720, y=110)
                
        
        if len(ewords)==0:
                
                groot.destroy()

    groot=Tk()
    groot.geometry("830x450")
    groot.maxsize(830, 450)
    groot.minsize(830, 450)
    groot.title("Easy level typing speed test game")   
    image=Image.open("groot.jpg")
    image = image.resize((830, 450),Image.ANTIALIAS)
    photo=ImageTk.PhotoImage(image)
    ph_label=Label(image=photo)
    ph_label.place(x=0,y=0)
    image1=Image.open("type.jpg")
    image1 = image1.resize((280, 250),Image.ANTIALIAS)
    photo1=ImageTk.PhotoImage(image1)
    ph_label1=Label(image=photo1)
    ph_label1.place(x=0,y=200)
    showtime = Label(groot, text='', font=("Comic Sans MS",20),height=1,width=19, fg='black', bg='goldenrod2')
    showtime.place(x=400, y=350)
    timeshow()
    if len(ewords)>0:     
        l()
           
    groot.mainloop()
def mediumgame():
    global i,currentQ,x2,b2, currentA,word,groot,word_entry,image,photo,ph_label,image2,photo2,ph_label2,showtime,timeshow,timeLeft,eresult,eroot,image3,photo3,ph_label3,r1,f2,mediumhighscore
    if i==0:
        eroot.destroy()
        i=i+1
    
    def eresult():
        groot.destroy()
        def quit1():
            erroot.destroy()
        global erroot,image3,photo3,ph_label3,r1,f2,score,hs2,mediumhighscore
        erroot=Tk()
        erroot.geometry("750x450")
        erroot.maxsize(750, 450)
        erroot.minsize(750, 450)
        erroot.title("medium test result")
        image3=Image.open("result.jpg")
        image3 = image3.resize((750, 450),Image.ANTIALIAS)
        photo3=ImageTk.PhotoImage(image3)
        ph_label3=Label(image=photo3)
        ph_label3.place(x=0,y=30)
        f2=Frame(erroot,bg="gold")
        f2.pack(side=TOP,fill="x")
        r1=Label(f2,text="YOUR SCORE IS {}".format(score),font=("Comic Sans MS",30,'bold'),fg="black",bg="gold")
        r1.pack(pady=5)
        r2=Label(erroot,text="HIGHSCORE {}".format(str(hs2)),font=("Comic Sans MS",25,'bold'),fg="black",bg="gold")
        r2.place(x=250,y=380)
        r3=Label(erroot,text="MEDIUM LEVEL",font=("Comic Sans MS",15,'bold'),fg="black",bg="gold")
        r3.place(x=20,y=80)
        b2 = Button(erroot, text="QUIT",font=("Comic Sans MS",15,'bold'),command=quit1,width=5, fg='gold',bg='black')
        b2.place(x=650, y=380)
    def timeshow():
         
         global i, timeLeft,showtime,groot,word_entry,x2,currentQ,eresult
         

         if timeLeft['sec']>0:    
                timeLeft['sec']-=1
                showtime.config(text='Time Left: {}min:{}sec'.format(timeLeft['min'],timeLeft['sec']))
                showtime.after(1000, timeshow) 
         elif timeLeft['min']==0 and timeLeft['sec']==0:
                messagebox.showwarning("TIME UP!","YOUR TIME IS UP!" )
                eresult()
                
                
    
    def la():
         global x2,word_entry,currentQ,score,f,x4,start,end,timeshow,timeLeft,hs2,mediumhighscore
         f=0
         if word_entry.get() == currentQ:
                score=score+1
                
                
                
         else:
            
            messagebox.showerror("showerror", "WRONG INPUT!")
         
         mwords.remove(currentQ)
         x2.destroy()
         
         if score>hs2:
             high_score2.seek(0)
             file=open("mediumhighscore.txt","w")
             file.write(str(hs1))
             #high_score2.write(str(score))
             hs2=score
             file=open("mediumhighscore.txt","w")
             file.write(str(hs2))
         word_entry.delete(0, 'end')
         l()
         
    def l():
        global word_entry,x2,currentQ,start,end,timeshow,timeLeft
        
        if len(mwords)>0:
                
                currentQ = random.choice(mwords)
                x3 = Label(groot, text="START TYPING THE WORD",fg="white", font=("Comic Sans MS",30),bg="black")
                x3.place(x=150, y=10)
                word_entry = Entry(groot,text=" ", font=("Comic Sans MS",20))
                word_entry.place(x=350, y=110,height=50,width=350)
                x2 = Label(groot, text=currentQ,fg="white", font=("Comic Sans MS",30),bg="black")
                x2.place(x=60, y=100)
                b2 = Button(groot, text="DONE",font=("Comic Sans MS",15),command=la,width=5, bg='white')
                b2.place(x=720, y=110)
                
        
        if len(mwords)==0:
                
                groot.destroy()

    groot=Tk()
    groot.geometry("830x450")
    groot.maxsize(830, 450)
    groot.minsize(830, 450)
    groot.title("Medium level typing speed test game")   
    image=Image.open("groot.jpg")
    image = image.resize((830, 450),Image.ANTIALIAS)
    photo=ImageTk.PhotoImage(image)
    ph_label=Label(image=photo)
    ph_label.place(x=0,y=0)
    image1=Image.open("type.jpg")
    image1 = image1.resize((280, 250),Image.ANTIALIAS)
    photo1=ImageTk.PhotoImage(image1)
    ph_label1=Label(image=photo1)
    ph_label1.place(x=0,y=200)
    showtime = Label(groot, text='', font=("Comic Sans MS",20),height=1,width=19, fg='black', bg='goldenrod2')
    showtime.place(x=400, y=350)
    timeshow()
    if len(mwords)>0:     
        l()
           
    groot.mainloop()

def hardgame():
    global i,currentQ,x2,b2, currentA,word,groot,word_entry,image,photo,ph_label,image2,photo2,ph_label2,showtime,timeshow,timeLeft,eresult,eroot,image3,photo3,ph_label3,r1,f2,hardhighscore
    if i==0:
        eroot.destroy()
        i=i+1
    
    def eresult():
        groot.destroy()
        def quit1():
            erroot.destroy()
        global erroot,image3,photo3,ph_label3,r1,f2,score,hs3,hardhighscore
        erroot=Tk()
        erroot.geometry("750x450")
        erroot.maxsize(750, 450)
        erroot.minsize(750, 450)
        erroot.title("hard test result")
        image3=Image.open("result.jpg")
        image3 = image3.resize((750, 450),Image.ANTIALIAS)
        photo3=ImageTk.PhotoImage(image3)
        ph_label3=Label(image=photo3)
        ph_label3.place(x=0,y=30)
        f2=Frame(erroot,bg="gold")
        f2.pack(side=TOP,fill="x")
        r1=Label(f2,text="YOUR SCORE IS {}".format(score),font=("Comic Sans MS",30,'bold'),fg="black",bg="gold")
        r1.pack(pady=5)
        r2=Label(erroot,text="HIGHSCORE {}".format(str(hs3)),font=("Comic Sans MS",25,'bold'),fg="black",bg="gold")
        r2.place(x=250,y=380)
        r3=Label(erroot,text="HARD LEVEL",font=("Comic Sans MS",15,'bold'),fg="black",bg="gold")
        r3.place(x=20,y=80)
        b2 = Button(erroot, text="QUIT",font=("Comic Sans MS",15,'bold'),command=quit1,width=5, fg='gold',bg='black')
        b2.place(x=650, y=380)
    def timeshow():
         
         global i, timeLeft,showtime,groot,word_entry,x2,currentQ,eresult
         

         if timeLeft['sec']>0:    
                timeLeft['sec']-=1
                showtime.config(text='Time Left: {}min:{}sec'.format(timeLeft['min'],timeLeft['sec']))
                showtime.after(1000, timeshow) 
         elif timeLeft['min']==0 and timeLeft['sec']==0:
                messagebox.showwarning("TIME UP!","YOUR TIME IS UP!" )
                eresult()
                
                
    
    def la():
         global x2,word_entry,currentQ,score,f,x4,start,end,timeshow,timeLeft,hs3,hardhighscore
         f=0
         if word_entry.get() == currentQ:
                score=score+1
                
                
                
         else:
            
            messagebox.showerror("showerror", "WRONG INPUT!")
         
         hwords.remove(currentQ)
         x2.destroy()
         
         if score>hs3:
             high_score3.seek(0)
             file=open("hardhighscore.txt","w")
             file.write(str(hs3))
             #high_score3.write(str(score))
             hs3=score
             file=open("hardhighscore.txt","w")
             file.write(str(hs3))
         word_entry.delete(0, 'end')
         l()
         
    def l():
        global word_entry,x2,currentQ,start,end,timeshow,timeLeft
        
        if len(hwords)>0:
                
                currentQ = random.choice(hwords)
                x3 = Label(groot, text="START TYPING THE WORD",fg="white", font=("Comic Sans MS",30),bg="black")
                x3.place(x=150, y=10)
                word_entry = Entry(groot,text=" ", font=("Comic Sans MS",20))
                word_entry.place(x=350, y=110,height=50,width=350)
                x2 = Label(groot, text=currentQ,fg="white", font=("Comic Sans MS",30),bg="black")
                x2.place(x=60, y=100)
                b2 = Button(groot, text="DONE",font=("Comic Sans MS",15),command=la,width=5, bg='white')
                b2.place(x=720, y=110)
                
        
        if len(hwords)==0:
                
                groot.destroy()

    groot=Tk()
    groot.geometry("830x450")
    groot.maxsize(830, 450)
    groot.minsize(830, 450)
    groot.title("Hard level typing speed test game")   
    image=Image.open("groot.jpg")
    image = image.resize((830, 450),Image.ANTIALIAS)
    photo=ImageTk.PhotoImage(image)
    ph_label=Label(image=photo)
    ph_label.place(x=0,y=0)
    image1=Image.open("type.jpg")
    image1 = image1.resize((280, 250),Image.ANTIALIAS)
    photo1=ImageTk.PhotoImage(image1)
    ph_label1=Label(image=photo1)
    ph_label1.place(x=0,y=200)
    showtime = Label(groot, text='', font=("Comic Sans MS",20),height=1,width=19, fg='black', bg='goldenrod2')
    showtime.place(x=400, y=350)
    timeshow()
    if len(hwords)>0:     
        l()
           
    groot.mainloop()




def start():
    root.destroy()
    global proot
    proot=Tk()
    proot.geometry("750x450")
    proot.maxsize(750, 450)
    proot.minsize(750, 450)
    proot.title("start")
    f1=Frame(proot)
    f1.pack(side=TOP,fill="x")
    l1=Label(f1,text="TEST YOUR TYPING SPEED! CHOOSE A LEVEL",font=("Comic Sans MS",20))
    l1.pack(pady=22)
    image=Image.open("level1.jpg")
    photo=ImageTk.PhotoImage(image)
    ph_label=Label(proot,image=photo)
    ph_label.place(x=0,y=60)
    
    f2=Frame(proot)
    f2.place(relx=0.2, rely=0.5,anchor=CENTER)
    b1=Button(f2, text="EASY",font=("Comic Sans MS",20),command=easy)
    b1.pack()

    f2=Frame(proot)
    f2.place(relx=0.5, rely=0.5,anchor=CENTER)
    b1=Button(f2, text="MEDIUM",font=("Comic Sans MS",20),command=medium)
    b1.pack()

    f2=Frame(proot)
    f2.place(relx=0.8, rely=0.5,anchor=CENTER)
    b1=Button(f2, text="HARD",font=("Comic Sans MS",20),command=hard)
    b1.pack()
    proot.mainloop()

    
def easy():
    proot.destroy()
    global eroot
    eroot=Tk()
    eroot.geometry("850x450")
    eroot.maxsize(850, 450)
    eroot.minsize(850, 450)
    eroot.title("easy")
    image1=Image.open("typing.jpg")
    image1 = image1.resize((850, 450),Image.ANTIALIAS)
    photo1=ImageTk.PhotoImage(image1)
    ph_label1=Label(image=photo1)
    ph_label1.pack()

    x1 = Label(eroot, text="LETS START PLAYING....", font=("Comic Sans MS",20))
    x1.place(x=20, y=50)
    intro='''\t\tINSTRUCTIONS:
.......................................................................................................
        1. The total  time is 40 seconds.
        2. After clicking the GO button type the words as fast as you can.
        3. Each correct input contains 1 point.
        \t\tGOOD LUCK!!
.......................................................................................................'''

    x2 = Label(eroot, text=intro, font=("Comic Sans MS",13), wraplength=420, justify="left",height=10,width=43)
    x2.place(x=380, y=50)  
    b1 = Button(eroot, text="GO",font=("Comic Sans MS",15), command=easygame, width=10, bg='white')
    b1.place(x=550, y=350)
    eroot.mainloop()
def medium():
    proot.destroy()
    global eroot
    eroot=Tk()
    eroot.geometry("850x450")
    eroot.maxsize(850, 450)
    eroot.minsize(850, 450)
    
    eroot.title("medium")
    image1=Image.open("typing.jpg")
    image1 = image1.resize((850, 450),Image.ANTIALIAS)
    photo1=ImageTk.PhotoImage(image1)
    ph_label1=Label(image=photo1)
    ph_label1.pack()

    x1 = Label(eroot, text="LETS START PLAYING....", font=("Comic Sans MS",20))
    x1.place(x=20, y=50)
    intro='''\t\tINSTRUCTIONS:
.......................................................................................................
        1. The total  time is 40 seconds.
        2. After clicking the GO button type the words  as fast as you can.
        3. Each correct input contains 1 point.
        \t\tGOOD LUCK!!
.......................................................................................................'''

    x2 = Label(eroot, text=intro, font=("Comic Sans MS",13), wraplength=420, justify="left",height=10,width=43)
    x2.place(x=380, y=50)   
    b1 = Button(eroot, text="GO",font=("Comic Sans MS",15), command=mediumgame, width=10, bg='white')
    b1.place(x=550, y=350)
    eroot.mainloop()

def hard():
    proot.destroy()
    global eroot
    eroot=Tk()
    eroot.geometry("850x450")
    eroot.maxsize(850, 450)
    eroot.minsize(850, 450)
    
    eroot.title("hard")
    image1=Image.open("typing.jpg")
    image1 = image1.resize((850, 450),Image.ANTIALIAS)
    photo1=ImageTk.PhotoImage(image1)
    ph_label1=Label(image=photo1)
    ph_label1.pack()

    x1 = Label(eroot, text="LETS START PLAYING....", font=("Comic Sans MS",20))
    x1.place(x=20, y=50)
    intro='''\t\tINSTRUCTIONS:
.......................................................................................................
        1. The total  time is 40 seconds.
        2. After clicking the GO button type the words   as fast as you can.
        3. Each correct input contains 1 point.
        \t\tGOOD LUCK!!
.......................................................................................................'''

    x2 = Label(eroot, text=intro, font=("Comic Sans MS",13), wraplength=420, justify="left",height=10,width=43)
    x2.place(x=380, y=50)  
    b1 = Button(eroot, text="GO",font=("Comic Sans MS",15), command=hardgame, width=10, bg='white')
    b1.place(x=550, y=350)
    eroot.mainloop()

        
root.title("TYPING SPEED TEST")
f1=Frame(root,bg="white")
f1.pack(side=TOP,fill="x")
l1=Label(f1,text="WELCOME! TEST YOUR TYPING SPEED",font=("Comic Sans MS",30),bg="white")
l1.pack(pady=20)

f2=Frame(root,bg="black")
f2.pack(side=BOTTOM,fill="x")
b1=Button(f2, text="START",font=("Comic Sans MS",20),command=start)
b1.pack(pady=24)

image1=Image.open("welcome.jpg")
image1 = image1.resize((950, 550),Image.ANTIALIAS)
photo1=ImageTk.PhotoImage(image1)
ph_label1=Label(image=photo1)
ph_label1.pack()

root.mainloop()


