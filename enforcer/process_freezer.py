import psutil

def freeze_process(pid):
    try:
        target = psutil.Process(pid)
        target.suspend()
        return True
    except(psutil.NoSuchProcess, psutil.AccessDenied):
        print("İşlem bulunamadı veya izin verilmedi")
        return False
    
def resume_process(pid):
    try:
        target = psutil.Process(pid)
        target.resume()
        return True
    except(psutil.NoSuchProcess, psutil.AccessDenied):
        print("İşlem bulunamadı veya izin verilmedi")
        return False