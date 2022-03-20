import pyautogui as pg
import time
from tkinter import * 
def screenshot1() :
    '''It only for taking screenshots'''
    time.sleep(2)
    j = pg.screenshot()
    j.show()
    
    ss = input("Enter the name :")
    j.save("D:\\ss\\"+ss+".png") 