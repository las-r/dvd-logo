require "gosu"

# dvd logo made by las-r on github

# window
class Window < Gosu::Window
    def dvdColor
        @odvd = @dvd
        while @dvd == @odvd
            @dvd = [@dvdb, @dvdc, @dvdg, @dvdm, @dvdr, @dvdw, @dvdy].sample
        end
    end

    def initialize
        # settings
        @width = 800
        @height = 600

        # setup window
        super @width, @height
        self.caption = "DVD Logo"

        # variables
        @x = (@width / 2).to_i
        @y = (@height / 2).to_i
        @xs = 2
        @ys = 2

        # images
        @dvdb = Gosu::Image.new("images/dvdb.png")
        @dvdc = Gosu::Image.new("images/dvdc.png")
        @dvdg = Gosu::Image.new("images/dvdg.png")
        @dvdm = Gosu::Image.new("images/dvdm.png")
        @dvdr = Gosu::Image.new("images/dvdr.png")
        @dvdw = Gosu::Image.new("images/dvdw.png")
        @dvdy = Gosu::Image.new("images/dvdy.png")

        # set logo color
        dvdColor
    end

    def update
        @x += @xs
        @y += @ys

        if @x == 0 or @x == @width - 100
            @xs *= -1
            dvdColor
        end
        if @y == 0 or @y == @height - 44
            @ys *= -1
            dvdColor
        end
    end

    def draw
        # draw logo
        @dvd.draw(@x, @y, 0, 0.1, 0.1)
    end
end

window = Window.new
window.show
