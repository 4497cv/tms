import cv2
#import numpy as np
import pyautogui
#import imutils
#from matplotlib import pyplot as plt

from pynput import mouse
from pynput import keyboard
import time
import sys
import string

RGB_AWAY = (253,198,63)
RGB_ONLINE = (146, 195, 83)
RGB_BUSY = (196,49,75)

def selectText(x,y):
    from pynput.mouse import Controller, Button
    mouse = Controller()
    time.sleep(.200)
    mouse.position = (x,y)
    time.sleep(.200)
    mouse.press(Button.left)
    mouse.release(Button.left)

def locate_and_click(file_name, conf):
    b = pyautogui.locateOnScreen(file_name, grayscale=True, confidence =conf)

    if(b != None):
        x = b.left
        y = b.top
        selectText(x,y)

def locate(file_name, conf):
    b = pyautogui.locateOnScreen(file_name, grayscale=True, confidence =conf)

    if(b != None):
        return 1 #TRUE
    else:
        return 0 #FALSE

def getTeamsState():
    pixel = pyautogui.pixel(1347, 105)
    if(RGB_AWAY == pixel):
        return "AWAY"
    elif(RGB_BUSY == pixel):
        return "BUSY"
    elif(RGB_ONLINE == pixel):
        return "ONLINE"
    else:
        return "NOT_A_STATE"
            


def main():
    from pynput.keyboard import Key, Controller
    keyboard = Controller()
    
    locate_and_click('img/teams.png', 1)
    
    while(1):
        state = getTeamsState()
        print(state)
            
        if(state == "AWAY"):
            if(locate('img/teams.png', 1) == 0):
                locate_and_click('img/chat.png',.8)
                time.sleep(2.5)
                locate_and_click('img/teams.png',.8)
        time.sleep(5)
            
    sys.exit(0)
    
main()

#pyautogui.mouseInfo()
##image = pyautogui.screenshot()
##image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
##cv2.imwrite("in_memory_to_disk.png", image)


