void Menu() {
  if (Menu<1) Menu=1;
  if (Menu>3) Menu=3;
  fill(255);
  background(0);
  textSize(12);
  text(GameName, 220, 50);
  text("Select with arrows and enter", 170, 150);
  text("Jeu", 120, 250);
  text("Editeur", 220, 250);
  text("Options", 320, 250);
  text("Press esc to back", 200, 350);
  rect(Menu*100+20, 270, 70, 5);
  delay(10);
}

void MenuPlay() {
  if (Menu<1) Menu=1;
  if (Menu>3) Menu=3;
  background(0);
  textSize(12);
  text(GameName, 220, 50);
  text("Select with arrows and enter", 170, 150);
  text("Solo vs Solo", 120, 250);
  text("Create Server", 220, 250);
  text("Join Server", 320, 250);
  text("Press esc to back", 200, 350);
  rect(Menu*100+20, 270, 70, 5);
  delay(10);
}

void MenuEditor() {
}

void MenuOption() {
}
