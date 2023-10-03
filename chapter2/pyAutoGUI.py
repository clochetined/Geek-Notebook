import pyautogui
import time

pyautogui.press('win')
pyautogui.write('memo')
time.sleep(1)
pyautogui.press('enter')
time.sleep(2)
pyautogui.write('Welcome to geek salon!', interval=0.05)
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')
for num in range(10):
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
time.sleep(1)
pyautogui.hotkey('ctrl', 'a')
pyautogui.press('del')
pyautogui.hotkey('alt', 'f4')