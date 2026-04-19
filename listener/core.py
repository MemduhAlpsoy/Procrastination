import json
import time
from .process_scanner import check_processes
from .window_scanner import check_windows

def load_config():
    with open('config.json', 'r', encoding='utf-8') as f:
        return json.load(f)
    
def start_listener(process_caught, window_caught):
    config = load_config()
    processes = config.get("target_processes", [])
    windows = config.get("target_windows", [])
    
    while True:
        captured_process = check_processes(processes)
        captured_window = check_windows(windows)
        if (captured_process):
            process_caught(captured_process)
        if (captured_window):
            window_caught(captured_window)

        time.sleep(2)