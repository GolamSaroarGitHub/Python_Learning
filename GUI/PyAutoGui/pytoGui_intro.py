import pyautogui

#
# for i in range(5):
#       pyautogui.moveTo(100, 100, duration=1)
#       pyautogui.moveTo(200, 100, duration=1)
#       pyautogui.moveTo(200, 200, duration=1)
#       pyautogui.moveTo(100, 200, duration=1)




for i in range(5):
      pyautogui.moveRel(10, 10, duration=1)
      pyautogui.moveRel(20, 10, duration=1)
      pyautogui.moveRel(20, 20, duration=1)
      pyautogui.moveRel(10, 20, duration=1)
