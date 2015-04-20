
# coding: utf-8

## Robot GUI

###### Please select Cell > Run All !! DO NOT close turtle world before GUI.

# In[9]:

from swampy.TurtleWorld import *
from math import *
import random
from Tkinter import *
import tkFont
import turtle


# In[10]:

#Find the comma and parse the string that follows
def Parse():
    inputs=stringtext.get("1.0",END)
    inputs+=","
    strbeg=0;
    for i in range (0,len(inputs)):
        if inputs[i]==",":
            Move(inputs[strbeg:i])
            strbeg=i+1


# In[11]:

#Determine the parsed command
def Move(command):
    command=command.upper()
    if command[0]=="F":
        #forward
        fd(bob,int(command[1:]))
    elif command[0]=="R":
        #right wheel moves, left wheel holds
        print "placeholder"
    elif command[0]=="L":
        #left wheel moves, right wheel holds
        print "placeholder"
    elif command[0]=="T":
        #twist
        rt(bob,int(command[1:]))
    elif command[0]=="P":
        #pendown, penup
        if int(command[1])==1:
            bob.pd()
        elif int(command[1])==0:
            bob.pu()


# In[12]:

#create window & set the size/position
Window = Tk()
w = 750
h = 330
x = 630
y = 200
Window.geometry("%dx%d+%d+%d" % (w, h, x, y))
Window.configure(background="#a0db8e")
Window.wm_title("MathBot")


# In[13]:

#input box
stringtext = Text(Window, width=30, height=10)
stringtext.place(x=50, y=90)
execute=Button(Window, text='Move Robot', fg="black", command=Parse)
execute.place(x=50, y=270)


# In[14]:

#create turtle
world = TurtleWorld()
bob = Turtle()
set_color(bob, 'green');


# In[15]:

#instructions & commands
instruct = Label(text = 'Enter a list of commands seperated by commas.', bg='#a0db8e',fg='#101514',font=("Helvetica", 16))
instruct.place(x=50, y=40)
F = Label(text = 'F (forward)', bg='#a0db8e',fg='#101514',font=("Helvetica", 12))
F.place(x=400, y=100)
R = Label(text = 'R (right wheel moves, left wheel holds)', bg='#a0db8e',fg='#101514',font=("Helvetica", 12))
R.place(x=400, y=125)
L = Label(text = 'L (left wheel moves, right wheel holds)', bg='#a0db8e',fg='#101514',font=("Helvetica", 12))
L.place(x=400, y=150)
T = Label(text = 'T (twist)', bg='#a0db8e',fg='#101514',font=("Helvetica", 12))
T.place(x=400, y=175)
P0 = Label(text = 'P0 (penup)', bg='#a0db8e',fg='#101514',font=("Helvetica", 12))
P0.place(x=400, y=200)
P1 = Label(text = 'P1 (pendown)', bg='#a0db8e',fg='#101514',font=("Helvetica", 12))
P1.place(x=400, y=225)
exam = Label(text = 'Example: f60,T20,p0,F80,t10,P1,f-90', bg='#a0db8e',fg='#101514',font=("Helvetica", 12))
exam.place(x=400, y=250)


# In[16]:

Window.mainloop();

