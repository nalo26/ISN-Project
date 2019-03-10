function MenuMaps() {
  //Menu de sélection des maps

  if (InteracMap==0) {
    background(0, 0, 0);
    textAlign(CENTER);
    image(BackgMenu,0,0);
    textSize(20);
    text("Play with Map N°1", 250, 200);
    text("Play with Map N°2", 250, 300);
    text("Play with Map N°3", 250, 400);
    textSize(14);
    text("Press arrows to select your folder and press RIGHT to load file", 250, 515);
    textAlign(LEFT);

    CurseurMenuMaps();

    //Chargement des maps
    Map1 = $.getJSON("Map1.json");
    Map2 = $.getJSON("Map2.json");
    Map3 = $.getJSON("Map3.json");

    //Remplace la map par défault par celle sélectionée
    if (keyPressed == true && key==39) {
      for (int i=0; i<99; i++) {
        if (SelectMap==1) Collision[i] = Map1[i];
        if (SelectMap==2) Collision[i] = Map2[i];
        if (SelectMap==3) Collision[i] = Map3[i];
      }
      toshow = "Game";
    }
  }

  if (InteracMap==1) {
    background(0, 0, 0);
    textAlign(CENTER);
    image(BackgMenu,0,0);
    fill(101,149,99);
    textSize(20);
    text("Remplace Map N°1", 250, 200);
    text("Remplace Map N°2", 250, 300);
    text("Remplace Map N°3", 250, 400);
    textSize(13);
    text("Press arrows to select a backup location and press Enter to save file", 250, 515);
    textAlign(LEFT);

    CurseurMenuMaps();

    //Le joueur choisir d'enregistrer sa Map 
    if (keyPressed == true && key==13) {

      if (SelectMap==1) Map1 = [];
      if (SelectMap==2) Map2 = [];
      if (SelectMap==3) Map3 = [];

      for (int i=0; i<99; i++) {
        if (SelectMap==1) Map1[i] = Collision[i];
        if (SelectMap==2) Map2[i] = Collision[i];
        if (SelectMap==3) Map3[i] = Collision[i];
      }
      var fs = require('fs');
      if (SelectMap==1) fs.writeFile("data/Map1.json", Map1);
      if (SelectMap==2) fs.writeFile("data/Map2.json", Map2);
      if (SelectMap==3) fs.writeFile("data/Map3.json", Map3);

      toshow = "Menu";
      InteracMap = 0;
    }
  }
}

function CurseurMenuMaps() {
  //Déplacement du curseur de choix
  if (key==40 && keyPressed==true && SelectMap<3) {
    SelectMap++;
    delay(150);
  }
  if (key==38 && keyPressed==true && SelectMap>1) {
    SelectMap--;
    delay(150);
  }

  //Souligne le choix du joueur
  image(BalleR, 100, SelectMap*100+70);
  image(BalleL, 350, SelectMap*100+70);
}