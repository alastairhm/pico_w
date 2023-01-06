import machine
import ssd1306

sda=machine.Pin(0)
scl=machine.Pin(1)
i2c=machine.I2C(0,sda=sda, scl=scl, freq=400000)
print("Scanning for IC2 devices")
devices = i2c.scan()
if len(devices) == 0:
    print("No i2c Devices found.")
else:
    for device in devices:
        print("Decimal address: ",device," | Hexa address: ",hex(device))
    display = ssd1306.SSD1306_I2C(128, 64, i2c)
    display.text("Hello", 0, 0)
    display.text("World", 0, 16)
    display.show()
        

        