# pico_w

Raspberry Pi Pico W

Some example for Raspberry Pi Pico W with MicroPython

## Code Examples

* [blink.py](blink.py) basic on board LED blink
* [i2c_scan.py](i2c_scan.py) Scan the IC2 Bus and test OLED display.
* [led_matrix.py](led_matrix.py) Testing connecting a MAX7219 8x8 Led Matric to Pico.
* [library/internal_temp.py](library/internal_temp.py) Class to read the internal temperature sensor.
* [library/tmp36.py](library/tmp36.py) Class to read temperature from TMP36 sensor of the kind described here [datasheet](http://cdn.sparkfun.com/datasheets/Sensors/Temp/TMP35_36_37.pdf)
* [library/wifi.py](library/wifi.py) Class to setup Wifi Connection
* [mandelbrot.py](mandelbrot.py) ASCII Mandelbrot Set from [http://warp.povusers.org/MandScripts/python.html](http://warp.povusers.org/MandScripts/python.html)
* [mand_oled.py](mand_oled.py) Mandelbrot Set displayed to OLED [https://youtube.com/shorts/dqHLxU5frKw?feature=share](https://youtube.com/shorts/dqHLxU5frKw?feature=share)
* micropython-max7219 Sub Module of library for MAX7129 LED Matrix see below, upload to Pico.
* micropython-ssd1306 Sub Module of library for OLED see below, upload to Pico.
* [temp_oled.py](temp_oled.py) Outputing temperature and IP address to OLED display.
* [temps.py](temps.py) Example using the two temperature classes
* [wifi.py](wifi.py) testing WIFI connection, reads connections details from `wifi.txt` stored on the Pico format  single line "SSID PASSWORD".
* [wifi_oled.py](wifi_oled.py) Connect to wifi and display IP on OLED

## Related Blog Posts

* [SPI 1306 OLED](https://blog.0x32.co.uk/posts/pico2/)
* [Temperature Reading internal and external](https://blog.0x32.co.uk/posts/pico3/)
* [Mandelbrot Set ASCII and OLED](https://blog.0x32.co.uk/posts/pico4/)

## External Dependances

* Library for SSD1306 OLED [micropython-ssd1306](https://github.com/stlehmann/micropython-ssd1306)
* Library for MAX7219 LED Matrix [micropython-max7219](https://github.com/enchant97/micropython-max7219)
