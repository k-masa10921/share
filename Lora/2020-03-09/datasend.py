import elasticprocess 
import glob,os
import time
#es = elasticprocess.es

while True:
	files = glob.glob("/home/pi/wifidata/*")
	for file in files:
		elasticprocess.sendfile(file,"static")
		os.remove(file)
	time.sleep(2)
