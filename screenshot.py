import pyautogui as pg
# import time
from tkinter import *
import os 
def screenshot1() :
    '''It only for taking screenshots'''
    j = pg.screenshot()
    j.save("D:\\ss\\ss.png")
    root = Tk()
    root.title("save")
    global T
    T = Text(root,height=1,width=20)
    T.place(x=10, y= 30)
    def save() :
        name = T.get("1.0", "end-1c")
        try :
            os.rename("D:\\ss\\ss.png", "D:\\ss\\"+name+".png")
            Label(root,text="saved").place(x=20 , y= 90)
        except :
            Label(root,text= "already saved").place(x=100, y = 120)
    b = Button(root, text="save", command= save, font="Algerian", bg = "white",
 activebackground= "lightcyan")
    b.place(x=20, y=50)
    j.show()
    mainloop()