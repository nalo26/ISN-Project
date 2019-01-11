boolean CanJoin = false;

void keyPressed() {
  if (toshow == "Menu") {
    if (keyCode==RIGHT) Menu++;
    if (keyCode==LEFT) Menu--;
    if (Menu==1 && keyCode==ENTER) {
      toshow = "MenuPlay";
      Menu = 0;
    }
    // if (Menu==2 && keyCode==ENTER) toshow = "MenuEditor";
    // if (Menu==3 && keyCode==ENTER) toshow = "MenuOption";
  }
  
  if (toshow == "MenuPlay") {
    if (keyCode==RIGHT) Menu++;
    if (keyCode==LEFT) Menu--;
    if (keyCode==TAB) toshow = "Menu";
    if (Menu == 1 && keyCode == ENTER) toshow = "Game";
    if (Menu == 2 && keyCode == ENTER) toshow = "ServerCreate";
    if (Menu == 3 && keyCode == ENTER){
      toshow = "ServerJoin";
      delay(300);
    }
  }
  
  if (toshow == "ServerJoin") {
      if (keyCode == BACKSPACE && ServerIP.length() > 0) ServerIP = ServerIP.substring(0, ServerIP.length()-1);
      else if (keyCode == TAB) toshow = "MenuPlay";
      else if (keyCode == ENTER && ServerIP.length() > 7) CanJoin = true;
      else if (key != CODED && keyCode != ENTER && keyCode != BACKSPACE) ServerIP += key;
  }
}
