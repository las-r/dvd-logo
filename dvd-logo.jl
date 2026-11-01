using Raylib

# dvd logo made by las-r on github

# settings
WIDTH, HEIGHT = 800, 600

# init
Raylib.InitWindow(WIDTH, HEIGHT, "DVD Logo")
Raylib.SetTargetFPS(60)

# logos
dvds = ["dvdb", "dvdc", "dvdg", "dvdm", "dvdr", "dvdw", "dvdy"]
dvdts = []
for d in dvds 
    dvdi = Raylib.LoadImage("images/$(d).png")
    push!(dvdts, Raylib.LoadTextureFromImage(dvdi))
    Raylib.UnloadImage(dvdi)
end

# main loop function
function main()
    # variables
    cdvd = rand(dvdts)
    x, y = fld(WIDTH, 2), fld(HEIGHT, 2)
    dx, dy = rand([-4, 4]), rand([-4, 4])

    # main loop
    while !Raylib.WindowShouldClose()
        # dvd movement
        x += dx
        y += dy
        if x <= 0 || x >= WIDTH - 100 || y <= 0 || y >= HEIGHT - 44
            dx = x <= 0 || x >= WIDTH - 100 ? -dx : dx
            dy = y <= 0 || y >= HEIGHT - 44 ? -dy : dy
            cdvd = rand(dvdts)
        end
        x = clamp(x, 0, WIDTH - 100)
        y = clamp(y, 0, HEIGHT - 44)

        # draw
        Raylib.BeginDrawing()
            Raylib.ClearBackground(Raylib.BLACK)
            Raylib.DrawTextureEx(cdvd, Raylib.RayVector2(x, y), 0, 0.1, Raylib.WHITE)
        Raylib.EndDrawing()
    end

    # deinit
    Raylib.CloseWindow()
end

main()
