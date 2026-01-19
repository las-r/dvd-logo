// dvd logo made by las-r on github

// variables
let x, y;
let xSpeed, ySpeed;
let dvd;
let logoWidth = 120;
let logoHeight = 60;

// dvd logo images
let imgs = [
  'https://raw.githubusercontent.com/las-r/dvd-logo/refs/heads/main/images/dvdb.png',
  'https://raw.githubusercontent.com/las-r/dvd-logo/refs/heads/main/images/dvdc.png',
  'https://raw.githubusercontent.com/las-r/dvd-logo/refs/heads/main/images/dvdg.png',
  'https://raw.githubusercontent.com/las-r/dvd-logo/refs/heads/main/images/dvdm.png',
  'https://raw.githubusercontent.com/las-r/dvd-logo/refs/heads/main/images/dvdr.png',
  'https://raw.githubusercontent.com/las-r/dvd-logo/refs/heads/main/images/dvdw.png',
  'https://raw.githubusercontent.com/las-r/dvd-logo/refs/heads/main/images/dvdy.png'
];

// change dvd color function
function dvdColor() {
  let randomIndex = Math.floor(Math.random() * imgs.length);
  dvd = loadImage(imgs[randomIndex]);
}

// preload & setup
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

// draw loop
function draw() {
  background(0);

  // draw dvd
  if (dvd) {
    image(dvd, x, y, logoWidth, logoHeight);
  }

  // dvd movement
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
