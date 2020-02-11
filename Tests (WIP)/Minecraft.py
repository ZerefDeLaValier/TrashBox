import shutil
import os
import psutil
import time

dir = os.environ["APPDATA"] + "\\.tlauncher"
dir2 = os.environ["APPDATA"]+"\\Roaming"

def find_process_pid(process_name):
    for process in psutil.process_iter():
        if process.name() == process_name:
            return process.pid

def start():
    pid = find_process_pid("javaw.exe")
    if pid == None:
        os.startfile("TLauncher.exe")
        print("Запускаю лаунчер...")
        time.sleep(20)
        pid = find_process_pid("javaw.exe")
        print("Готово")
        print("Id процесса:"+ str(pid))
        delete(pid)
    else:
        print("Лаунчер уже запущен")
        print("Id процесса:"+ str(pid))
        delete(pid)

def delete(pid):
    exist = 1
    while exist == 1:
        if psutil.pid_exists(pid) == False:
            print("Майнкрафт закрыт!")
            exist = 0
    print("Удаление конфигов...")
    path = os.path.join(os.path.abspath(os.path.dirname(dir2)), '.tlauncher')
    shutil.rmtree(path)
    print("Готово")


try:
    print("Копирование конфигов...")
    shutil.copytree(r".tlauncher", dir)
    print("Готово")
    start()
except PermissionError:
    print("Вы Gay")
    print("Завершение работы")
except FileNotFoundError:
    print("Нет файла")
    print("Завершение работы")
except FileExistsError:
    print("Файл Существует")
    start()



