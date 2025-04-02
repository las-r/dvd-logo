import pygame
import random
import time

# initialize
pygame.init()

# dvd color change
def dvdColor():
    global dvd
    
    oDvd = dvd
    while dvd == oDvd:
        dvd = random.choice([dvdb, dvdc, dvdg, dvdm, dvdr, dvdw, dvdy])

# settings
WIDTH, HEIGHT = 800, 600
DVDWIDTH, DVDHEIGHT = 100, 44
DVDSPEED = 400
BGCOLOR = (0, 0, 0)

# variables
x = WIDTH // 2
y = HEIGHT // 2
xs = random.choice([-1, 1])
ys = random.choice([-1, 1])

# load dvd logos
dvdb = pygame.transform.scale(pygame.image.load("images/dvdb.png"), (DVDWIDTH, DVDHEIGHT))
dvdc = pygame.transform.scale(pygame.image.load("images/dvdc.png"), (DVDWIDTH, DVDHEIGHT))
dvdg = pygame.transform.scale(pygame.image.load("images/dvdg.png"), (DVDWIDTH, DVDHEIGHT))
dvdm = pygame.transform.scale(pygame.image.load("images/dvdm.png"), (DVDWIDTH, DVDHEIGHT))
dvdr = pygame.transform.scale(pygame.image.load("images/dvdr.png"), (DVDWIDTH, DVDHEIGHT))
dvdw = pygame.transform.scale(pygame.image.load("images/dvdw.png"), (DVDWIDTH, DVDHEIGHT))
dvdy = pygame.transform.scale(pygame.image.load("images/dvdy.png"), (DVDWIDTH, DVDHEIGHT))
dvd = random.choice([dvdb, dvdc, dvdg, dvdm, dvdr, dvdw, dvdy])

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
    screen.blit(dvd, (x, y))

    # move dvd position
    x += xs
    y += ys

    # bounce dvd logo
    if x == 0 or x == WIDTH - DVDWIDTH:
        xs = -xs
        dvdColor()
    if y == 0 or y == HEIGHT - DVDHEIGHT:
        ys = -ys
        dvdColor()

    # update display
    pygame.display.flip()

    # speed
    time.sleep(1 / DVDSPEED)

# quit
pygame.quit()
