import network
import rp2
import time

class Wifi():
    """Setup Wifi Connection on Pico W"""

    def __init__(self, credentials, max_try, country):
        """Connect to Wifi"""

        self.ip = "Not Connected"
        self.ifconfig = []
        self.status = 0
        rp2.country(country)

        self.ssid = credentials["ssid"]
        password = credentials["password"]

        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(self.ssid, password)

        # Wait for connect or fail
        print("Connection to", self.ssid)
        max_wait = max_try
        while max_wait > 0:
            if wlan.status() < 0 or wlan.status() >= 3:
                break
            max_wait -= 1
            print("waiting for connection...")
            time.sleep(1)

        self.status = wlan.status()
        # Handle connection error
        if wlan.status() != 3:
            raise RuntimeError("network connection failed")
        else:
            print("connected")
            self.ifconfig = wlan.ifconfig()
            self.ip = self.ifconfig[0]
            print("ip = " + self.ip)

    def get_ip(self):
        """Return IP address"""
        return self.ip

    def get_ifconfig(self):
        """Return ifconfig"""
        return self.ifconfig

    def get_status(self):
        """Return Connection Status"""
        return self.status

if __name__ == "__main__":
    f = open("wifi.txt", "r")
    wifi_details = f.readline()
    f.close()
    credentials = {"ssid": wifi_details.split(" ")[0], "password" : wifi_details.split(" ")[1] }
    wifi_connect = Wifi(credentials, 10, "UK")
    print(wifi_connect.get_status())
    print(wifi_connect.get_ifconfig())