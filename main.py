import pyautogui
import time
import sys
from datetime import datetime

pyautogui.FAILSAFE = False
numMin = None

if ((len(sys.argv)<2) or sys.argv[1].isalpha() or int(sys.argv[1])<1):
    numMin = 1

else:
    numMin = int(sys.argv[1])

while(True):
    x = 0
    time.sleep(numMin * 60)
    for i in range:
        pyautogui.moveTo(0, i*4)
    pyautogui.moveTo(1,1)
    for i in range(0,3):
        pyautogui.press("shift")
    print(f"Movement made at {datetime.now().time()}")