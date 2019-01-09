void keyPressed() {
  if (toshow == "Menu") {
    if (keyCode==RIGHT) Menu++;
    if (keyCode==LEFT) Menu--;
    if (Menu==1 && keyCode==ENTER) toshow = "MenuPlay";
   // if (Menu==2 && keyCode==ENTER) toshow = "MenuEditor";
   // if (Menu==3 && keyCode==ENTER) toshow = "MenuOption";
  }
  if (toshow == "MenuPlay") {
    if (keyCode==RIGHT) Menu++;
    if (keyCode==LEFT) Menu--;
    if (Menu == 1 && keyCode == ENTER) toshow = "Game";
    if (Menu == 2 && keyCode == ENTER) toshow = "ServerCreate";
    if (Menu == 3 && keyCode == ENTER) toshow = "ServerJoin";
  }
}
