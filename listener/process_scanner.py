import psutil

def check_processes(target_processes):
    iter = psutil.process_iter(['name', 'pid'])
    for proc in iter:
        for target in target_processes:
            if (proc.info['name'] is not None and proc.info['name'].lower() == target.lower()):
                return target, proc.info['pid']
    
    return False