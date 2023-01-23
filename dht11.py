"""
Temperature and Humidity with DHT11
https://docs.micropython.org/en/latest/esp8266/tutorial/dht.html
"""
import dht
import machine
import time

d = dht.DHT11(machine.Pin(16))

while True:
    d.measure()
    print("Temperature :", d.temperature(), "C")
    print("Humidity    :", d.humidity(), "%")
    time.sleep(5)
