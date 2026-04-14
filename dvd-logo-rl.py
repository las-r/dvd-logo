from pyray import * #type:ignore
import random

# dvd logo made by las-r on github

# settings
WIDTH, HEIGHT = 800, 600

# init window
init_window(WIDTH, HEIGHT, "DVD Logo")
set_target_fps(60)

# logos
dvds = ["dvdb", "dvdc", "dvdg", "dvdm", "dvdr", "dvdw", "dvdy"]
dvdts = []
for d in dvds:
    dvdi = load_image(f"images/{d}.png")
    dvdts.append(load_texture_from_image(dvdi))
    unload_image(dvdi)

# variables
cdvd = random.choice(dvdts)
x, y = WIDTH // 2, HEIGHT // 2
dx, dy = random.choice((-4, 4)), random.choice((-4, 4))

# main loop
while not window_should_close():
    # dvd movement
    x += dx
    y += dy
    if x <= 0 or x >= WIDTH - 100:
        dx *= -1
        cdvd = random.choice(dvdts)
    if y <= 0 or y >= HEIGHT - 44:
        dy *= -1
        cdvd = random.choice(dvdts)
    x = max(0, min(x, WIDTH))
    y = max(0, min(y, WIDTH))
    
    # draw
    begin_drawing()
    clear_background(BLACK)
    draw_texture_ex(cdvd, (x, y), 0, 0.1, WHITE)
    end_drawing()
        
# close
close_window()
