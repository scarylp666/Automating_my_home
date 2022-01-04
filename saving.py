import time
import re
import requests
url1 = "http://192.168.1.232/output.txt"
r1 = requests.get(url1)
r2 = re.findall(r"(\d+\.\d+)",r1.text)
file1 = open("saved_data.txt","w")
for i in range (50):
	file1.write(str(r2[0]))
	file1.write(",")
	time.sleep(20)