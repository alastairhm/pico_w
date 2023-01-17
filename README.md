# pico_w

Raspberry Pi Pico W

Some example for Raspberry Pi Pico W with MicroPython

## Code Examples

* [blink.py](blink.py) basic on board LED blink
* [i2c_scan.py](i2c_scan.py) Scan the IC2 Bus and test OLED display.
* [library/internal_temp.py](library/internal_temp.py) Class to read the internal temperature sensor.
* [library/tmp36.py](library/tmp36.py) Class to read temperature from TMP36 sensor of the kind described here [datasheet](http://cdn.sparkfun.com/datasheets/Sensors/Temp/TMP35_36_37.pdf)
* [library/wifi.py](library/wifi.py) Class to setup Wifi Connection
* [mandelbrot.py](mandelbrot.py) ASCII Mandelbrot Set from [http://warp.povusers.org/MandScripts/python.html](http://warp.povusers.org/MandScripts/python.html)
* [mand_oled.py](mand_oled.py) Mandelbrot Set displayed to OLED [https://youtube.com/shorts/dqHLxU5frKw?feature=share](https://youtube.com/shorts/dqHLxU5frKw?feature=share)
* [ssd1306.py](ssd1306.py) Copy of library for OLED from [https://github.com/stlehmann/micropython-ssd1306](https://github.com/stlehmann/micropython-ssd1306)
* [temp_oled.py](temp_oled.py) Outputing temperature and IP address to OLED display.
* [temps.py](temps.py) Example using the two temperature classes
* [wifi.py](wifi.py) testing WIFI connection, reads connections details from `wifi.txt` stored on the Pico format  single line "SSID PASSWORD".
* [wifi_oled.py](wifi_oled.py) Connect to wifi and display IP on OLED

## Related Blog Posts

* [SPI 1306 OLED](https://blog.0x32.co.uk/posts/pico2/)
* [Temperature Reading internal and external](https://blog.0x32.co.uk/posts/pico3/)
* [Mandelbrot Set ASCII and OLED](https://blog.0x32.co.uk/posts/pico4/)

