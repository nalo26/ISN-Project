void MenuMaps() {
  //Menu de sélection des maps

  // /!\ Don't touch my creation Mouhahahahaha /!\
  if (InteracMap==0) {
    background(0);
    textAlign(CENTER);
    text("CHOIX DE LA MAP", 250, 50);
    text("Choisir Map N°1", 250, 100);
    text("Choisir Map N°2", 250, 200);
    text("Choisir Map N°3", 250, 300);
    text("Appuyer sur la flèche du Haut ou du Bas pour choisir un dossier de sauvegarde", 250, 400);
    text("Et Appuyez sur la flèche de droite pour confirmer", 250, 450);
    textAlign(LEFT);

    CurseurMenuMaps();

    //Chargement des maps
    Map1 = loadJSONObject("Map1.json");
    Map2 = loadJSONObject("Map2.json");
    Map3 = loadJSONObject("Map3.json");

    //Remplace la map par défault par celle sélectionée
    if (keyCode==RIGHT) {
      for (int i=0; i<99; i++) {
        String CollisionID = str (i);
        if (SelectMap==1)Collision [i] = Map1.getInt(CollisionID);
        if (SelectMap==2)Collision [i] = Map2.getInt(CollisionID);
        if (SelectMap==3)Collision [i] = Map3.getInt(CollisionID);
      }
      toshow = "Game";
    }
  }

  if (InteracMap==1) {
    background(0);
    textAlign(CENTER);
    text("Remplacer Map N°1", 250, 100);
    text("Remplacer Map N°2", 250, 200);
    text("Remplacer Map N°3", 250, 300);
    text("Appuyer sur la flèche du Haut ou du Bas pour choisir le dossier de sauvegarde", 250, 400);
    text("Et Appuyez sur Entrer pour confirmer", 250, 450);
    textAlign(LEFT);

    CurseurMenuMaps();

    //Le joueur choisir d'enregistrer sa Map 
    if (keyCode==ENTER) {

      if (SelectMap==1) Map1 = new JSONObject();
      if (SelectMap==2) Map2 = new JSONObject();
      if (SelectMap==3) Map3 = new JSONObject();

      for (int i=0; i<99; i++) {
        String ColisionID = str (i);

        if (SelectMap==1)Map1.setInt(ColisionID, Collision[i]);
        if (SelectMap==2)Map2.setInt(ColisionID, Collision[i]);
        if (SelectMap==3)Map3.setInt(ColisionID, Collision[i]);
      }
      if (SelectMap==1)saveJSONObject(Map1, "data/Map1.json");
      if (SelectMap==2)saveJSONObject(Map2, "data/Map2.json");
      if (SelectMap==3)saveJSONObject(Map3, "data/Map3.json");

      toshow = "Menu";
      InteracMap = 0;
    }
  }
}

void CurseurMenuMaps() {
  //Déplacement du curseur de choix
  if (keyCode==DOWN && keyPressed==true && SelectMap<3) {
    SelectMap++;
    delay(150);
  }
  if (keyCode==UP && keyPressed==true && SelectMap>1) {
    SelectMap--;
    delay(150);
  }

  //Souligne le choix du joueur
  rect(150, SelectMap*100+10, 200, 5);
}