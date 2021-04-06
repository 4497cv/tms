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
    print(b)
    if(b != None):
        x = b.left
        y = b.top
        selectText(x,y)
    else:
        print("Image file not located")

def check_teams_state(file_name, conf):
    b = pyautogui.locateOnScreen(file_name, grayscale=True, confidence =conf)
    print(b)
    if(b != None):
        return "OFFLINE"
    else:
        print("Image file not located")
        return "ONLINE"


def main():
    from pynput.keyboard import Key, Controller
    keyboard = Controller()
    locate_and_click('img/teams.png',.8)
    while(1):
        state = check_teams_state('img/cv.png', .8)
        if(state == "OFFLINE"):
            locate_and_click('img/chat.png',.8)
            time.sleep(2)
            locate_and_click('img/teams.png',.8)
        time.sleep(60)
            
    sys.exit(0)
    
main()

#pyautogui.mouseInfo()
##image = pyautogui.screenshot()
##image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
##cv2.imwrite("in_memory_to_disk.png", image)
#pyautogui.mouseInfo()

