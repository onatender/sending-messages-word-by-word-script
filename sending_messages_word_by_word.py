import pyperclip
import keyboard
import pyautogui
import time

def select_all():
    pyautogui.hotkey('ctrl', 'a')

def cut_text():
    pyautogui.hotkey('ctrl', 'x')

def on_enter():
    select_all()  
    cut_text()  
    text = pyperclip.paste() 
    if text:
        words = text.split()  
        for word in words:
            print(word)  
            pyperclip.copy(word)
            keyboard.write(word)  
            keyboard.press_and_release('enter')  
            time.sleep(.5)

keyboard.add_hotkey('pagedown', on_enter)

print("Script çalışıyor... 'Page Down' tuşuna basarak test edebilirsiniz.")
keyboard.wait('esc')  
