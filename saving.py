from datetime import date
from datetime import datetime
import time
import re
import requests
url1 = "http://192.168.1.232/output.txt"
with open("saved_dataT.txt","w") as file1:
	with open("saved_dataH.txt","w") as file2:
		with open("saved_time.txt","w") as file3:
			for i in range (24):
				r1 = requests.get(url1)
				r2 = re.findall(r"(\d+\.\d+)",r1.text)
				today = date.today()
				now = datetime.now()
				hour = int(today.strftime("%I"))
				current_day = now.strftime("%H:%M:%S")
				file1.write(str(r2[0]))
				file2.write(str(r2[1]))
				file3.write(current_day)
				file1.write(",")
				file2.write(",")
				file3.write(",")
				time.sleep(3600)
