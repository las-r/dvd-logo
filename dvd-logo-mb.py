import random
import time
from microbit import *

# dvd logo made by las-r on github

# variables
x, y = random.randint(0, 3), random.randint(0, 4)
dx, dy = random.choice([-1, 1]), random.choice([-1, 1])

# main loop
while True:
    # update display
    display.clear()
    display.set_pixel(x, y, 9)
    display.set_pixel(x + 1, y, 9)
    
    # dvd movement
    x += dx
    y += dy
    if x <= 0 or x >= 3:
        dx = -dx
    if y <= 0 or y >= 4:
        dy = -dy
        
    # tick rate
    time.sleep_ms(200)
