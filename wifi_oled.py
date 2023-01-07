import machine
import ssd1306
import time
import network

f = open("wifi.txt", "r")
wifi_details = f.readlines()
f.close()

ssid = wifi_details[0].split(" ")[0]
password = wifi_details[0].split(" ")[1]

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

# Wait for connect or fail
print("Connection to", ssid)
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print("waiting for connection...")
    time.sleep(1)

# Handle connection error
if wlan.status() != 3:
    raise RuntimeError("network connection failed")
else:
    print("connected")
    status = wlan.ifconfig()
    print("ip = " + status[0])

sda = machine.Pin(0)
scl = machine.Pin(1)
i2c = machine.I2C(0, sda=sda, scl=scl, freq=400000)
print("Scanning for IC2 devices")
devices = i2c.scan()
if len(devices) == 0:
    print("No i2c Devices found.")
else:
    for device in devices:
        print("Decimal address: ", device, " | Hexa address: ", hex(device))
    display = ssd1306.SSD1306_I2C(128, 64, i2c)
    display.rect(0, 0, 128, 16, 1)
    display.rect(0, 17, 127, 46, 1)
    display.text(status[0], 1, 2)
    display.text("Hello World", 1, 18)
    display.show()
