import pyxel
import random

# dvd logo made by las-r on github

class App:
    def __init__(self):
        pyxel.init(800, 600)
        pyxel.load("my_resource.pyxres")
        self.DVDS = 32
        self.x = pyxel.width // 2
        self.y = pyxel.height // 2
        self.dx = random.choice([-4, 4])
        self.dy = random.choice([-4, 4])
        self.curcol = 7
        pyxel.run(self.update, self.draw)
    
    def update(self):
        self.x += self.dx
        self.y += self.dy
        if self.x <= 0 or self.x >= pyxel.width - self.DVDS:
            self.x = max(0, min(pyxel.width - self.DVDS, self.x))
            self.dx *= -1
            self.curcol = random.randint(1, 15)
        if self.y <= 0 or self.y >= pyxel.height - self.DVDS:
            self.y = max(0, min(pyxel.height - self.DVDS, self.y))
            self.dy *= -1
            self.curcol = random.randint(1, 15)
            
    def draw(self):
        pyxel.cls(0)
        pyxel.pal(7, self.curcol)
        pyxel.blt(self.x, self.y, 0, 0, 0, 16, 16, 0, scale=4)
        pyxel.pal()
        
App()