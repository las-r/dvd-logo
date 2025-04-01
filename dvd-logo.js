let x, y;
let xSpeed, ySpeed;
let dvd;
let logoWidth = 120;
let logoHeight = 60;

let imgs = [
  'https://raw.githubusercontent.com/las-r/dvd-logo/refs/heads/main/images/dvdb.png',
  'https://raw.githubusercontent.com/las-r/dvd-logo/refs/heads/main/images/dvdc.png',
  'https://raw.githubusercontent.com/las-r/dvd-logo/refs/heads/main/images/dvdg.png',
  'https://raw.githubusercontent.com/las-r/dvd-logo/refs/heads/main/images/dvdm.png',
  'https://raw.githubusercontent.com/las-r/dvd-logo/refs/heads/main/images/dvdr.png',
  'https://raw.githubusercontent.com/las-r/dvd-logo/refs/heads/main/images/dvdw.png',
  'https://raw.githubusercontent.com/las-r/dvd-logo/refs/heads/main/images/dvdy.png'
];

function dvdColor() {
  let randomIndex = Math.floor(Math.random() * imgs.length);
  dvd = loadImage(imgs[randomIndex]);
}

function preload() {
  dvdColor();
}

function setup() {
  createCanvas(800, 600);
  x = random(width - logoWidth);
  y = random(height - logoHeight);
  xSpeed = 3;
  ySpeed = 3;
}

function draw() {
  background(0);
  
  if (dvd) {
    image(dvd, x, y, logoWidth, logoHeight);
  }

  x += xSpeed;
  y += ySpeed;
  
  if (x <= 0 || x + logoWidth >= width) {
    xSpeed *= -1;
    dvdColor();
  }
  
  if (y <= 0 || y + logoHeight >= height) {
    ySpeed *= -1;
    dvdColor();
  }
}
