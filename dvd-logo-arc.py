import arcade
import random

# settings
WIDTH, HEIGHT = 800, 600

# dvd images
dvdb = arcade.load_texture("images/dvdb.png")
dvdc = arcade.load_texture("images/dvdc.png")
dvdg = arcade.load_texture("images/dvdg.png")
dvdm = arcade.load_texture("images/dvdm.png")
dvdr = arcade.load_texture("images/dvdr.png")
dvdw = arcade.load_texture("images/dvdw.png")
dvdy = arcade.load_texture("images/dvdy.png")
dvd = random.choice([dvdb, dvdc, dvdg, dvdm, dvdr, dvdw, dvdy])

# variables
x = WIDTH // 2
y = HEIGHT // 2
xs = random.choice([-2, 2])
ys = random.choice([-2, 2])

# dvd color change
def dvdColor():
    global dvd
    odvd = dvd
    while dvd == odvd:
        dvd = random.choice([dvdb, dvdc, dvdg, dvdm, dvdr, dvdw, dvdy])
        
# view class
class View(arcade.View):
    def __init__(self):
        super().__init__()
    
    # update func
    def on_update(self, delta_time):
        global x, y, xs, ys
        
        # move dvd
        x += xs
        y += ys
        
        # bounce dvd
        if x <= 50 or x >= WIDTH - 50:
            xs = -xs
            dvdColor()
        if y <= 22 or y >= HEIGHT - 22:
            ys = -ys
            dvdColor()
            
    # draw func
    def on_draw(self):
        self.clear()
        arcade.draw_texture_rect(dvd, arcade.XYWH(x, y, 100, 44))

# window
arcade.Window(WIDTH, HEIGHT, "DVD Logo").show_view(View())

# arcade loop
arcade.run()
