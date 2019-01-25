'''
blink.py (internal led)
'''

import machine
import time

led = machine.Pin(13, machine.Pin.OUT)

while True:
    led.value(1)
    time.sleep(0.5)
    led.value(0)
    time.sleep(0.5)
