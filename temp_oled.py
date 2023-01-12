import machine
import ssd1306
import utime
import network
import tmp36
import internal_temp
import rp2

def wifi_connection(file, max_try, country):
    """Connect to Wifi"""

    ip = "Not Connected"
    rp2.country(country)
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
    max_wait = max_try
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


def update_display(display, lines, y_offset=2):
    """Update the Display"""
    clear_display(display)
    frames = [[0,0,128,16,1],[0,17,127,46,1]]
    draw_frames(display, frames)
    y = y_offset
    for line in lines:
        display.text(line, 1, y)
        y += 16
    display.show()

def clear_display(display):
    """Clear the display"""
    display.fill(0)
    display.show()

def draw_frames(display, frames):
    """Draw frames on display"""
    for frame in frames:
        display.rect(frame[0], frame[1], frame[2], frame[3], frame[4])


if __name__ == "__main__":
    sda = machine.Pin(0)
    scl = machine.Pin(1)
    display = setup_display(sda, scl)
    update_display(display, ["Connecting..."])
    ip_address = wifi_connection("wifi.txt", 10, "UK")
    lines = [ip_address, "Hello", "World"]
    update_display(display, lines)
    tmp36 = tmp36.GetTemp(2)
    internal = internal_temp.GetTemp()
    while True:
        int_tmp = "Int " + internal.get_temp_str()
        ext_tmp = "Ext " + tmp36.get_temp_str()
        lines = [ip_address, int_tmp, ext_tmp]
        print(int_tmp, ext_tmp)
        update_display(display,lines)
        utime.sleep(5)        

