import requests
import time
from threading import Thread

def draw():
    while True:
        for i in range(80):
            for j in range(100):
                #th = Thread(target=sleepMe, args=(i, ))
                r = requests.post(f"https://pixel.vsfi.org/api/v1/pixel", json={"x": 80-i, "y" : 80-j, "color": "#000000"})
                #time.sleep(6)
threads = []

if __name__ == '__main__':
    for i in range(100):
        th = Thread(target=draw)
        th.start()
        threads.append(th)
        time.sleep(3)
    

