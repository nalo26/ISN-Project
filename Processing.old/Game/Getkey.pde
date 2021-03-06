boolean CanJoin = false;

//Si une touche est appuyé, faire ce qui est demandé en fonction du menu affiché
void keyPressed() {
  if (toshow == "Menu") { //Si le jeu est sur le menu principal
    if (keyCode==UP && Menu==2) Menu=1;
    if (keyCode==UP && Menu==4) Menu=3;
    if (keyCode==DOWN && Menu==1) Menu=2;
    if (keyCode==DOWN && Menu==3) Menu=4;
    if (keyCode==RIGHT && Menu==1) Menu=3;
    if (keyCode==RIGHT && Menu==2) Menu=4;
    if (keyCode==LEFT && Menu==3) Menu=1;
    if (keyCode==LEFT && Menu==4) Menu=2;
    if (Menu==1 && keyCode==ENTER) { //Lancer le menu de choix de jeu
      toshow = "MenuPlay";
      Menu = 0;
    }
    if (Menu==2 && keyCode==ENTER) toshow = "MenuEditor"; //Lancer l'éditeur
    if (Menu==3 && keyCode==ENTER) {
      toshow = "Options";
    }//Lancer le menu d'option
    if (Menu==4 && keyCode==ENTER) toshow = "Credits";
  }

  if (toshow == "MenuPlay") { //Si le jeu est sur la sélection de type de jeu
    if (keyCode==DOWN) Menu++;
    if (keyCode==UP) Menu--;
    if (keyCode==TAB) toshow = "Menu"; //Touche retour, pour revenir sur le menu principal
    if (Menu == 1 && keyCode == ENTER) toshow = "MenuMaps"; //Lancer le jeu
    if (Menu == 2 && keyCode == ENTER){
      toshow = "MenuMaps";
      IA = true;
    }
    if (Menu == 3 && keyCode == ENTER) toshow = "ServerCreate"; //Afficher la page de création de serveur
    if (Menu == 4 && keyCode == ENTER) toshow = "ServerJoin"; //Afficher la page pour rejoindre le serveur
  }

  if (toshow == "ServerJoin") { //récupérer l'entré des touches pour taper l'adresse ip du serveur à rejoindre
    if (keyCode == BACKSPACE && ServerIP.length() > 0) ServerIP = ServerIP.substring(0, ServerIP.length()-1);
    else if (keyCode == TAB) toshow = "MenuPlay";
    else if (keyCode == ENTER && ServerIP.length() > 7) CanJoin = true;
    else if (key != CODED && keyCode != ENTER && keyCode != BACKSPACE) ServerIP += key;
  }
  if (toshow == "MenuEditor" && keyCode == TAB) {
    toshow = "MenuMaps";
    InteracMap = 1;
  }
  if (toshow == "MenuMaps" && keyCode == SHIFT) {
    toshow = "Menu";
    InteracMap = 0;
  }

  if (toshow == "Options" && keyCode == TAB && MenuOpt==0 && Link==0) Reset();
  if (toshow == "Options" && keyCode == TAB && MenuOpt==0 && Link==1) toshow = "Game";
  if (toshow == "Options" && keyCode == RIGHT && MenuOpt==0) MenuOpt = SMenuOpt;
  if (toshow == "Options" && keyCode == TAB && MenuOpt>0) MenuOpt = 0;

  if (toshow == "Game"){
    if(keyCode == SHIFT) {
    toshow = "Options";
    Link=1;
    }
    if (Winner != 0 && keyCode == ' ') Reset();
  }

  if (toshow == "Credits" && keyCode == TAB) toshow = "Menu";
}
