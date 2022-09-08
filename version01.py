import pyautogui
import cv2
import numpy as np
from tkinter import *
from lplay import lplay
from screenshot import  screenshot1
from time import time 
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
		# t =str( round((time() - starttime), 2))
		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

		out.write(frame)

		cv2.imshow('Live', frame)

		if cv2.waitKey(1)==ord("q"):
			break
	out.release()
	cv2.destroyAllWindows()
	
	
l = lplay()
master = Tk()
master.geometry("320x100")

# label of screen record button   
Label(master, text="Screen Record",font='Engravers').place(x=0,y=10)
# button to start record  
b = Button(master, text="rec", command = screen_recorder, font="Algerian", bg= "lightcyan")
b.place(x=200 , y=10)

# label of screenshot button 
Label(master , text = "Screenshot",font= 'Engravers').place(x=0,y=50)
# button to capture screenshot
b1 = Button(master , text = "capture" , command= screenshot1, font= "Algerian", bg="lightcyan" )
b1.place(x=200, y= 50)
mainloop()