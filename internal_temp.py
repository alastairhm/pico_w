import machine
import utime


class GetInternalTemp:
    """Read the internal temp sensor"""

    def __init__(self):
        """Init"""
        self.sensor_temp = machine.ADC(4)
        self.convert = 3.3 / 65535
        self.temperature = 0

    def get_temp(self):
        """Read the Internal Temp Sensor"""
        reading = self.sensor_temp.read_u16() * self.convert
        self.temperature = 27 - (reading - 0.706) / 0.001721
        return self.temperature


if __name__ == "__main__":
    temp = GetInternalTemp()
    while True:
        print(temp.get_temp())
        utime.sleep(1)
