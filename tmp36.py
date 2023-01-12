import machine
import utime

class GetTemp:
    """Read the temp from a TMP36 sensor"""

    def __init__(self, adc, ref_voltage=3.3):
        """Init"""
        self.sensor_temp = machine.ADC(adc)
        self.convert = ref_voltage * 1000 / 65535
        self.temperature = 0

    def get_temp(self):
        """Read the Internal Temp Sensor"""
        millivolts = self.get_raw() * self.convert
        self.temperature = (millivolts - 550) / 10
        return self.temperature

    def get_temp_f(self):
        """Get Temp in Fahrenheit"""
        return (self.get_temp() * 1.8) + 32
    
    def get_raw(self):
        return self.sensor_temp.read_u16()

    def get_temp_str(self):
        return "{:.1f} C".format(self.get_temp())


if __name__ == "__main__":
    temp = GetTemp(2)
    while True:
        print("%.4f C, %.4f F" % (temp.get_temp(), temp.get_temp_f()))
        print(temp.get_temp_str())
        utime.sleep(2)
