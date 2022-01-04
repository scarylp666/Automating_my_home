import requests
import matplotlib.pyplot as plt
from datetime import date
from datetime import datetime
import re
tempreature = open("saved_dataT.txt","r")
humidity = open("saved_dataH.txt","r")
time = open("saved_time.txt","r")
#today = date.today()
#now = datetime.now()
#hour = int(today.strftime("%I"))
#current_time = now.strftime("%H:%M")
#r = requests.get(url)
#r1 = requests.get(url1)
#2 = re.findall(r"(\d+\.\d+)",r1.text)
x1 = str(time)
y1 = str(tempreature)
plt.scatter(x1, y1, label= "Teplota", color= "red",marker= "+", s=30)
y2 = str(humidity)
plt.scatter(x1, y2, label= "Vlhkost", color= "green",marker= "+", s=30)
plt.xlabel('x - Hodiny')
plt.ylabel('y - Hodnota')
plt.title('Zmena vlhkosti a teploty v priebehu dna')
plt.legend()
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
plt.show()

#print(r2)
#print(r1)
