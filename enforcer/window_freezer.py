import pygetwindow

def minimize_window(window_title):
    title_array = pygetwindow.getWindowsWithTitle(window_title)
    if (title_array):
        for window in title_array:
            try:
                window.minimize()
            except Exception:
                print("Minimize edilemedi!")
                continue
        
        return True
    
    return False