from listener import start_listener
from enforcer import freeze_process, resume_process, minimize_window
from generator import derivative
from gui import ask_question
import psutil 
import time

app_immunity_dictionary = {}
window_immunity_dictionary = {}

minute = 60
gaming_time = 30 * minute
internet_time = 30 * minute

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
        if not is_correct:
            psutil.Process(pid).kill()
        else:
            app_immunity_dictionary[app_name] = time.time()
    finally:
        resume_process(pid)

def handle_window(captured_window):
    window_title = captured_window
    print(window_title)
    if (window_title in window_immunity_dictionary):
        passed_time = time.time() - window_immunity_dictionary[window_title]
        if (passed_time < internet_time):
            return
    minimize_window(captured_window)
    question,answer = derivative()
    is_correct = ask_question(question,answer,window_title)
    
    if (is_correct):
        window_immunity_dictionary[window_title] = time.time()

start_listener(handle_process,handle_window)