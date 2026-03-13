#Import of libraries
import pyautogui
import time
#Program will determine what position the mouse is in and adjust accordingly
while True:
    initial_mouse = pyautogui.position()
    time.sleep(0.5)
    final_mouse = pyautogui.position()
    print(initial_mouse)
    print(final_mouse)
    if initial_mouse != final_mouse:
        pyautogui.hotkey("alt","tab")
    else:
        exit
