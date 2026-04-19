import json
import time
from .process_scanner import check_processes
from .window_scanner import check_windows

def load_config():
    with open('config.json', 'r', encoding='utf-8') as f:
        return json.load(f)
    
def start_listener():
    config = load_config()
    processes = config.get("target_processes", [])
    windows = config.get("target_windows", [])
    
    while True:
        captured_process = check_processes(processes)
        captured_window = check_windows(windows)
        if (captured_process):
            print(captured_process)
        if (captured_window):
            print(captured_window)

        time.sleep(2)