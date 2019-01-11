/*
/!\Il y a des éléments spécifiques à cet affichage (bien qu'il faille faire le tri) /!\
 Affichages des tanks ne doit pas se faire par exemple d'ou le AffEditeur
 
 */

void Menu2() {
  AffEditeur();

  //Enter permet d'accéder au choix des types de terrains (ex:montagne,lave...) qui vont remplacer ceux choisit par le curseur  
  if (keyCode==ENTER && Selectile==0 && LockTile==0) {
    Selectile=1;
    LockTile=1;
  }
  if (keyCode==ENTER && Selectile!=0 && LockTile==0) {
    Selectedtile=Selectile-1;
    Selectile=0;
    LockTile=1;
  }
  //A changer plus tard (Force le joueur a choisir une texture avec les fleches avant de valider
  if (keyPressed==true) {
    LockTile=0;
  }

  //Déplacement du curseur
  if (keyPressed==true && keyCode==LEFT && Selectile==0 && XCursorEdit!=0) {
    XCursorEdit--;
  }
  if (keyPressed==true && keyCode==RIGHT && Selectile==0 && XCursorEdit!=9) {
    XCursorEdit++;
  }
  if (keyPressed==true && keyCode==UP && Selectile==0 && YCursorEdit!=0) {
    YCursorEdit--;
  }
  if (keyPressed==true && keyCode==DOWN && Selectile==0 && YCursorEdit!=9) {
    YCursorEdit++;
  }

  if (keyPressed==true && keyCode==LEFT && Selectile!=0 && Selectile!=1) {
    Selectile--;
  }
  if (keyPressed==true && keyCode==RIGHT && Selectile!=0 && Selectile!=5) {
    Selectile++;
  }

  //Remplace le terrain choisit par le curseur par celui choisit dans la barre d'info (En appuyant sur Shift)
  if (keyPressed==true && keyCode==SHIFT && Selectile==0) {
    Collision [XCursorEdit+YCursorEdit*10] =Selectedtile;
  }
}

void AffEditeur () {//Affiche l'éditeur
  delay(50);
  background(45, 139, 97);
  fill(0);
  rect(0, 500, 500, 50);
  fill(200);
  rect(0, 500, 500, 3);
  noStroke();

  for (int x=0; x<10; x++) {
    for (int y=0; y<10; y++) {
      int Ax = x;
      int Ay = y*10;
      int A = Ax + Ay;
      if (Collision [A] ==1) {
        PImage Montagne;
        Montagne = loadImage("Montagne.png");
        image(Montagne, x*50, y*50);
      }//Couleur Roche
      if (Collision [A] ==2) {
        //Eau
        PImage Eau; 
        Eau = loadImage("Eau.png");
        image(Eau, x*50, y*50);

        //rebors eau
        if (A>10 && Collision [A-10] !=2) {
          PImage Eauhaut; 
          Eauhaut = loadImage("Lavehaut.png");
          image(Eauhaut, x*50, y*50);
          Haut=true;
        }
        if (A<90 && Collision [A+10] !=2) {
          PImage Eaubas; 
          Eaubas = loadImage("Lavebas.png");
          image(Eaubas, x*50, y*50);
          Bas=true;
        }
        if (A!=0 && A!=10 && A!=20 && A!=30 && A!=40 && A!=50 && A!=60 && A!=70 && A!=80 && A!=90 && Collision [A-1] !=2) {
          PImage Eaugauche; 
          Eaugauche = loadImage("Lavegauche.png");
          image(Eaugauche, x*50, y*50);
          Gauche=true;
        }
        if (A!=9 &&A!=19 && A!=29 && A!=39 && A!=49 && A!=59 && A!=69 && A!=79 && A!=89 && A!=99 && Collision [A+1] !=2) {
          PImage Eaudroite; 
          Eaudroite = loadImage("Lavedroite.png");
          image(Eaudroite, x*50, y*50);
          Droite=true;
        }

        //Coins/angles lave
        if (Haut==true && Droite==true) {
          PImage Eauhetd; 
          Eauhetd = loadImage("Lavehaut+droite.png");
          image(Eauhetd, x*50, y*50);
        }
        if (Haut==true && Gauche==true) {
          PImage Eauhetg; 
          Eauhetg = loadImage("Lavehaut+gauche.png");
          image(Eauhetg, x*50, y*50);
        }
        if (Bas==true && Droite==true) {
          PImage Eaubetd; 
          Eaubetd = loadImage("Lavebas+droite.png");
          image(Eaubetd, x*50, y*50);
        }
        if (Bas==true && Gauche==true) {
          PImage Eaubetg; 
          Eaubetg = loadImage("Lavebas+gauche.png");
          image(Eaubetg, x*50, y*50);
        }

        //Remise a 0 de la détection des tiles autours du blocs de lave
        Bas= false;
        Haut= false;
        Droite= false;
        Gauche= false;
      }//Couleur Eau

      if (Collision [A] ==3) {
        //Lave
        PImage Lave; 
        Lave = loadImage("Lave.png");
        image(Lave, x*50, y*50);
        //rebors lave
        if (A>10 && Collision [A-10] !=3) {
          PImage Lavehaut; 
          Lavehaut = loadImage("Lavehaut.png");
          image(Lavehaut, x*50, y*50);
          Haut=true;
        }
        if (A<90 && Collision [A+10] !=3) {
          PImage Lavebas; 
          Lavebas = loadImage("Lavebas.png");
          image(Lavebas, x*50, y*50);
          Bas=true;
        }
        if (A!=0 && A!=10 && A!=20 && A!=30 && A!=40 && A!=50 && A!=60 && A!=70 && A!=80 && A!=90 && Collision [A-1] !=3) {
          PImage Lavegauche; 
          Lavegauche = loadImage("Lavegauche.png");
          image(Lavegauche, x*50, y*50);
          Gauche=true;
        }
        if (A!=9 &&A!=19 && A!=29 && A!=39 && A!=49 && A!=59 && A!=69 && A!=79 && A!=89 && A!=99 && Collision [A+1] !=3) {
          PImage Lavedroite; 
          Lavedroite = loadImage("Lavedroite.png");
          image(Lavedroite, x*50, y*50);
          Droite=true;
        }

        //Coins/angles lave
        if (Haut==true && Droite==true) {
          PImage Lavehetd; 
          Lavehetd = loadImage("Lavehaut+droite.png");
          image(Lavehetd, x*50, y*50);
        }
        if (Haut==true && Gauche==true) {
          PImage Lavehetg; 
          Lavehetg = loadImage("Lavehaut+gauche.png");
          image(Lavehetg, x*50, y*50);
        }
        if (Bas==true && Droite==true) {
          PImage Lavebetd; 
          Lavebetd = loadImage("Lavebas+droite.png");
          image(Lavebetd, x*50, y*50);
        }
        if (Bas==true && Gauche==true) {
          PImage Lavebetg; 
          Lavebetg = loadImage("Lavebas+gauche.png");
          image(Lavebetg, x*50, y*50);
        }

        //Remise a 0 de la détection des tiles autours du blocs de lave
        Bas= false;
        Haut= false;
        Droite= false;
        Gauche= false;
      }//Couleur Lave

      //Foret/arbre en bas pour recouvrir les tank
      if (Collision [A] ==4) {
        PImage arbre; 
        arbre = loadImage("arbre.png");
        image(arbre, x*50, y*50);
      }//Couleur Foret
    }
  }
  //Affiche les terrains proposées en barre d'info
  fill(45, 139, 97);
  rect(60, 505, 50, 50);
  PImage Montagne;
  Montagne = loadImage("Montagne.png");
  image(Montagne, 140, 505);
  PImage Eau; 
  Eau = loadImage("Eau.png");
  image(Eau, 220, 505);
  PImage Lave; 
  Lave = loadImage("Lave.png");
  image(Lave, 300, 505);
  PImage arbre; 
  arbre = loadImage("arbre.png");
  image(arbre, 380, 505);

  //Affichage selection dans la barre d'info lors du choix de la texture
  if (Selectile!=0) {
    PImage STile; 
    STile = loadImage("Selection Tank2.png");
    image(STile, Selectile*80-20, 505);
  }
  //Affichage curseur sur la map pour le changement des textures
  if (Selectile==0) {
    PImage STile; 
    STile = loadImage("Selection Tank2.png");
    image(STile, XCursorEdit*50, YCursorEdit*50);
  }
}
