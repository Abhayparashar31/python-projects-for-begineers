import pyautogui,time
time.sleep(5)
f = open("data.txt",'r')
for word in f:
    pyautogui.tywriter(word)
    pyautogui.press("enter")
