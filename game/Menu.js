function Menu() {
  ctx.fillStyle = "rgb(255, 255, 255)";
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = "rgb(101,149,99)";
  ctx.text = "20px Sans Serif";
  ctx.textAlign = "center";
  image(BackgMenu,0,0);
  ctx.fillText("Game", 125+30, 150+60);
  ctx.fillText("Editor", 125+30, 350+50);
  ctx.fillText("Options", 375-30, 150+60);
  ctx.fillText("Credits", 375-30, 350+50);
  ctx.text = "15px Sans Serif";
  ctx.fillText("Select with arrows and enter and press esc to back", 250, 515);
  if (Menu==1) {
    image(BalleR, 25+30, 120+60);
    image(BalleL, 175+30, 120+60);
  }
  if (Menu==2) {
    image(BalleR, 25+30, 320+50);
    image(BalleL, 175+30, 320+50);
  }
  if (Menu==3) {
    image(BalleR, 275-30, 120+60);
    image(BalleL, 425-30, 120+60);
  }
  if (Menu==4) {
    image(BalleR, 275-30, 320+50);
    image(BalleL, 425-30, 320+50);
  }
  setTimeout(function() {}, 10);
}

void MenuPlay() {
  if (Menu<1) Menu=1;
  if (Menu>4) Menu=4;
  ctx.fillStyle = "rgb(0, 0, 0)";
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  ctx.text = "20px Sans Serif";
  ctx.textAlign = "center";
  image(BackgMenu,0,0);
  ctx.fillText("1 vs 1 Local", 250, 200);
  ctx.fillText("1 vs IA Local", 250, 270);
  ctx.fillText("Create Server", 250, 340);
  ctx.fillText("Join Server", 250, 410);
  ctx.text = "15px Sans Serif";
  ctx.fillText("Select with arrows and enter and press tab to back", 250, 515);
  image(BalleR, 100, Menu*70+100);
  image(BalleL, 350, Menu*70+100);
  setTimeout(function() {}, 10);
}