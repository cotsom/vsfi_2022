import requests
import time
from threading import Thread

def draw(data):
    for j in range(50):
        r = requests.post(f"https://pixel.vsfi.org/api/v1/pixel", json={"x": data, "y" : j, "color": "#000000"}, verify=False)
        print(r.text)
threads = []

if __name__ == '__main__':
    for i in range(500):
        th = Thread(target=draw, args=(i, ))
        th.start()
