void Menu() {
  if (Menu<1) Menu=1;
  if (Menu>3) Menu=3;
  fill(255);
  background(0);
  textSize(12);
  textAlign(CENTER);
  text(GameName, 250, 50);
  text("Select with arrows and enter", 250, 150);
  text("Game", 140, 250);
  text("Editor", 240, 250);
  text("Options", 340, 250);
  text("Press esc to back", 250, 350);
  rect(Menu*100+5, 270, 70, 5);
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