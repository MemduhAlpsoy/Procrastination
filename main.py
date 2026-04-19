from listener import start_listener
from enforcer import freeze_process, resume_process, minimize_window
import time

def handle_process(captured_process):
    try:
        pid = captured_process[1]
        freeze_process(pid)
        print("5 saniyelik dondurma")
        time.sleep(5)
        resume_process(pid)
    finally:
        resume_process(pid)

def handle_window(captured_window):
    minimize_window(captured_window)
    print("Pencere minimize edildi")

start_listener(handle_process,handle_window)