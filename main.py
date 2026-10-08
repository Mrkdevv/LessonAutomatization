import time
import webbrowser
from time import sleep

import pyautogui
from slovari import all_days
from datetime import datetime

buttons = ["join.png" , "zapit.png"]

def find_button(image):
    try:
        pos = pyautogui.locateCenterOnScreen(image, confidence=0.8)
    except pyautogui.ImageNotFoundException:
        return None
    return pos

def connect_to_lesson(url):
    if not url:
        return
    if "zoommtg" in url:
        webbrowser.open(url)
    elif "meet.google.com" in url:
        webbrowser.open(url)
        time.sleep(2)
        for i in range(11):
            for j in buttons:
                temp = find_button(j)
                if temp is not None:
                    pyautogui.click(temp)
                    return
    else:
        print("Not a good url")
def day_today():
    return datetime.today().weekday()
def time_now():
    return datetime.now().strftime("%H:%M")
open_one_lesson = set()

while True:
    today_lessons = all_days.get(day_today())
    if today_lessons is not None:
        url_for_lesson = today_lessons.get(time_now())
        if url_for_lesson is not None:
            key = datetime.now().date() , time_now()
            if key not in open_one_lesson:
                open_one_lesson.add(key)
                connect_to_lesson(url_for_lesson)
    time.sleep(20)

