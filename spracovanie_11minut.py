import requests
import matplotlib.pyplot as plt
from datetime import date
from datetime import datetime
import numpy as np
import re
#urlT = "http://192.168.194.12/saved_dataT.txt"
#urlH = "http://192.168.194.12/saved_dataH.txt"
#url = "http://192.168.194.12/saved_time.txt"
url1 = "http://192.168.194.12/output.txt"
i=0
with open("saved_dataT.txt","w") as tempreature:
	with open("saved_dataH.txt","w") as humidity:
		with open("saved_time.txt","w") as time:
			while i < 12:
				r1 = requests.get(url1)
				r2 = re.findall(r"(\d+\.\d+)",r1.text)
				today = date.today()
				now = datetime.now()
				hour = int(today.strftime("%I"))
				current_day = now.strftime("%d.%m.%y-%H:%M")
				if len(r2) > 0:
					tempreature.write(str(r2[0]))
					humidity.write(str(r2[1]))
					time.write(current_day)
					tempreature.write(",")
					humidity.write(",")
					time.write(",")
					i+=1
				else:
					continue
				time.sleep(60)
			#tempreature = requests.get(urlT)
			#humidity = requests.get(urlH)
			#time = requests.get(url)
			tempreature1 = list(np.float_(tempreature.read().split(",")[:-1]))
			humidity1 = list(np.float_(humidity.read().split(",")[:-1]))
			time1 = (time.read().split(",")[:-1])
			#tempreature1 = list(np.float_(tempreature.text.split(",")[:-1]))
			#humidity1 = list(np.float_(humidity.text.split(",")[:-1]))
			#time1 = (time.text.split(",")[:-1])
			plt.plot(time1, tempreature1, label = "teplota",marker='o', markerfacecolor='red', markersize=5)
			plt.plot(time1, humidity1, label = "vlhkost",marker='o', markerfacecolor='green', markersize=5)
			plt.xlabel('x - Hodiny')
			plt.xticks(rotation = -45)
			plt.ylabel('y - Hodnota')
			plt.title('Zmena vlhkosti a teploty za poslednych 12 minut')
			plt.legend()
			plt.grid(color = 'purple', linestyle = '--', linewidth = 0.5)
			plt.savefig("test.png",bbox_inches='tight',dpi=100)
			plt.show()
