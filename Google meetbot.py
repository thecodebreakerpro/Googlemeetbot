#THIS IS MADE BY NEXA CODE.
from cgitb import text
from email.policy import default
from turtle import title
import pyautogui
import time

meetingID = pyautogui.prompt(text ='Enter your meeting ID',title = 'Meeting ID',default='')
time.sleep(1)
pyautogui.press('win',interval =0.5)
time.sleep(1)
pyautogui.typewrite('brave',interval = 0.5)
time.sleep(1)
pyautogui.press('enter',interval=0.5)
time.sleep(13)
pyautogui.typewrite('https://meet.google.com/?authser=0',interval=0.3)
time.sleep(1)
pyautogui.press('enter',interval = 0.5)
time.sleep(13)
pyautogui.click(250,520)
time.sleep(1)
pyautogui.typewrite(meetingID,interval = 0.2)
time.sleep(1)
pyautogui.press('enter',interval = 0.2)
time.sleep(9)
pyautogui.click(400,570)
time.sleep(2)
pyautogui.click(500,570)
time.sleep(2)
pyautogui.alert(text = 'We are entering the meeting',title='Info',button = 'ok')
time.sleep(1)
pyautogui.click(990,440)
print("Asked to join the meeting")