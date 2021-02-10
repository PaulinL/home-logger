import Adafruit_DHT 
import requests
import os
import sched, time
import json

API_URL = os.environ.get('API_URL')
print('Sending data  to ' + API_URL)

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

SECOND_BETWEEN_MEASURE = 60

s = sched.scheduler(time.time, time.sleep)

headers = {
    'Content-Type': 'application/json'
}

def buildMeasurements(temperature, humidity):
    return {
		"measurements": [{
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
	  }

def measure(sc):
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    print(humidity, temperature)
    print(json.dumps(buildMeasurements(temperature, humidity)))
    requests.post(API_URL, headers=headers, data=json.dumps(buildMeasurements(temperature, humidity)))
    s.enter(SECOND_BETWEEN_MEASURE, 1, measure, (sc,))

s.enter(SECOND_BETWEEN_MEASURE, 1, measure, (s,))
s.run()
