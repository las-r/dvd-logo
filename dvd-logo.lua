-- dvd logo made by las-r on github

-- settings
WIDTH, HEIGHT = 800, 600

-- variables
local x = math.floor(WIDTH / 2)
local y = math.floor(HEIGHT / 2)
local xs = 2
local ys = 2
local dvd
local dvdb
local dvdc
local dvdg
local dvdm
local dvdr
local dvdw
local dvdy
local images

-- color change
local function color()
    local odvd = dvd
    while dvd == odvd do
        dvd = images[math.random(#images)]
    end
end

-- load
function love.load()
    -- setup window
    love.window.setMode(WIDTH, HEIGHT)
    love.window.setTitle("DVD Logo")

    -- images
    dvdb = love.graphics.newImage("images/dvdb.png")
    dvdc = love.graphics.newImage("images/dvdc.png")
    dvdg = love.graphics.newImage("images/dvdg.png")
    dvdm = love.graphics.newImage("images/dvdm.png")
    dvdr = love.graphics.newImage("images/dvdr.png")
    dvdw = love.graphics.newImage("images/dvdw.png")
    dvdy = love.graphics.newImage("images/dvdy.png")
    images = {dvdb, dvdc, dvdg, dvdm, dvdr, dvdw, dvdy}

    -- dvd logo
    dvd = images[math.random(#images)]
end

-- update
function love.update()
    -- move dvd
    x = x + xs
    y = y + ys

    -- bounce dvd
    if x <= 0 or x >= WIDTH - 100 then
        xs = -xs
        color()
    end
    if y <= 0 or y >= HEIGHT - 44 then
        ys = -ys
        color()
    end
end

-- draw
function love.draw()
    love.graphics.draw(dvd, x, y, 0, 0.1, 0.1)
end
