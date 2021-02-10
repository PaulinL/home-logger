import Adafruit_DHT 
import requests
import os
import sched, time

API_URL = os.environ.get('API_URL')

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

SECOND_BETWEEN_MEASURE = 20

s = sched.scheduler(time.time, time.sleep)

def measure(sc):
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    print(humidity, temperature)
    requests.post(API_URL, data={
        measurements: buildMeasurements(temperature, humidity)
    })
    s.enter(SECOND_BETWEEN_MEASURE, 1, measure, (sc,))

s.enter(SECOND_BETWEEN_MEASURE, 1, measure, (s,))
s.run()

def buildMeasurements(temperature, humidity):
    return [{
    			"measurement": "temperature_living_room_in",
    			"fields": {
    				"value": temperature
    			}
    		},
    		{
    			"measurement": "humidity_living_room_in",
    			"fields": {
    				"value": humidity
    			}
    		}]
