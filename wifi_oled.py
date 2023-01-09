import machine
import ssd1306
import time
import network

def wifi_connection(file, max):
    """Connect to Wifi"""

    ip = "Not Connected"
    f = open(file, "r")
    wifi_details = f.readline()
    f.close()

    ssid = wifi_details.split(" ")[0]
    password = wifi_details.split(" ")[1]

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    # Wait for connect or fail
    print("Connection to", ssid)
    max_wait = max
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
        ip = wlan.ifconfig()[0]
        print("ip = " + ip)
    return ip

def setup_display(sda, scl, x=128, y=64, freq=400000):
    """Setup I2C Display"""
    i2c = machine.I2C(0, sda=sda, scl=scl, freq=freq)
    return ssd1306.SSD1306_I2C(x, y, i2c)

def update_display(display, lines):
    """Update the Display"""
    display.fill(0)
    display.show()
    display.rect(0, 0, 128, 16, 1)
    display.rect(0, 17, 127, 46, 1)
    y = 2
    for line in lines:
        display.text(line,1,y)
        y +=16
    display.show()

if __name__ == "__main__":
    sda = machine.Pin(0)
    scl = machine.Pin(1)
    display = setup_display(sda, scl)
    update_display(display,["Connecting..."])
    ip_address = wifi_connection("wifi.txt", 10)
    lines = [ip_address, "Hello","World"]
    update_display(display, lines)

