extern crate piston_window;
use piston_window::*;

// main
fn main() {
    // settings
    let width = 800;
    let height = 600;

    // setup window
    let mut window: PistonWindow = WindowSettings::new("DVD Logo", (width, height))
        .exit_on_esc(true)
        .build()
        .unwrap();
    
    // load images
    let mut texture_context = window.create_texture_context();
    let dvdb = Texture::from_path(&mut texture_context, "images/dvdb.png", Flip::None, &TextureSettings::new()).expect("Failed to load image");
    let dvdc = Texture::from_path(&mut texture_context, "images/dvdc.png", Flip::None, &TextureSettings::new()).expect("Failed to load image");
    let dvdg = Texture::from_path(&mut texture_context, "images/dvdg.png", Flip::None, &TextureSettings::new()).expect("Failed to load image");
    let dvdm = Texture::from_path(&mut texture_context, "images/dvdr.png", Flip::None, &TextureSettings::new()).expect("Failed to load image");
    let dvdr = Texture::from_path(&mut texture_context, "images/dvdm.png", Flip::None, &TextureSettings::new()).expect("Failed to load image");
    let dvdw = Texture::from_path(&mut texture_context, "images/dvdw.png", Flip::None, &TextureSettings::new()).expect("Failed to load image");
    let dvdy = Texture::from_path(&mut texture_context, "images/dvdy.png", Flip::None, &TextureSettings::new()).expect("Failed to load image");
    let mut dvd = dvdb.clone();

    // pos and vel
    let mut x = 0.0;
    let mut y = 0.0;
    let mut xs = 1.0;
    let mut ys = 1.0;
    
    // main loop
    while let Some(e) = window.next() {
        if let Some(_) = e.update_args() {
            // update position
            x += xs;
            y += ys;
    
            // bounce logic
            if x < 0.0 || x > width as f64 - 100.0 {
                xs = -xs;
                if dvd == dvdb {
                    dvd = dvdc.clone()
                }
                else if dvd == dvdc {
                    dvd = dvdg.clone()
                }
                else if dvd == dvdg {
                    dvd = dvdm.clone()
                }
                else if dvd == dvdm {
                    dvd = dvdr.clone()
                }
                else if dvd == dvdr {
                    dvd = dvdw.clone()
                }
                else if dvd == dvdw {
                    dvd = dvdy.clone()
                }
                else {
                    dvd = dvdb.clone()
                }
            }
            if y < 0.0 || y > height as f64 - 44.0 {
                ys = -ys;
                if dvd == dvdb {
                    dvd = dvdc.clone()
                }
                else if dvd == dvdc {
                    dvd = dvdg.clone()
                }
                else if dvd == dvdg {
                    dvd = dvdm.clone()
                }
                else if dvd == dvdm {
                    dvd = dvdr.clone()
                }
                else if dvd == dvdr {
                    dvd = dvdw.clone()
                }
                else if dvd == dvdw {
                    dvd = dvdy.clone()
                }
                else {
                    dvd = dvdb.clone()
                }
            }
        }
    
        if let Some(_) = e.render_args() {
            // draw the dvd logo
            window.draw_2d(&e, |c, g, _| {
                clear([0.0, 0.0, 0.0, 1.0], g);
                image(&dvd, c.transform.trans(x, y).scale(0.1, 0.1), g);
            });
        }
    }    
}
