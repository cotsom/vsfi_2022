import time
import numpy
from PIL import Image
from numpy import array
import requests
from threading import Thread

def draw_skull():
    im_1 = Image.open("1622008093_3-phonoteka_org-p-cherep-piksel-art-krasivo-3.jpg")
    ar = array(im_1)
    while True:
        for (x,y) in numpy.ndenumerate(ar):
            r = requests.post(f"https://pixel.vsfi.org/api/v1/pixel", json={"x": x[0], "y" : x[1], "color": "#ff0000" if
                                                                                y == 255 else "#000000"})
threads = []
for i in range(100):
    th = Thread(target=draw_skull)
    th.start()
    threads.append(th)