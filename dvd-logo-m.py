from machine import Pin, SPI
from random import randint
from time import sleep_ms
import max7219

# led matrix
spi = SPI(1, baudrate=10000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(23))
cs = Pin(5, Pin.OUT)

# display init
display = max7219.Matrix8x8(spi, cs, 1)
display.brightness(5)

# pixel vals
x, y = randint(0, 7), randint(0, 7)
dx, dy = 2, 1

# bounce loop
while True:
    # output pixel
    display.fill(0)
    display.pixel(x, y, 1)
    display.show()
    
    # update pixel location
    x += dx
    y += dy
    
    # bounce pixel
    if x <= 0 or x >= 7:
        x = max(0, min(x, 7))
        dx *= -1
    if y <= 0 or y >= 7:
        x = max(0, min(x, 7))
        dy *= -1
        
    # delay
    sleep_ms(250)
