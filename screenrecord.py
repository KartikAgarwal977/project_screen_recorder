import pyautogui
import cv2
import numpy as np
from tkinter import *
from lplay import lplay
from screenshot import  screenshot1

def screen_recorder () :
	resolution = (1920, 1080)

	codec = cv2.VideoWriter_fourcc(*"FMP4")

	file = input("Enter the filename :")
	filename ="D:\\ss\\"+file+".avi" 

	fps = 20.0

	out = cv2.VideoWriter(filename, codec, fps, resolution)

	cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

	cv2.resizeWindow("Live", 480, 270)

	while True:
		img = pyautogui.screenshot()

		frame = np.array(img)

		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

		out.write(frame)

		cv2.imshow('Live', frame)

		if cv2.waitKey(1) == ord('q'):
			break

	out.release()

	cv2.destroyAllWindows()
l = lplay()
master = Tk()
# label of screen record button   
Label(master, text="Screen Record").grid(row=0, sticky=E, rowspan=4)
# button to start record  
b = Button(master, text="rec", command = screen_recorder)
b.grid(row=0, column=2, columnspan=6, rowspan=2, padx=5, pady=5)
# label of screenshot button 
Label(master , text = "screenshot").grid(row = 4, sticky=E , rowspan= 15)
# button to capture screenshot
b1 = Button(master , text = "capture" , command= screenshot1 )
b1.grid(row =4 , column = 2, rowspan=6 , columnspan= 6)
mainloop()