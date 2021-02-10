import Adafruit_DHT 
import requests
import os
import sched, time

API_URL = os.environ.get('API_URL')

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

s = sched.scheduler(time.time, time.sleep)

def measure(sc):
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    print(humidity, temperature)
    s.enter(60, 1, do_something, (sc,))

s.enter(60, 1, do_something, (s,))
s.run()
