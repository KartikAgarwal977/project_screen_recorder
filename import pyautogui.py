import pyautogui
import cv2
import numpy as np
from tkinter import *
from lplay import lplay
from screenshot import  screenshot1
import time
def countdown():
    
    times = int(hrs.get())*3600+ int(mins.get())*60 + int(sec.get())
    while times > -1:
        minute,second = (times // 60 , times % 60)
        
        hour = 0
        if minute > 60:
            hour , minute = (minute // 60 , minute % 60)
      
        sec.set(second)
        mins.set(minute)
        hrs.set(hour)
   
        master.update()
        time.sleep(1)

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
sec = StringVar()
Entry(master, textvariable = sec, width = 2, font = 'arial 12').place(x=250, y=155)
sec.set('00')

mins= StringVar()
Entry(master, textvariable = mins, width =2, font = 'arial 12').place(x=225, y=155)
mins.set('00')

hrs= StringVar()
Entry(master, textvariable = hrs, width =2, font = 'arial 12').place(x=200, y=155)
hrs.set('00')
master.config(bg ='blanched almond')
# label of screen record button   
Label(master, text="Screen Record",bg = 'papaya whip').grid(row=0, sticky=E, rowspan=4)
# button to start record  
b = Button(master, text="rec", command = screen_recorder and countdown )
b.grid(row=0, column=2, columnspan=6, rowspan=2, padx=5, pady=5)
# label of screenshot button 
Label(master , text = "screenshot",bg = 'papaya whip').grid(row = 4,column=0, sticky=E , rowspan= 1)
# button to capture screenshot
b1 = Button(master , text = "capture" , command= screenshot1 )
b1.grid(row =4 , column = 2, rowspan=6 , columnspan= 6)
mainloop()