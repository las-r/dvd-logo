// made by las-r on github

function rc(t) {
  return t[randomNumber(0, t.length - 1)];
}

var dirs = [2, -2];
var cols = ["b", "c", "g", "m", "r", "w", "y"];
var dvds = [[createSprite(200, 200), rc(dirs), rc(dirs)]];
dvds[0][0].setAnimation(rc(cols));
dvds[0][0].scale = 0.1;

function draw() {
  background("black");
  
  for (var i = 0; i < dvds.length; i++) {
    var dvd = dvds[i];
    
    dvd[0].x += dvd[1];
    dvd[0].y += dvd[2];
    
    if (dvd[0].x <= 50 || dvd[0].x >= 350) {
      dvd[0].x = Math.min(Math.max(50, dvd[0].x), 350);
      dvd[1] *= -1;
      dvd[0].setAnimation(rc(cols));
    }
    if (dvd[0].y <= 22 || dvd[0].y >= 378) {
      dvd[0].y = Math.min(Math.max(22, dvd[0].y), 378);
      dvd[2] *= -1;
      dvd[0].setAnimation(rc(cols));
    }
    
    if (mouseIsOver(dvd[0])) {
      dvd[0].setAnimation(rc(cols));
    }
  }
  
  if (keyWentDown("space")) {
    dvds.unshift([createSprite(200, 200), rc(dirs), rc(dirs)]);
    dvds[0][0].setAnimation(rc(cols));
    dvds[0][0].scale = 0.1;
  }
  
  stroke("none");
  fill("white");
  textSize(14);
  text("Amount of dvds: " + dvds.length, 2, 14);
  textAlign("left", "top");
  
  drawSprites();
}
