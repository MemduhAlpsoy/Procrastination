from listener import start_listener,load_config
from enforcer import freeze_process, resume_process, minimize_window
from generator import derivative
from gui import ask_question
import psutil
import pygetwindow
import pyautogui
import time
import json

app_immunity_dictionary = {}
window_immunity_dictionary = {}

minute = 60
gaming_time = 30 * minute
internet_time = 30 * minute

config = load_config()
forbidden_windows = config.get("target_windows", [])

def handle_process(captured_process):
    try:
        pid = captured_process[1]
        app_name = captured_process[0]
        if (app_name in app_immunity_dictionary):
            passed_time = time.time() - app_immunity_dictionary[app_name]
            if (passed_time < gaming_time):
                return
        freeze_process(pid)
        question,answer = derivative()
        is_correct = ask_question(question,answer,app_name)
        if is_correct == "failed" or is_correct == "quit":
            psutil.Process(pid).kill()
        else:
            app_immunity_dictionary[app_name] = time.time()
    finally:
        resume_process(pid)

def handle_window(captured_window):
    window_title = captured_window
    target_window = ""
    for target in forbidden_windows:
        if target.lower() in captured_window.lower():
            target_window = target
    print(window_title)
    if not target_window:
        return
    if (target_window in window_immunity_dictionary):
        passed_time = time.time() - window_immunity_dictionary[target_window]
        if (passed_time < internet_time):
            return
    minimize_window(captured_window)
    question,answer = derivative()
    is_correct = ask_question(question,answer,target_window)
    
    if (is_correct == "solved"):
        window_immunity_dictionary[target_window] = time.time()
        

    if (is_correct == "failed" or is_correct == "quit"):
        window_objs = pygetwindow.getWindowsWithTitle(captured_window)
        if (window_objs):
            window_obj = window_objs[0]
            window_obj.restore()
            window_obj.activate()
            
            time.sleep(0.5)

            pyautogui.hotkey('ctrl', 'w')
        
start_listener(handle_process,handle_window)