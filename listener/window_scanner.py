import pygetwindow

def check_windows(target_windows):
    windows = pygetwindow.getAllTitles()
    for window in windows:
        for target in target_windows:
            if (target.lower() in window.lower()):
                return window
            
    return False