/*
v. 1.2.1, 03/02/19 à 19h34, Benjamin
 
 Changelog :
 
 - Ajout de nouvelles options
 
 */
String GameName = "Tank Game";
int Player = 0; //Joueur 1 et 2 changement
int Act = 0;
int xbase = 0; // Emplacement tank 1
int ybase = 0;
int xbase2 = 450; // Emplacement tank 2
int ybase2 = 450;
int vietank1 = 5; //Vie des tanks
int vietank2 = 5;
int Direction = 2; //Direction des sprites des tanks
int Direction2 = 2;
float CP = 0; //Compteur Placement
int turn=0; //Un décompte de random éffectué
int arrows=0; //Empèche le joueur de maintenir les flèches pour se déplacer ( un appui = un déplacement )
int choix=0; //Validation Choix
int choix2=0;//Choix entre Attaque ou Déplacement
int choix3=0;//Anti Enter*2 ( effet d'un key pressed pour enter car non ascii)
int xbasem = 0; // Emplacement balle
int ybasem = 0;
float CB = 0; //Compteur Balle
int MLock = 0;
int lock=0; //touche de tire vérouillée
int lock2=0; //direction du tir
int lock3=0;//Anti Enter*2 ( effet d'un key pressed pour enter car non ascii)
int TestCadriD=0;//Test cadrillage renvoie 0 ou 1 => Si on peux passer ou pas
int TD2 = 0 ;
boolean Bas= false; //Variable détectant si plusieurs bord existes pour un angle (texture)
boolean Haut= false;
boolean Droite= false;
boolean Gauche= false;
boolean end = false;
String toshow = "Menu";
int Menu=1;

// Parties valeurs MenuEditeur
int Selectile=0;
int Selectedtile=0;
int LockTile=0;
int XCursorEdit=0;
int YCursorEdit=0;

//MenuMaps
JSONObject Map1;
JSONObject Map2;
JSONObject Map3;
//Interac(tion)Map permet de définir s'il s'agit d'une lecture (0) ou d'une écriture de map
int InteracMap = 0; 
//Annonce quelle map est sélectione
int SelectMap = 1;

//Menu option
int MenuOpt = 0;
int SMenuOpt = 1;
int MusicVOL = 50;
int SoundVOL = 50;
int TypeDeSon = 1;
int Design = 1;
//Permet d'accéder au parametres de son en jeu
int Link =0;

//MusicBackground
int FrameRate = 60;
int DecompteMusique = 19 * FrameRate + 1;

//Maps de base lorsqu'on édite une map dans le menu editeur
/*int [] Collision = {
 0, 2, 2, 4, 4, 0, 0, 1, 1, 3, 
 0, 2, 2, 2, 4, 4, 0, 0, 0, 3, 
 0, 1, 2, 2, 0, 0, 0, 3, 0, 0, 
 0, 1, 2, 2, 2, 0, 0, 0, 1, 1, 
 0, 0, 2, 2, 2, 2, 0, 0, 0, 1, 
 1, 0, 0, 0, 2, 2, 2, 2, 0, 0, 
 1, 1, 0, 0, 0, 2, 2, 2, 1, 0, 
 0, 0, 3, 0, 0, 0, 2, 2, 1, 0, 
 3, 0, 0, 0, 4, 4, 2, 2, 2, 0, 
 3, 1, 1, 0, 0, 4, 4, 2, 2, 0
 };*/
int [] Collision = {
  0, 1, 2, 3, 4, 0, 0, 0, 0, 0, 
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0
};
PImage Montagne, Eau, Eauhaut, Eaubas, Eaugauche, Eaudroite, Eauhetd, Eauhetg, Eaubetd, Eaubetg, Lave, Lavehaut, Lavebas, Lavegauche, Lavedroite, Lavehetd, Lavehetg, Lavebetd, Lavebetg;
PImage arbre, STank1, STank2, Tank1, Tank1u, Tank1d, Tank1r, Tank1l, Tank2, Tank2u, Tank2d, Tank2r, Tank2l, Vies, Balle, BalleU, BalleD, BalleR, BalleL, BalleExplosion;
import processing.sound.*; 
SoundFile Fire; 
SoundFile Move; 
SoundFile MusicBackground;

void setup() {
  size(500, 550);
  background(0);
  //A changer pour changer la rapidité du jeu
  frameRate(60);

  Montagne = loadImage("Montagne.png");
  Eau = loadImage("Eau.png");
  Eauhaut = loadImage("Lavehaut.png");
  Eaubas = loadImage("Lavebas.png");
  Eaugauche = loadImage("Lavegauche.png");
  Eaudroite = loadImage("Lavedroite.png");
  Eauhetd = loadImage("Lavehaut+droite.png");
  Eauhetg = loadImage("Lavehaut+gauche.png");
  Eaubetd = loadImage("Lavebas+droite.png");
  Eaubetg = loadImage("Lavebas+gauche.png");
  Lave = loadImage("Lave.png");
  Lavehaut = loadImage("Lavehaut.png");
  Lavebas = loadImage("Lavebas.png");
  Lavegauche = loadImage("Lavegauche.png");
  Lavedroite = loadImage("Lavedroite.png");
  Lavehetd = loadImage("Lavehaut+droite.png");
  Lavehetg = loadImage("Lavehaut+gauche.png");
  Lavebetd = loadImage("Lavebas+droite.png");
  Lavebetg = loadImage("Lavebas+gauche.png");

  arbre = loadImage("arbre.png");
  STank1 = loadImage("Selection Tank1.png");
  STank2 = loadImage("Selection Tank2.png");
  Tank1u = loadImage("Tank1u.png");
  Tank1d = loadImage("Tank1d.png");
  Tank1l = loadImage("Tank1l.png");
  Tank1r = loadImage("Tank1r.png");
  Tank2u = loadImage("Tank2u.png");
  Tank2d = loadImage("Tank2d.png");
  Tank2l = loadImage("Tank2l.png");
  Tank2r = loadImage("Tank2r.png");
  Vies = loadImage("Vies.png");
  BalleU = loadImage("BalleU.png");
  BalleD = loadImage("BalleD.png");
  BalleR = loadImage("BalleR.png");
  BalleL = loadImage("BalleL.png");
  BalleExplosion = loadImage("Explosion.png");

  Fire = new SoundFile(this, "tankfire.wav");
  Move = new SoundFile(this, "Move.wav");
  MusicBackground = new SoundFile(this, "MusicBackground.wav");
}
void CDD() {
  //Cadrillage Des Déplacements (Tanks)
  int CDDx = xbase/50;
  int CDDy = ybase/50*10;
  int CDD = CDDx + CDDy;

  //Colisions cotés de terrain (Déplacements)        si le tank rencontre la limite et qu'il se trouve sur de l'eau CP a besoin de +2 pour revenir a son etat initial
  if (CDDx<0) {
    CDD=CDD+1;
    xbase=xbase+50;
    CP=CP+1;
    if (Collision [CDD] ==2) CP=CP+1;
  }
  if (CDDy<0) {
    CDD=CDD+10;
    ybase=ybase+50;
    CP=CP+1;
    if (Collision [CDD] ==2) CP=CP+1;
  }
  if (CDDx>9) {
    CDD=CDD-1;
    xbase=xbase-50;
    CP=CP+1;
    if (Collision [CDD] ==2) CP=CP+1;
  }
  if (CDDy>90) {
    CDD=CDD-10;
    ybase=ybase-50;
    CP=CP+1;
    if (Collision [CDD] ==2) CP=CP+1;
  }


  //Si le tank veux aller dans un endroit qu'il ne peux traverser (Montagne)
  if (Collision [CDD] ==1) {
    TestCadriD=0;
    TD2=1;
  }
  //Si le tank veux aller dans un endroit qu'il ne peux traverser (Lave)
  if (Collision [CDD] ==3) {
    TestCadriD=0;
    TD2=1;
  }
  //Si le tank va dans l'eau (Il est alors ralenti)
  if (Collision [CDD] ==2) CP=CP-1;
}
void CDD2() {
  //Cadrillage Des Déplacements (Tanks)
  int CDDx = xbase2/50;
  int CDDy = ybase2/50*10;
  int CDD = CDDx + CDDy;

  //Colisions cotés de terrain (Déplacements)        si le tank rencontre la limite et qu'il se trouve sur de l'eau CP a besoin de +2 pour revenir a son etat initial
  if (CDDx<0) {
    CDD=CDD+1;
    xbase2=xbase2+50;
    CP=CP+1;
    if (Collision [CDD] ==2) CP=CP+1;
  }
  if (CDDy<0) {
    CDD=CDD+10;
    ybase2=ybase2+50;
    CP=CP+1;
    if (Collision [CDD] ==2) CP=CP+1;
  }
  if (CDDx>9) {
    CDD=CDD-1;
    xbase2=xbase2-50;
    CP=CP+1;
    if (Collision [CDD] ==2) CP=CP+1;
  }
  if (CDDy>90) {
    CDD=CDD-10;
    ybase2=ybase2-50;
    CP=CP+1;
    if (Collision [CDD] ==2) CP=CP+1;
  }


  //Si le tank veux aller dans un endroit qu'il ne peux traverser (Montagne)
  if (Collision [CDD] ==1) {
    TestCadriD=0;
    TD2=1;
  }
  //Si le tank veux aller dans un endroit qu'il ne peux traverser (Lave)
  if (Collision [CDD] ==3) {
    TestCadriD=0;
    TD2=1;
  }
  //Si le tank va dans l'eau (Il est alors ralenti)
  if (Collision [CDD] ==2) CP=CP-1;
}
void CDA() {
  //Cadrillage Des Attaques (Bullets)
  int CDAx = xbasem/50;
  int CDAy = ybasem/50*10;
  int CDA = CDAx + CDAy;

  //Colisions cotés de terrain (Attaque)
  if (CDAx<0) {
    CDA=CDA+1;
    CB=0;
  }
  if (CDAy<0) {
    CDA=CDA+10;
    CB=0;
  }
  if (CDAx>9) {
    CDA=CDA-1;
    CB=0;
  }
  if (CDAy>90) {
    CDA=CDA-10;
    CB=0;
  }

  //Si le tank veux aller dans un endroit qu'il ne peux traverser (Montagne)
  if (Collision [CDA] ==1) CB=0;
  //Si le tank veux aller dans un endroit qu'il ne peux traverser (Foret)
  if (Collision [CDA] ==4) CB=0;
}


void AffTank () {//Affiche le tank

  delay(50);
  background(45, 139, 97);
  //Affichage barre d'info
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
      if (Collision [A] == 1) image(Montagne, x*50, y*50);
      //Couleur Roche
      if (Collision [A] == 2) {
        //Eau
        image(Eau, x*50, y*50);
        //rebors eau
        if (A>10 && Collision [A-10] !=2) {
          image(Eauhaut, x*50, y*50);
          Haut=true;
        }
        if (A<90 && Collision [A+10] !=2) {
          image(Eaubas, x*50, y*50);
          Bas=true;
        }
        if (A!=0 && A!=10 && A!=20 && A!=30 && A!=40 && A!=50 && A!=60 && A!=70 && A!=80 && A!=90 && Collision [A-1] !=2) {
          image(Eaugauche, x*50, y*50);
          Gauche=true;
        }
        if (A!=9 &&A!=19 && A!=29 && A!=39 && A!=49 && A!=59 && A!=69 && A!=79 && A!=89 && A!=99 && Collision [A+1] !=2) {
          image(Eaudroite, x*50, y*50);
          Droite=true;
        }

        //Coins/angles lave
        if (Haut==true && Droite==true) image(Eauhetd, x*50, y*50);
        if (Haut==true && Gauche==true) image(Eauhetg, x*50, y*50);
        if (Bas==true && Droite==true) image(Eaubetd, x*50, y*50);
        if (Bas==true && Gauche==true) image(Eaubetg, x*50, y*50);

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
          image(Lavehaut, x*50, y*50);
          Haut=true;
        }
        if (A<90 && Collision [A+10] !=3) {
          image(Lavebas, x*50, y*50);
          Bas=true;
        }
        if (A!=0 && A!=10 && A!=20 && A!=30 && A!=40 && A!=50 && A!=60 && A!=70 && A!=80 && A!=90 && Collision [A-1] !=3) {
          image(Lavegauche, x*50, y*50);
          Gauche=true;
        }
        if (A!=9 &&A!=19 && A!=29 && A!=39 && A!=49 && A!=59 && A!=69 && A!=79 && A!=89 && A!=99 && Collision [A+1] !=3) {
          image(Lavedroite, x*50, y*50);
          Droite=true;
        }

        //Coins/angles lave
        if (Haut==true && Droite==true) image(Lavehetd, x*50, y*50);
        if (Haut==true && Gauche==true) image(Lavehetg, x*50, y*50);
        if (Bas==true && Droite==true) image(Lavebetd, x*50, y*50);
        if (Bas==true && Gauche==true) image(Lavebetg, x*50, y*50);

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

  //Selection entourage tank
  if (Player==1) image(STank1, xbase, ybase);
  if (Player==2) image(STank2, xbase2, ybase2);


  //Affichage Tank
  if (Direction == 1) { 
    Tank1 = Tank1u; 
    image(Tank1, xbase, ybase);
  }
  if (Direction == 2) { 
    Tank1 = Tank1d; 
    image(Tank1, xbase, ybase);
  }
  if (Direction == 3) { 
    Tank1 = Tank1l; 
    image(Tank1, xbase, ybase);
  }
  if (Direction == 4) { 
    Tank1 = Tank1r; 
    image(Tank1, xbase, ybase);
  }

  if (Direction2 == 1) { 
    Tank2 = Tank2u; 
    image(Tank2, xbase2, ybase2);
  }
  if (Direction2 == 2) { 
    Tank2 = Tank2d; 
    image(Tank2, xbase2, ybase2);
  }
  if (Direction2 == 3) { 
    Tank2 = Tank2l; 
    image(Tank2, xbase2, ybase2);
  }
  if (Direction2 == 4) { 
    Tank2 = Tank2r; 
    image(Tank2, xbase2, ybase2);
  }


  //Affichage des vies
  fill(255);
  textSize(14);
  text("V1:", 20, 530);
  text(":V2", 460, 530);
  for (int viebarre1 = vietank1; viebarre1>0; viebarre1--) {
    fill(150, 32, 32);
    image(Vies, 12*viebarre1+40, 523, 8, 8);
  }
  for (int viebarre2 = vietank2; viebarre2>0; viebarre2--) {
    fill(150, 32, 32);
    image(Vies, -12*viebarre2+460, 523, 8, 8);
  }

  //Affichage de la Commande pour accéder aux options en jeu
  textAlign(CENTER);
  fill(255);
  text("Press Shift", 250, 520);
  text("For Options", 250, 540);
  textAlign(LEFT);
}

void draw() {

  if (toshow == "Menu") Menu();
  if (toshow == "MenuPlay") MenuPlay();
  if (toshow == "MenuEditor") MenuEditor();
  if (toshow == "MenuOption") MenuOption();
  if (toshow == "Game") Game();
  if (toshow == "ServerJoin") ServerJoin();
  if (toshow == "ServerCreate") ServerCreate();
  if (toshow == "MenuMaps") MenuMaps();
  if (toshow == "Options") Options();
  MusicBackground();

}

void MusicBackground(){
  
  //Volume du son
  MusicBackground.amp((float)MusicVOL/1000);
  //Boucle musique de fond
  DecompteMusique--;
  if (DecompteMusique<0 || DecompteMusique==(19*FrameRate)) {
    MusicBackground.play();
    DecompteMusique=(19*FrameRate);
      }
}

void Game() {
  Move.amp((float)SoundVOL/1000);
  Fire.amp((float)SoundVOL/1000);

  textAlign(LEFT);
  if (Player==0 && Act==0 && vietank1>0 && vietank2>0 || Player==2 && Act==0 && vietank1>0 && vietank2>0) {
    background(0);
    //textSize(40);
    //text("Player 1", 160, 220);
    //text("Press Down", 130, 270);
    stroke(0);
    fill(0, 0, 255);
    textSize(40);
    text("Player 1", 160, 220);
    text("Press Down", 130, 270);
    if (keyPressed==true && keyCode==DOWN) {
      Player=1; 
      Act=3;
      if (IsMulti == true) {
        dataO.setInt("tour", 1);
        data.setJSONObject(4, dataO);
      }
    }
  }

  if (Player==1 && Act==0 && vietank1>0 && vietank2>0) {
    background(0);  
    fill(255, 0, 0);
    textSize(40);
    text("Player 2", 160, 220);
    text("Press Down", 130, 270);
    if (keyPressed==true && keyCode==DOWN) {
      Player=2; 
      Act=3;
      if (IsMulti == true) {
        dataO.setInt("tour", 2);
        data.setJSONObject(4, dataO);
      }
    }
  }

  if (vietank1<1) {
    background(0);
    fill(255, 0, 0);
    textSize(40);
    text("Player 2 WIN", 130, 220);
    if (IsMulti == true) {
      dataO.setInt("winner", 2);
      data.setJSONObject(6, dataO);
    }
  }
  if (vietank2<1) {
    background(0);
    fill(0, 0, 255);
    textSize(40);
    text("Player 1 WIN", 130, 220);
    if (IsMulti == true) {
      dataO.setInt("winner", 1);
      data.setJSONObject(6, dataO);
    }
  }
  //début modification (et sécurité ctrl + Z)
  if (Act>0) {

    AffTank();

    if (choix==0) {//Choix des actions (Left=Shoot/Right=Move)

      if (keyCode==LEFT) {//Lorsque le curseur est sur Shoot
        choix2=1;
        choix3=1;
        fill(255, 255, 255, 100);//Souligne en rouge le choix Left
        rect(55, 227, 180, 30);
      }

      if (keyCode==RIGHT) {//Lorsque le curseur est sur Move
        choix2=2;
        choix3=1;
        fill(255, 255, 255, 100);//Souligne en rouge le choix Right
        rect(263, 227, 180, 30);
      }

      if (choix3==1 && keyCode==ENTER) {
        choix=choix2;
        choix3=0;
      }//Lorsque l'action est choisie par Enter


      //Affichage du choix des Actions (shoot ou move)
      fill(0, 0, 0, 125);
      rect(0, 175, 500, 140);
      
      fill(0, 0, 0, 65);
      rect(0, 175+140, 500, 500-(175+140));
      rect(0, 0, 500, 175);
      
      fill(255, 255, 255, 30);
      rect(0, 175+140, 500, 3);
      rect(0, 172, 500, 3);
      
      textAlign(CENTER);
      textSize(45);
      fill(255, 255, 255, 200);
      ellipse(480, 190, 15, 15);
      if (Player==1)fill(0, 0, 255);
      if (Player==2)fill(255, 0, 0);
      ellipse(480, 190, 10, 10);
      
      textSize(23);
      fill(250, 250, 250, 255);
      text("Left(for Attack)     Right(for move)", 250, 250);
      fill(255);
      textSize(20);
      text("Press arrow", 250, 200);
      text("And then press Enter", 250, 300);
      textAlign(LEFT);
    }


    if (choix==1) {//Shoot

      if (CB<1 || lock==0) {
        CB = random(10);
        CB = int(CB);
        println(CB);
        if (IsMulti == true) {
          dataO.setInt("DistFeu", int(CB));
          if (Player == 1) data.setJSONObject(1, dataO);
          if (Player == 2) data.setJSONObject(2, dataO);
        }

        if (Player == 1) {
          xbasem=xbase;
          ybasem=ybase;
        }
        if (Player == 2) {
          xbasem=xbase2;
          ybasem=ybase2;
        }

        AffTank();

        fill(200);
        textSize(20);
        text("Press arrows to shoot your bullet in a direction", 30, 430);
        text("Then press Enter", 180, 480);

        if ( keyCode==UP) {
          lock2=1;
          lock3=1;
          if (Player == 1) triangle(xbase+10, ybase-10, xbase+40, ybase-10, xbase+25, ybase-30);
          if (Player == 1) Direction=1;
          if (Player == 2) triangle(xbase2+10, ybase2-10, xbase2+40, ybase2-10, xbase2+25, ybase2-30);
          if (Player == 2) Direction2=1;
        }
        if ( keyCode==DOWN) {
          lock2=2;
          lock3=1;
          if (Player == 1) triangle(xbase+10, ybase+60, xbase+40, ybase+60, xbase+25, ybase+80);
          if (Player == 1) Direction=2;
          if (Player == 2) triangle(xbase2+10, ybase2+60, xbase2+40, ybase2+60, xbase2+25, ybase2+80);
          if (Player == 2) Direction2=2;
        }
        if ( keyCode==LEFT) {
          lock2=3;
          lock3=1;
          if (Player == 1) triangle(xbase-10, ybase+10, xbase-10, ybase+40, xbase-30, ybase+25);
          if (Player == 1) Direction=3;
          if (Player == 2) triangle(xbase2-10, ybase2+10, xbase2-10, ybase2+40, xbase2-30, ybase2+25);
          if (Player == 2) Direction2=3;
        }
        if ( keyCode==RIGHT) {
          lock2=4;
          lock3=1;
          if (Player == 1) triangle(xbase+60, ybase+10, xbase+60, ybase+40, xbase+80, ybase+25);
          if (Player == 1) Direction=4;
          if (Player == 2) triangle(xbase2+60, ybase2+10, xbase2+60, ybase2+40, xbase2+80, ybase2+25);
          if (Player == 2) Direction2=4;
        }
        if (lock3==1 && keyCode==ENTER) {
          Fire.play(3);
          lock=lock2;
          lock3=0;
          if (IsMulti == true) {
            dataO.setBoolean("Feu", true);
            if (Player == 1) data.setJSONObject(1, dataO);
            if (Player == 2) data.setJSONObject(2, dataO);
          }
        }

        if (IsMulti == true) {
          if (Player == 1) {
            dataO.setInt("Direction", Direction);
            data.setJSONObject(1, dataO);
          }
          if (Player == 2) {
            dataO.setInt("Direction", Direction2);
            data.setJSONObject(2, dataO);
          }
        }
      }

      if (CB>0 && lock!=0) {

        CB=CB-1;

        if (lock==1) {
          ybasem=ybasem-50;
          CDA();
        }
        if (lock==2) {
          ybasem=ybasem+50;
          CDA();
        }
        if (lock==3) {
          xbasem=xbasem-50;
          CDA();
        }
        if (lock==4) {
          xbasem=xbasem+50;
          CDA();
        }
        if (Player == 1) {
          if (xbasem==xbase2 && ybasem==ybase2) {
            CB=0;
            vietank2=vietank2-1;
          }
        }
        if (Player == 2) {
          if (xbasem==xbase && ybasem==ybase) {
            CB=0;
            vietank1=vietank1-1;
          }
        }

        AffTank();
        if (lock==1) {
          Balle = BalleU;
          image(Balle, xbasem, ybasem);
        }
        if (lock==2) {
          Balle = BalleD;
          image(Balle, xbasem, ybasem);
        }
        if (lock==3) {
          Balle = BalleL;
          image(Balle, xbasem, ybasem);
        }
        if (lock==4) {
          Balle = BalleR;
          image(Balle, xbasem, ybasem);
        }
        fill(200);
        textSize(50);
        text(CB, 450, 490, 500);
      }

      if (CB<1 && lock!=0) {
        choix=0;
        lock=0;
        AffTank();
        Balle =  BalleExplosion;
        image(Balle, xbasem, ybasem);
        Act=Act-1;
      }
    }
  }


  if (choix==2) {//Move
    println(CP);
    //Initialisation du dès de déplacements
    if (CP<1) {
      CP = random(10);
      CP = int(CP);
      println(CP);
    }

    //Déplacements lorsque CP est != de 0 (Joueur a encore des déplacements)
    if (CP>0) {
      if (keyPressed==true && keyCode==UP /*&& arrows==0*/) {
        if (Player == 1) ybase= ybase-50;
        if (Player == 2) ybase2 = ybase2-50;
        CP=CP-1;
        if (Player == 1) CDD();
        if (Player == 2) CDD2();
        if (Player == 1) Direction=1;/*arrows=1;*/
        if (Player == 2) Direction2 = 1;
        Move.play();
      }
      if (keyPressed==true && keyCode==DOWN /*&& arrows==0*/) {
        if (Player == 1) ybase= ybase+50;
        if (Player == 2) ybase2 = ybase2+50;
        CP=CP-1;
        if (Player == 1) CDD();
        if (Player == 2) CDD2();
        if (Player == 1) Direction=2;/*arrows=1;*/
        if (Player == 2) Direction2=2;
        Move.play();
      }
      if (keyPressed==true && keyCode==LEFT /*&& arrows==0*/) {
        if (Player == 1) xbase= xbase-50;
        if (Player == 2) xbase2= xbase2-50;
        CP=CP-1;
        if (Player == 1) CDD();
        if (Player == 2) CDD2();
        if (Player == 1) Direction=3;/*arrows=1;*/
        if (Player == 2) Direction2=3;
        Move.play();
      }
      if (keyPressed==true && keyCode==RIGHT /*&& arrows==0*/) {
        if (Player == 1) xbase= xbase+50;
        if (Player == 2) xbase2= xbase2+50;
        CP=CP-1;
        if (Player == 1) CDD();
        if (Player == 2) CDD2();
        if (Player == 1) Direction=4;/*arrows=1;*/
        if (Player == 2) Direction2=4;
        Move.play();
      }
      //if (keyPressed==false && arrows==1){arrows=0;}

      if (keyCode==UP && TestCadriD==0) {
        if (Player == 1) ybase= ybase+50;
        if (Player == 2) ybase2= ybase2+50;
        CP=CP+1;
        TestCadriD=1;
      }
      if (keyCode==DOWN && TestCadriD==0) {
        if (Player == 1) ybase= ybase-50;
        if (Player == 2) ybase2= ybase2-50;
        CP=CP+1;
        TestCadriD=1;
      }
      if (keyCode==LEFT && TestCadriD==0) {
        if (Player == 1) xbase= xbase+50;
        if (Player == 2) xbase2= xbase2+50;
        CP=CP+1;
        TestCadriD=1;
      }
      if (keyCode==RIGHT && TestCadriD==0) {
        if (Player == 1) xbase= xbase-50;
        if (Player == 2) xbase2= xbase2-50;
        CP=CP+1;
        TestCadriD=1;
      }
      if (IsMulti == true) {
        if (Player == 1) {
          dataO.setInt("PosX", xbase);
          dataO.setInt("PosY", ybase);
          data.setJSONObject(1, dataO);
        }
        if (Player == 2) {
          dataO.setInt("PosX", xbase2);
          dataO.setInt("PosY", ybase2);
          data.setJSONObject(2, dataO);
        }
      }

      AffTank();
      fill(200);

      textSize(50);
      text(CP, 450, 490, 500);
      println(CP);
    }

    //Déplacements lorsque CP est inférieur à 0 (Joueur n'a plus de déplacements)
    if (CP<1) {
      choix=0;
      Act=Act-1;
    }
  }
}