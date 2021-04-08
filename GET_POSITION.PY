import pyautogui
import time
time.sleep(4)

screenWidth, screenHeight = pyautogui.size() # Returns two integers, the width and height of the screen. (The primary monitor, in multi-monitor setups.)
print(pyautogui.position()) # Returns two integers, the x and y of the mouse cursor's current position.

