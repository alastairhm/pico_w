import machine
import ssd1306
import utime
import network
import rp2
from library import internal_temp, tmp36, wifi

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
    
    f = open("wifi.txt", "r")
    wifi_details = f.readline()
    f.close()
    credentials = {"ssid": wifi_details.split(" ")[0], "password" : wifi_details.split(" ")[1] }    
    
    wifi_instance = wifi.Wifi(credentials, 10, "UK")
    ip_address = wifi_instance.get_ip()
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

