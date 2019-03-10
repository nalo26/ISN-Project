/*
/!\Il y a des éléments spécifiques à cet affichage (bien qu'il faille faire le tri) /!\
 Affichages des tanks ne doit pas se faire par exemple d'ou le AffEditeur
 
 */

function MenuEditor() {
  AffEditeur();
  textSize(10);
  text("SHIFT=Print",450,515);
  text("ENTER=Switch",450,525);
  text("TAB=Save",450,535);
  text("TAB+SHIFT=Menu",450,545);

  //Enter permet d'accéder au choix des types de terrains (ex:montagne,lave...) qui vont remplacer ceux choisit par le curseur  
  if (keyPressed == true && key==13 && Selectile==0 && LockTile==0) {
    Selectile=1;
    LockTile=1;
  }
  if (keyPressed == true && key==13 && Selectile!=0 && LockTile==0) {
    Selectedtile=Selectile-1;
    Selectile=0;
    LockTile=1;
  }
  //A changer plus tard (Force le joueur a choisir une texture avec les fleches avant de valider
  if (keyPressed==true) LockTile=0;

  //Déplacement du curseur
  if (keyPressed==true && keyPressed == true && key==37 && Selectile==0 && XCursorEdit!=0) XCursorEdit--;
  if (keyPressed==true && keyPressed == true && key==39 && Selectile==0 && XCursorEdit!=9) XCursorEdit++;
  if (keyPressed==true && keyPressed == true && key==38 && Selectile==0 && YCursorEdit!=0) YCursorEdit--;
  if (keyPressed==true && keyPressed == true && key==40 && Selectile==0 && YCursorEdit!=9) YCursorEdit++;

  if (keyPressed==true && keyPressed == true && key==37 && Selectile!=0 && Selectile!=1) Selectile--;
  if (keyPressed==true && keyPressed == true && key==39 && Selectile!=0 && Selectile!=5) Selectile++;

  //Remplace le terrain choisit par le curseur par celui choisit dans la barre d'info (En appuyant sur Shift)
  if (keyPressed==true && keyPressed == true && key==16 && Selectile==0) Collision [XCursorEdit+YCursorEdit*10] =Selectedtile;
}

function AffEditeur () {//Affiche l'éditeur
  delay(150);
  background(45, 139, 97);
  fill(0, 0, 0);
  rect(0, 500, 500, 50);
  fill(200, 200, 200);
  rect(0, 500, 500, 3);

  for (int x=0; x<10; x++) {
    for (int y=0; y<10; y++) {
      var Ax = x;
      var Ay = y*10;
      var A = Ax + Ay;
      if (Collision [A] ==1) {
        image(Montagne, x*50, y*50);
      }//Couleur Roche
      if (Collision [A] ==2) {
        //Eau
        image(Eau, x*50, y*50);

        //rebors eau
        if (A>10 && Collision [A-10] !=2) {
          image(ContH, x*50, y*50);
          Haut=true;
        }
        if (A<90 && Collision [A+10] !=2) {
          image(ContB, x*50, y*50);
          Bas=true;
        }
        if (A!=0 && A!=10 && A!=20 && A!=30 && A!=40 && A!=50 && A!=60 && A!=70 && A!=80 && A!=90 && Collision [A-1] !=2) {
          image(ContG, x*50, y*50);
          Gauche=true;
        }
        if (A!=9 &&A!=19 && A!=29 && A!=39 && A!=49 && A!=59 && A!=69 && A!=79 && A!=89 && A!=99 && Collision [A+1] !=2) {
          image(ContD, x*50, y*50);
          Droite=true;
        }

        //Coins/angles lave
        if (Haut==true && Droite==true) image(ContHD, x*50, y*50);
        if (Haut==true && Gauche==true) image(ContHG, x*50, y*50);
        if (Bas==true && Droite==true) image(ContBD, x*50, y*50);
        if (Bas==true && Gauche==true) image(ContBG, x*50, y*50);

        //Remise a 0 de la détection des tiles autours du blocs de lave
        Bas= false;
        Haut= false;
        Droite= false;
        Gauche= false;
      }//Couleur Eau

      if (Collision [A] ==3) {
        //Lave
        image(Lave, x*50, y*50);
        //rebors lave
        if (A>10 && Collision [A-10] !=3) {
          image(ContH, x*50, y*50);
          Haut=true;
        }
        if (A<90 && Collision [A+10] !=3) { 
          image(ContB, x*50, y*50);
          Bas=true;
        }
        if (A!=0 && A!=10 && A!=20 && A!=30 && A!=40 && A!=50 && A!=60 && A!=70 && A!=80 && A!=90 && Collision [A-1] !=3) {
          image(ContG, x*50, y*50);
          Gauche=true;
        }
        if (A!=9 &&A!=19 && A!=29 && A!=39 && A!=49 && A!=59 && A!=69 && A!=79 && A!=89 && A!=99 && Collision [A+1] !=3) {
          image(ContD, x*50, y*50);
          Droite=true;
        }

        //Coins/angles lave
        if (Haut==true && Droite==true) image(ContHD, x*50, y*50);
        if (Haut==true && Gauche==true) image(ContHG, x*50, y*50);
        if (Bas==true && Droite==true) image(ContBD, x*50, y*50);
        if (Bas==true && Gauche==true) image(ContBG, x*50, y*50);

        //Remise a 0 de la détection des tiles autours du blocs de lave
        Bas= false;
        Haut= false;
        Droite= false;
        Gauche= false;
      }//Couleur Lave

      //Foret/arbre en bas pour recouvrir les tank
      if (Collision [A] ==4) image(arbre, x*50, y*50);
      //Couleur Foret
    }
  }
  //Affiche les terrains proposées en barre d'info
  fill(45, 139, 97);
  rect(20, 505, 50, 50);
  image(Montagne, 100, 505);
  image(Eau, 180, 505);
  image(Lave, 260, 505);
  image(arbre, 340, 505);

  //Affichage selection dans la barre d'info lors du choix de la texture
  if (Selectile!=0) {
    PImage STile; 
    STile = loadImage("Selection Tank2.png");
    image(STile, Selectile*80-60, 505);
  }
  //Affichage curseur sur la map pour le changement des textures
  if (Selectile==0) {
    PImage STile; 
    STile = loadImage("Selection Tank2.png");
    image(STile, XCursorEdit*50, YCursorEdit*50);
  }
}