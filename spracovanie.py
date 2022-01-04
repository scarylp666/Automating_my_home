import requests
import matplotlib.pyplot as plt
from datetime import date
from datetime import datetime
import numpy as np
import re
tempreature = open("saved_dataT.txt","r")
humidity = open("saved_dataH.txt","r")
time = open("saved_time.txt","r")
tempreature1 = list(np.float_(tempreature.read().split(",")[:-1]))
humidity1 = list(np.float_(humidity.read().split(",")[:-1]))
time1 = (time.read().split(",")[:-1])
plt.plot(time1, tempreature1, label = "teplota",marker='o', markerfacecolor='red', markersize=5)
plt.plot(time1, humidity1, label = "vlhkost",marker='o', markerfacecolor='green', markersize=5)
plt.xlabel('x - Hodiny')
plt.ylabel('y - Hodnota')
plt.title('Zmena vlhkosti a teploty v priebehu dna')
plt.legend()
plt.grid(color = 'purple', linestyle = '--', linewidth = 0.5)
plt.show()
