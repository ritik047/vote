from tkinter import *
from tkinter import messagebox

#global count
#global count1=0
count2=0
def hello():
    global count
    print("HY Ritik this side !!!")
    messagebox.showinfo("Welcome Superpower2020","Welcome to the Detention Centre\n#Copied from China")
    count =count+1
def chutiya():
    messagebox.showinfo("","Do we even exist!!!")
    count1=count1+1
def dev():
    messagebox.showinfo("","Development Asap")
    count2=count2+1
    
tc=Tk()
tc.geometry("500x500")
ab=Button(tc,text="AAP",bg="black",fg="white",command=dev)
cg=Button(tc,text="Cong",bg="black",fg="white",command=chutiya)
gb=Button(tc,text="BJP",bg="black",fg="white",command= hello )
gg=Label(tc,text="Voting day today:",font=("product sans",30,""))
gg.pack()
gb.place(x=5,y=70)
gb.config(height=5,width=10)
#gb.pack()
#ab.pack()
ab.place(x=100,y=70)
ab.config(height=5,width=10)

#cg.pack()
cg.place(x=200,y=70)
cg.config(height=5,width=10)
