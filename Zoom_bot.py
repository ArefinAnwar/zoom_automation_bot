import pyautogui
import time
import subprocess

meeting_id = input("Enter Meeting ID: ")
meeting_password = input("Enter Meeting Password: ")
print("Joining meeting", end="")
for i in range(0, 5):
    print(".", end="")         # printing Joining meeting....
    time.sleep(0.5)
try:
    screenWidth, screenHeight = pyautogui.size()
    pyautogui.position()

    subprocess.call(['C:\\Users\\User\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe'])
    #pyautogui.hotkey('win', 'r')
    # pyautogui.press('enter')
    time.sleep(2)
    u = "C:/Users/User/AppData/Roaming/Zoom/bin/Zoom.exe"
    '''pyautogui.moveTo(208, 622)  #Clicking run textbox
    pyautogui.click()
    time.sleep(2)
    pyautogui.write(u)
    pyautogui.press('enter')
    #pyautogui.moveTo(761, 748)   #opening zoom
    #pyautogui.click()
    time.sleep(10)
    '''
    pyautogui.moveTo(591, 293)  # Clicking join
    pyautogui.click()

    pyautogui.moveTo(618, 324)  # Clicking meeting id textbox
    pyautogui.click()

    time.sleep(6)
    pyautogui.write(meeting_id)  # typing meeting id

    pyautogui.moveTo(713, 494)  # clicking  join
    pyautogui.click()

    pyautogui.moveTo(597, 329)  # Clicking meeting password textbox
    pyautogui.click()

    time.sleep(3)
    pyautogui.write(meeting_password)  # Typing meeting textbox

    pyautogui.moveTo(704, 499)  # Cicking join
    pyautogui.click()

    print("\nJoined meeting!")  # Printing joined meetng
except:
    print("Failed to join meeting try again!")
