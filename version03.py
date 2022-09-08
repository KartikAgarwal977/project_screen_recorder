from time import sleep
import keyboard
import pyautogui
import cv2
import numpy as np
from tkinter import *
from lplay import lplay
import os
import pyautogui as pg


# The turtle screen use as logo finish
l = lplay()
master = Tk()
######################################################################################################
# The save function for screen recorder
def save () :
	name = T.get("1.0", "end-1c")
	try :
		os.rename("D:\\ss\\jj.avi", "D:\\ss\\"+name+".avi") # The path and rename takes place
		Label(master,text="saved").place(x=100 , y= 120)
	except :
		Label(master,text= "already saved").place(x=100, y = 120)
##############################################################################################
# The recording function
def screen_recorder () :
	resolution = (1920, 1080)
	master.wm_state("iconic")
	codec = cv2.VideoWriter_fourcc(*"FMP4")
	
	fps = 20.0
	filename = "D:\\ss\\jj.avi"	

	
	out = cv2.VideoWriter(filename, codec, fps, resolution)

	cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

	cv2.resizeWindow("Live", 480, 270)

	while True:
		
		img = pyautogui.screenshot()

		frame = np.array(img)
			
		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

		out.write(frame)
		cv2.imshow('Live', frame)


		if cv2.waitKey(1)== ord("q"):
				break
		if keyboard.is_pressed('ctrl+c') :
			break
		
	out.release()
	cv2.destroyAllWindows()
	master.wm_state("normal")
	global T
	T = Text(master, height = 1, width = 20)
	T.place(x=10, y= 90)
	b3 = Button(master, text="save", command= save, font="Algerian", bg = "white",
 activebackground= "lightcyan")
	b3.place (x=200, y=90)

# the save function of screenshot
def save1() :
        name = T.get("1.0", "end-1c")
        try :
            os.rename("D:\\ss\\ss.png", "D:\\ss\\"+name+".png")
            Label(master,text="saved").place(x=100 , y= 120)
        except :
            Label(master,text= "already saved").place(x=100, y = 120)

# For screen shot the function is defined 
def screenshot1() :
    '''It only for taking screenshots'''
    master.wm_state("iconic")
    sleep(0.5)
    j = pg.screenshot()
    global T
    T = Text(master,height=1,width=20)
    T.place(x=10, y= 90)
    j.show()
    j.save("D:\\ss\\ss.png")
    master.wm_state("normal")
    b = Button(master, text="save", command= save1, font="Algerian", bg = "white",
 activebackground= "lightcyan")
    b.place(x=200, y=90)


# Here is the gui buttons and specified front work

# button to start record  
master.geometry("320x150")
master.resizable(0,0)
master.title('Screen_App')
p = PhotoImage(file="D:\\html\\lolo.png")
master.iconphoto(False,p)
master.configure(background="ivory2")
# label of screen record button  
b = Button(master, text="rec", command = screen_recorder, font="Algerian", bg= "white",
 activebackground="lightcyan")
Label(master, text="Screen Record",font='Engravers').place(x=0,y=10)
b.place(x=200 , y=10)
# label of screenshot button 
Label(master , text = "Screenshot",font= 'Engravers').place(x=0,y=50)
# button to capture screenshot
b1 = Button(master , text = "capture" , command= screenshot1, font= "Algerian", bg='white', 
                activebackground="lightcyan" )
b1.place(x=200, y= 50)
mainloop()