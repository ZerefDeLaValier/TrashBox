import psutil

def find_process_pid(process_name):
    for process in psutil.process_iter():
        if process.name() == process_name:
            return process.pid
pid = find_process_pid("javaw.exe")
print(pid)