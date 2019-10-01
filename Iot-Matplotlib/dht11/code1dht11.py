import Adafruit_DHT
import datetime
from time import sleep, strftime, time
import csv

print("hi")

try:
    while True:
        row = []
        humidity, temperature = Adafruit_DHT.read_retry(11,4)
        row.append(temperature)
        row.append(humidity)
        row.append(str(datetime.datetime.now()))
        print(row)
        with open('reading.csv','a')as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
finally:
    csvFile.close()
