import requests
import matplotlib.pyplot as plt
from datetime import date
from datetime import datetime
import re
url = "http://192.168.1.232/"
url1 = "http://192.168.1.232/output.txt"
today = date.today()
now = datetime.now()
hour = int(today.strftime("%I"))
current_time = now.strftime("%H:%M")
r = requests.get(url)
r1 = requests.get(url1)
r2 = re.findall(r"(\d+\.\d+)",r1.text)
x1 =  current_time
y1 = float(r2[0])
plt.scatter(x1, y1, label= "Teplota", color= "red",marker= "+", s=30)
y2 = float(r2[1])
plt.scatter(x1, y2, label= "Vlhkost", color= "green",marker= "+", s=30)
plt.xlabel('x - Hodiny')
plt.ylabel('y - Hodnota')
plt.title('Zmena vlhkosti a teploty v priebehu dna')
plt.legend()
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
plt.show()

#print(r2)
#print(r1)