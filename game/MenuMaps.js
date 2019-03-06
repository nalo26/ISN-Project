void MenuMaps() {
  //Menu de sélection des maps

  // /!\ Don't touch my creation Mouhahahahaha /!\
  if (InteracMap==0) {
    ctx.fillStyle = "rgb(0, 0, 0)";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.textAlign = "center";
    image(BackgMenu,0,0);
    ctx.text = "20px Sans Serif";
    ctx.fillText("Play with Map N°1", 250, 200);
    ctx.fillText("Play with Map N°2", 250, 300);
    ctx.fillText("Play with Map N°3", 250, 400);
    ctx.text = "14px Sans Serif";
    ctx.fillText("Press arrows to select your folder and press RIGHT to load file", 250, 515);
    ctx.textAlign = "left";

    CurseurMenuMaps();

    //Chargement des maps
    Map1 = loadJSONObject("Map1.json");
    Map2 = loadJSONObject("Map2.json");
    Map3 = loadJSONObject("Map3.json");

    //Remplace la map par défault par celle sélectionée
    if (keyCode==RIGHT) {
      for (var i=0; i<99; i++) {
        String CollisionID = str (i);
        if (SelectMap==1)Collision [i] = Map1.getInt(CollisionID);
        if (SelectMap==2)Collision [i] = Map2.getInt(CollisionID);
        if (SelectMap==3)Collision [i] = Map3.getInt(CollisionID);
      }
      toshow = "Game";
    }
  }

  if (InteracMap==1) {
    ctx.fillStyle = "rgb(0, 0, 0)";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.textAlign = "center";
    image(BackgMenu,0,0);
    ctx.fillStyle = "rgb(101, 149, 99)";
    ctx.text = "20px Sans Serif";
    ctx.fillText("Remplace Map N°1", 250, 200);
    ctx.fillText("Remplace Map N°2", 250, 300);
    ctx.fillText("Remplace Map N°3", 250, 400);
    ctx.text = "13px Sans Serif";
    ctx.fillText("Press arrows to select a backup location and press Enter to save file", 250, 515);
    ctx.textAlign = "left";

    CurseurMenuMaps();

    //Le joueur choisir d'enregistrer sa Map 
    if (keyCode==ENTER) {

      if (SelectMap==1) Map1 = new JSONObject();
      if (SelectMap==2) Map2 = new JSONObject();
      if (SelectMap==3) Map3 = new JSONObject();

      for (var i=0; i<99; i++) {
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
    setTimeout(function() {}, 200);
  }
  if (keyCode==UP && keyPressed==true && SelectMap>1) {
    SelectMap--;
    setTimeout(function() {}, 200);
  }

  //Souligne le choix du joueur
  image(BalleR, 100, SelectMap*100+70);
  image(BalleL, 350, SelectMap*100+70);
}