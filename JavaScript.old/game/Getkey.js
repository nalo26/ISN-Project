var key;
var keyPressed;
/*
UP = 38
DOWN = 40
RIGHT = 39
LEFT = 37
SHIFT = 16
ENTER = 13
TAB = 9
ESC = 27
SPACE = 32

https://keycode.info/
*/

//Si une touche est appuyé, faire ce qui est demandé en fonction du menu affiché
document.addEventListener('keydown', function(event) {
  key = event.keyCode;
  keyPressed = true;
  if (toshow == "Menu") { //Si le jeu est sur le menu principal
    if (key==38 && Menu==2) Menu=1;
    if (key==38 && Menu==4) Menu=3;
    if (key==40 && Menu==1) Menu=2;
    if (key==40 && Menu==3) Menu=4;
    if (key==39 && Menu==1) Menu=3;
    if (key==39 && Menu==2) Menu=4;
    if (key==37 && Menu==3) Menu=1;
    if (key==37 && Menu==4) Menu=2;
    if (Menu==1 && key==13) { //Lancer le menu de choix de jeu
      toshow = "MenuPlay";
      Menu = 0;
    }
    if (Menu==2 && key==13) toshow = "MenuEditor"; //Lancer l'éditeur
    if (Menu==3 && key==13) {
      toshow = "Options";
    }//Lancer le menu d'option
    if (Menu==4 && key==13) toshow = "Credits";
  }

  if (toshow == "MenuPlay") { //Si le jeu est sur la sélection de type de jeu
    if (key==40) Menu++;
    if (key==38) Menu--;
    if (key==9) toshow = "Menu"; //Touche retour, pour revenir sur le menu principal
    if (Menu == 1 && key == 13) toshow = "MenuMaps"; //Lancer le jeu
    if (Menu == 2 && key == 13){
      toshow = "MenuMaps";
      IA = true;
    }
    if (Menu == 3 && key == 13) toshow = "ServerCreate"; //Afficher la page de création de serveur
    if (Menu == 4 && key == 13) toshow = "ServerJoin"; //Afficher la page pour rejoindre le serveur
  }

  if (toshow == "MenuEditor" && key == 9) {
    toshow = "MenuMaps";
    InteracMap = 1;
  }
  if (toshow == "MenuMaps" && key == 16) {
    toshow = "Menu";
    InteracMap = 0;
  }

  if (toshow == "Options" && key == 9 && MenuOpt==0 && Link==0) Reset();
  if (toshow == "Options" && key == 9 && MenuOpt==0 && Link==1) toshow = "Game";
  if (toshow == "Options" && key == 39 && MenuOpt==0) MenuOpt = SMenuOpt;
  if (toshow == "Options" && key == 9 && MenuOpt>0) MenuOpt = 0;

  if (toshow == "Game"){
    if (key == 16) {
    toshow = "Options";
    Link=1;
    }
    if (Winner != 0 && key == 32) Reset();
  }

  if (toshow == "Credits" && key == 9) toshow = "Menu";
});

document.addEventListener('keyup', function(event) {
  if (event.keyCode == key){
   key = 0;
   keyPressed = false;
  }  

});