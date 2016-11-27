import pyautogui
import time
print('Press Ctrl+C to Exit')

try:
    while True:
        # x, y = pyautogui.position()
        # positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        # print(positionStr, end='')
        # print('\b' * len(positionStr), end='', flush=True)
        print(pyautogui.position())
        time.sleep(1)

except KeyboardInterrupt:
    print('\nDone')
