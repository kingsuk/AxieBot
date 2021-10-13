
import webbrowser
import pyautogui
import keyboard

webbrowser.open_new('https://marketplace.axieinfinity.com/axie/3550167')
#screenWidth, screenHeight = pyautogui.size()
while(True):
    buy_button_location = pyautogui.locateCenterOnScreen("buy.png")
    if buy_button_location:
        pyautogui.moveTo(1495, 279)
        pyautogui.click()
            
        #pyautogui.move(1495, 279)
