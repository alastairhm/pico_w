"""
Blink the on board LED on Raspberry Pi Pico W
"""
import machine

led = machine.Pin("LED", machine.Pin.OUT)
timer = machine.Timer()


def blink(timer):
    """
    Toggle LED
    """
    led.toggle()


timer.init(freq=4, mode=machine.Timer.PERIODIC, callback=blink)

