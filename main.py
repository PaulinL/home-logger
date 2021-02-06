import Adafruit_DHT 
from influxdb import InfluxDBClient

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

client = InfluxDBClient(host='plambert.dev', port=8086, username='admin', password='admin', database='db0')

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    print(humidity, temperature)
    point = {
        "measurement": "measurements",
        "tags": {
            "Area": "Paris",
            "Location": "Paris",
            "ClientIP": "192.168.1.1"
        },
        "fields": {
            "humidity": humidity,
            "temperature": temperature
        }
    }
    client.write_points([point])


