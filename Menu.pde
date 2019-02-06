void Menu() {
  fill(255);
  background(0);
  textSize(20);
  textAlign(CENTER);
  text(GameName, 250, 50);
  text("Game", 125, 150+40);
  text("Editor", 125, 350+40);
  text("Options", 375, 150+40);
  text("Credits", 375, 350+40);
  textSize(15);
  text("Select with arrows and enter and press esc to back", 250, 500);
  if (Menu==1) {
    image(BalleR, 25, 120+40);
    image(BalleL, 175, 120+40);
  }
  if (Menu==2) {
    image(BalleR, 25, 320+40);
    image(BalleL, 175, 320+40);
  }
  if (Menu==3) {
    image(BalleR, 275, 120+40);
    image(BalleL, 425, 120+40);
  }
  if (Menu==4) {
    image(BalleR, 275, 320+40);
    image(BalleL, 425, 320+40);
  }
  delay(10);
}

void MenuPlay() {
  if (Menu<1) Menu=1;
  if (Menu>3) Menu=3;
  background(0);
  textSize(12);
  textAlign(CENTER);
  text(GameName, 250, 50);
  text("Select with arrows and enter", 250, 150);
  text("Solo vs Solo", 140, 250);
  text("Create Server", 240, 250);
  text("Join Server", 340, 250);
  text("Press tab to back", 250, 350);
  rect(Menu*100+5, 270, 70, 5);
  delay(10);
}

void MenuOption() {
}