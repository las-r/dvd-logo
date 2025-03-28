import pygame
import random
import time

# initialize
pygame.init()

# settings
WIDTH, HEIGHT = 800, 600
DVDIMG = "images/dvd.png"
DVDWIDTH, DVDHEIGHT = 100, 44
DVDSPEED = 500
BGCOLOR = (0, 0, 0)

# variables
xPos = WIDTH // 2
yPos = HEIGHT // 2
xDir = random.randint(0, 1)
yDir = random.randint(0, 1)

# load dvd logo
dvd = pygame.transform.scale(pygame.image.load(DVDIMG), (DVDWIDTH, DVDHEIGHT))

# setup display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DVD Logo")

# main loop
running = True
while running:
    screen.fill(BGCOLOR)

    # event
    for event in pygame.event.get():
        # quit
        if event.type == pygame.QUIT:
            running = False

    # dvd logo
    screen.blit(dvd, (xPos, yPos))

    # move dvd position
    if xDir:
        xPos += 1
    else:
        xPos -= 1
    if yDir:
        yPos -= 1
    else:
        yPos += 1

    # bounce dvd logo
    if xPos == 0:
        xDir = 1
    if xPos == WIDTH - DVDWIDTH:
        xDir = 0
    if yPos == 0:
        yDir = 0
    if yPos == HEIGHT - DVDHEIGHT:
        yDir = 1

    # detect corner hit
    if (xPos == 0 or xPos == WIDTH - DVDWIDTH) and (yPos == 0 or yPos == HEIGHT - DVDHEIGHT):
        print("omg it hit the corner wowowowow")

    # update display
    pygame.display.flip()

    # speed
    time.sleep(1 / DVDSPEED)

# quit
pygame.quit()