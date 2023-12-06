import webbrowser
import psutil
def open_google():
    webbrowser.open("google.com", new=0, autoraise=True)

def close_google(process_name):
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == process_name:
            try:
                pid = process.info['pid']
                p = psutil.Process(pid)
                p.terminate()
            except psutil.NoSuchProcess:
                print(f"Процесс {process_name} не найден.")