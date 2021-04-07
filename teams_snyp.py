import cv2
#import numpy as np
import pyautogui
#import imutils
#from matplotlib import pyplot as plt

from pynput import mouse
from pynput import keyboard
import time
import sys

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
  

def check_teams_state(file_name, conf):
    b = pyautogui.locateOnScreen(file_name, grayscale=True, confidence =conf)

    if(b != None):
        print("The user is currently online")
        return "OFFLINE"
    else:
        print("The user is currently offline")
        return "ONLINE"


def main():
    image = pyautogui.screenshot()
    pix = pyautogui.pixel(1347, 105)
    print(pix)
    pyautogui.mouseInfo()
    sys.exit(0)
    
main()

##image = pyautogui.screenshot()
##image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
##cv2.imwrite("in_memory_to_disk.png", image)


