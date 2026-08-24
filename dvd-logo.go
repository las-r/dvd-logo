package main

import (
	"math/rand/v2"

	rl "github.com/gen2brain/raylib-go/raylib"
)

// dvd logo made by las-r on github

func main() {
	// settings
	const w = 800
	const h = 600

	// init
	rl.InitWindow(800, 600, "DVD Logo")
	rl.SetTargetFPS(60)
	defer rl.CloseWindow()

	// logos
	var dvds = []string{"dvdb", "dvdc", "dvdg", "dvdm", "dvdr", "dvdw", "dvdy"}
	var dvdts = make([]rl.Texture2D, 0, len(dvds))
	for _, d := range dvds {
		var dvdi = rl.LoadImage("images/" + d + ".png")
		dvdts = append(dvdts, rl.LoadTextureFromImage(dvdi))
	}

	// variables
	var cdvd = dvdts[rand.IntN(len(dvdts))]
	var x = int(w / 2)
	var y = int(h / 2)
	var dx = []int{-4, 4}[rand.IntN(2)]
	var dy = []int{-4, 4}[rand.IntN(2)]

	// main loop
	for !rl.WindowShouldClose() {
		// dvd movement
		x += dx
		y += dy
		if x <= 0 || x >= w-100 {
			dx *= -1
			cdvd = dvdts[rand.IntN(len(dvdts))]
		}
		if y <= 0 || y >= h-44 {
			dy *= -1
			cdvd = dvdts[rand.IntN(len(dvdts))]
		}
		x = max(0, min(x, w))
		y = max(0, min(y, h))

		// draw
		rl.BeginDrawing()
		rl.ClearBackground(rl.Black)
		rl.DrawTextureEx(cdvd, rl.Vector2{X: float32(x), Y: float32(y)}, 0.0, 0.1, rl.White)
		rl.EndDrawing()
	}
}
