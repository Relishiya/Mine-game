from tkinter import *
from tkinter.ttk import *
import array
import tkinter as tk
import numpy as np
import random
import sys
import test
import copy
import collections
import random
from tkinter import messagebox
from random import randint

root = tk.Tk()
labels=[]

string='Loc'
print(" ")
print("---------------------START----------------------------------")
print(" ")
def fun():
    global labels
    global array
    global randnums
    
    array= [0]*25
    print("25 rooms are allocated zeros")
    print(array)
    print(" ")
    randnums= random.sample(range(2,25),8)
    print("Locations of the mines are allocated randomly")
    print(randnums)
    my_rand=list(randnums)
    print("")
    print("mines are assigned as digit 7 and alerts are assigned to digit 1.. if the alert is in both sides then the alerts are assigned to 2 ")
    for a in range(0,8):
        array[randnums[a]]=7
    
        #print(array[randnums[a]]=7)
        if(array[randnums[a]+1]!=7):
            array[randnums[a]+1]=array[randnums[a]+1]+1
        if(array[randnums[a]-1]!=7):
            array[randnums[a]-1]=array[randnums[a]-1]+1

    print(array)


    print("")
    print(" ************START MOVING THE AGENT**********")


    val=0    
    for b in range(0,25):
        print("go")
        tk.Label(root, text=" # ",background='blue', height=2, width=5).grid(column=i, row=1)
        root.after(500)
        if(array[b]==1 or array[b]==2):
            b=randint(0,24)
            print(array[b])
            if (array[b]==7):
                print("you lost the attempt")
                tk.Label(root, text=" # ",background='blue', height=2, width=5).grid(column=i, row=1)
                root.after(500)
                val+=1
                if(val==2):
                    messagebox.showinfo("you lost the 2nd attempt")
                    break
            elif (array[b]!=7):
                print("safe to move after random move")
                tk.Label(root, text=" # ",background='blue', height=2, width=5).grid(column=i, row=1)
                root.after(500)
    for a in range(0,8):
        tk.Label(root, text="*",background='red', height=2, width=5).grid(column=randnums[a], row=0)
        
for i in range(25):
    tk.Label(root, text=str(i),background='lime green',height=2, width=5).grid(column=i, row=0)
for i in range(25):
    tk.Label(root, text=str(i),background='yellow', height=2, width=5).grid(column=i, row=1)

btn=tk.Button(root,text="start",height=2,width=5,command =fun)
btn.grid(column=2,row=4)


        

"""
class GFG: 
    def __init__(self, master = None): 
        self.master = master 
          
        # to take care movement in x direction 
        self.x = 1
        # to take care movement in y direction 
        self.y = 0
  
        # canvas object to create shape 
        self.canvas = Canvas(master) 
        # creating rectangle 
        self.rectangle = self.canvas.create_oval( 
                         5, 10, 25, 25, fill = "black") 
        self.canvas.pack() 
  
        # calling class's movement method to  
        # move the rectangle 
        self.movement()
    def movement(self): 
  
        # This is where the move() method is called 
        # This moves the rectangle to x, y coordinates 
        self.canvas.move(self.rectangle, self.x, self.y) 
  
        self.canvas.after(100, self.movement) 
      
    # for motion in negative x direction 
    def left(self, event): 
        print(event.keysym) 
        self.x = -5
        self.y = 0
      
    # for motion in positive x direction 
    def right(self, event): 
        print(event.keysym) 
        self.x = 5
        self.y = 0
      
    # for motion in positive y direction 
    def up(self, event): 
        print(event.keysym) 
        self.x = 0
        self.y = -5
      
    # for motion in negative y direction 
    def down(self, event): 
        print(event.keysym) 
        self.x = 0
        self.y = 5
  
if __name__ == "__main__": 
  
    # object of class Tk, resposible for creating 
    # a tkinter toplevel window 
    master = Tk() 
    gfg = GFG(master) 
    # This will bind arrow keys to the tkinter 
    # toplevel which will navigate the image or drawing 
    master.bind("<KeyPress-Left>", lambda e: gfg.left(e)) 
    master.bind("<KeyPress-Right>", lambda e: gfg.right(e)) 
    master.bind("<KeyPress-Up>", lambda e: gfg.up(e)) 
    master.bind("<KeyPress-Down>", lambda e: gfg.down(e)) 
tk.Button(root, text="start",background='Blue',comment=lambda e: gfg.left(e),height=2, width=5).grid(column=6, row=3)         
"""
tk.mainloop()






