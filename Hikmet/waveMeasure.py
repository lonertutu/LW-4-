import waveFunctions as b
import spidev
import time
import RPi.GPIO as GPIO
import numpy as np
import matplotlib.pyplot as plt


spi = spidev.SpiDev()
b.initSpiAdc()
c =[]
start = time.time()
for i in range(1000):
    a = b.getAdc()
    print(a)
    time.sleep(0.015)
    c.append(a)
finish = time.time()

b.saveMeasures(c, 1000, 1, start, finish)