void Menu() {
  fill(255);
  background(0);
  fill(101,149,99);
  textSize(20);
  textAlign(CENTER);
  image(BackgMenu,0,0);
  text("Game", 125+30, 150+60);
  text("Editor", 125+30, 350+50);
  text("Options", 375-30, 150+60);
  text("Credits", 375-30, 350+50);
  textSize(15);
  text("Select with arrows and enter and press esc to back", 250, 515);
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
  delay(10);
}

void MenuPlay() {
  if (Menu<1) Menu=1;
  if (Menu>3) Menu=3;
  background(0);
  textSize(20);
  textAlign(CENTER);
  image(BackgMenu,0,0);
  text("Solo vs Solo", 250, 200);
  text("Create Server", 250, 300);
  text("Join Server", 250, 400);
  text("", 250, 350);
  textSize(15);
  text("Select with arrows and enter and press tab to back", 250, 515);
  image(BalleR, 100, Menu*100+70);
  image(BalleL, 350, Menu*100+70);
  delay(10);
}

void MenuOption() {
}