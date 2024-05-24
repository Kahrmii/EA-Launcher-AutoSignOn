import pyautogui
import keyboard
import win32api, win32con
import time
import pyscreeze
import base64
from io import BytesIO
from PIL import Image

pyscreeze.USE_IMAGE_NOT_FOUND_EXCEPTION = False

def leftclick(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
def rightclick(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)

def read_line_from_file(file_path, line_number):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if 1 <= line_number <= len(lines):
                return lines[line_number - 1].rstrip('\n')
            else:
                print(f"Line number {line_number} is out of range.")
                return None
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

file_path = 'README.txt'

img = "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"
img_data = base64.b64decode(img)
img = Image.open(BytesIO(img_data))
    
while keyboard.is_pressed('q') == False:
    time.sleep(0.5)
    cord = pyautogui.locateCenterOnScreen(img, confidence=0.9)
    if cord:
        x,y = cord
        time.sleep(int(read_line_from_file(file_path, 3)))
        leftclick(x,y)
        time.sleep(0.1)
        keyboard.write(read_line_from_file(file_path, 1))
        keyboard.press_and_release('tab')
        keyboard.write(read_line_from_file(file_path, 2))
        keyboard.press_and_release('Enter')
        exit()