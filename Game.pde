/*
v. 1.3.3, 01/03/19 à 17h30, Nathan
 
 Changelog :
 
 - Ajout d'un timer (décompte final) :
   - Modification des options pour rajouter sa case
   - Possibilité de régler les minutes et secondes
   - Affiché in game
   - Quand plus de temps, le gagnant est celui qui a le plus de vie
 - Ajout de la possibilité d'une égalité (si timer écoulé & les deux on la même vie)
 
 */
int Player = 0; //Joueur 1 et 2 changement
int Act = 0;
int xbase = 0; // Emplacement tank 1 (0, 0)
int ybase = 0;
int xbase2 = 450; // Emplacement tank 2 (450, 450)
int ybase2 = 450;
int DefaultVie = 5; //Vie des tanks par défaut
int vietank1 = DefaultVie; //Vie des tanks
int vietank2 = DefaultVie;
int Direction = 2; //Direction des sprites des tanks
int Direction2 = 2;
int CP = 0; //Compteur Placement
int turn=0; //Un décompte de random éffectué
int arrows=0; //Empèche le joueur de maintenir les flèches pour se déplacer ( un appui = un déplacement )
int choix=0; //Validation Choix
int choix2=0;//Choix entre Attaque ou Déplacement
int choix3=0;//Anti Enter*2 ( effet d'un key pressed pour enter car non ascii)
int xbasem = 0; // Emplacement balle
int ybasem = 0;
int CB = 0; //Compteur Balle
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
boolean bord = false;
boolean DegatsLaveTank=false;
int ChangementSaison = 0;
boolean Changementok = false ;

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
int MusicVOL = 1; //  <---------------------------------------------------------------------
int SoundVOL = 50;
int TSel = 1;
int TypeDeSon = 1;
int Design = 1;
int SummerDay = 1 ;
int WinterDay = 1 ;
int DefaultMin = 5, DefaultSec = 0;
//Permet d'accéder au parametres de son en jeu
int Link = 0;

int TimerSec = DefaultSec, TimerMin = DefaultMin;
int ComptTimer;

//MusicBackground
int FrameRate = 60;
int DecompteMusique = 19 * FrameRate + 1;

//Maps de base lorsqu'on édite une map dans le menu editeur
//int [] Collision = {
//  0, 2, 2, 4, 4, 0, 0, 1, 1, 3, 
//  0, 2, 2, 2, 4, 4, 0, 0, 0, 3, 
//  0, 1, 2, 2, 0, 0, 0, 3, 0, 0, 
//  0, 1, 2, 2, 2, 0, 0, 0, 1, 1, 
//  0, 0, 2, 2, 2, 2, 0, 0, 0, 1, 
//  1, 0, 0, 0, 2, 2, 2, 2, 0, 0, 
//  1, 1, 0, 0, 0, 2, 2, 2, 1, 0, 
//  0, 0, 3, 0, 0, 0, 2, 2, 1, 0, 
//  3, 0, 0, 0, 4, 4, 2, 2, 2, 0, 
//  3, 1, 1, 0, 0, 4, 4, 2, 2, 0
//};
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
//Chargement des images du jeu
PImage BackgMenu, BackOpt, Credits;
PImage arbre, Montagne, Eau, Lave, ContH, ContB, ContG, ContD, ContHD, ContHG, ContBD, ContBG;
PImage arbreW, MontagneW, EauW, LaveW, ContHW, ContBW, ContGW, ContDW, ContHDW, ContHGW, ContBDW, ContBGW;
PImage STank1, STank2, Tank1, Tank1u, Tank1d, Tank1r, Tank1l, Tank2, Tank2u, Tank2d, Tank2r, Tank2l, Vies, Balle, BalleU, BalleD, BalleR, BalleL, BalleExplosion;
import processing.sound.*; 
SoundFile Fire; 
SoundFile Move; 
SoundFile MusicBackground;

void setup() {
  size(500, 550);
  background(0);
  //A changer pour changer la rapidité du jeu
  frameRate(60);

  BackgMenu = loadImage("BackMenu.png");
  BackOpt = loadImage("Options.png");
  Credits = loadImage("Crédits.png");

  arbre = loadImage("arbre.png");
  Montagne = loadImage("Montagne.png");
  Eau = loadImage("Eau.png");
  Lave = loadImage("Lave.png");
  ContH = loadImage("Lavehaut.png");
  ContB = loadImage("Lavebas.png");
  ContG = loadImage("Lavegauche.png");
  ContD = loadImage("Lavedroite.png");
  ContHD = loadImage("Lavehaut+droite.png");
  ContHG = loadImage("Lavehaut+gauche.png");
  ContBD = loadImage("Lavebas+droite.png");
  ContBG = loadImage("Lavebas+gauche.png");

  arbreW = loadImage("arbreW.png");
  MontagneW = loadImage("MontagneW.png");
  EauW = loadImage("EauW.png");
  LaveW = loadImage("LaveW.png");
  ContHW = loadImage("LavehautW.png");
  ContBW = loadImage("LavebasW.png");
  ContGW = loadImage("LavegaucheW.png");
  ContDW = loadImage("LavedroiteW.png");
  ContHDW = loadImage("Lavehaut+droiteW.png");
  ContHGW = loadImage("Lavehaut+gaucheW.png");
  ContBDW = loadImage("Lavebas+droiteW.png");
  ContBGW = loadImage("Lavebas+gaucheW.png");

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
  //Permet de fixer des limites pour la glisse sur la glace
  bord = false;

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
  if (Collision [CDD] ==3 && Design == 1) {
    TestCadriD=0;
    TD2=1;
  }
  if (Collision [CDD] ==3 && Design == 2) {
    TestCadriD=1;
    TD2=1;
    vietank1--;
    DegatsLaveTank  =true;
  } else DegatsLaveTank=false;
  //Si le tank va dans l'eau (Il est alors ralenti)
  if (Collision [CDD] ==2 && Design ==1) CP=CP-1;
  //Si le Tank va sur la glace (Il glisse jusqu'à un rebord ou un terrain différent de la glace)
  if (Collision [CDD] ==2 && Design ==2) {

    while (Collision [CDD] ==2 && keyCode==RIGHT && bord ==false) {
      xbase=xbase+50; 
      if (xbase<=450)CDDx = xbase/50; 
      else { 
        bord = true ; 
        xbase=xbase-50;
      }
      CDD = CDDx + CDDy;
      if (Collision [CDD]==1) {
        bord = true ; 
        xbase=xbase-50;
      }
      AffTank();
    }

    while (Collision [CDD] ==2 && keyCode==LEFT && bord ==false) {
      xbase=xbase-50; 
      if (xbase>=0)CDDx = xbase/50; 
      else { 
        bord = true ; 
        xbase=xbase+50;
      }
      CDD = CDDx + CDDy;
      if (Collision [CDD]==1) {
        bord = true ; 
        xbase=xbase+50;
      }
      AffTank();
    }

    while (Collision[CDD] ==2 && keyCode==UP && bord ==false) {
      ybase=ybase-50; 
      if (ybase>=0)CDDy = ybase/50*10; 
      else { 
        bord = true ; 
        ybase=ybase+50;
      }
      CDD = CDDx + CDDy;
      if (Collision [CDD]==1) {
        bord = true ; 
        ybase=ybase+50;
      }
      AffTank();
    }

    while (Collision [CDD] ==2 && keyCode==DOWN && bord ==false) {
      ybase=ybase+50; 
      if (ybase<=450)CDDy = ybase/50*10; 
      else { 
        bord = true ; 
        ybase=ybase-50;
      }
      CDD = CDDx + CDDy;
      if (Collision [CDD]==1) {
        bord = true ; 
        ybase=ybase-50;
      }
      AffTank();
    }
  }
}

void CDD2() {
  //Cadrillage Des Déplacements (Tanks)
  int CDDx = xbase2/50;
  int CDDy = ybase2/50*10;
  int CDD = CDDx + CDDy;
  //Permet de fixer les bug sur les déplacements avec la glace
  bord = false;

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
  if (Collision [CDD] ==3 && Design == 1) {
    TestCadriD=0;
    TD2=1;
  }
  if (Collision [CDD] ==3 && Design == 2) {
    TestCadriD=1;
    TD2=1;
    vietank2--;
    DegatsLaveTank  =true;
  } else DegatsLaveTank=false;
  //Si le tank va dans l'eau (Il est alors ralenti)
  if (Collision [CDD] ==2 && Design ==1) CP=CP-1;
  //Si le Tank va sur la glace (Il glisse jusqu'à un rebord ou un terrain différent de la glace)
  if (Collision [CDD] ==2 && Design ==2) {

    while (Collision [CDD] ==2 && keyCode==RIGHT && bord ==false) {
      xbase2=xbase2+50; 
      if (xbase2<=450)CDDx = xbase2/50; 
      else { 
        bord = true ; 
        xbase2=xbase2-50;
      }
      CDD = CDDx + CDDy;
      if (Collision [CDD]==1) {
        bord = true ; 
        xbase2=xbase2-50;
      }
      AffTank();
    }

    while (Collision [CDD] ==2 && keyCode==LEFT && bord ==false) {
      xbase2=xbase2-50; 
      if (xbase2>=0)CDDx = xbase2/50; 
      else { 
        bord = true ; 
        xbase2=xbase2+50;
      }
      CDD = CDDx + CDDy;
      if (Collision [CDD]==1) {
        bord = true ; 
        xbase2=xbase2+50;
      }
      AffTank();
    }

    while (Collision[CDD] ==2 && keyCode==UP && bord ==false) {
      ybase2=ybase2-50; 
      if (ybase2>=0)CDDy = ybase2/50*10; 
      else { 
        bord = true ; 
        ybase2=ybase2+50;
      }
      CDD = CDDx + CDDy;
      if (Collision [CDD]==1) {
        bord = true ; 
        ybase2=ybase2+50;
      }
      AffTank();
    }

    while (Collision [CDD] ==2 && keyCode==DOWN && bord ==false) {
      ybase2=ybase2+50; 
      if (ybase2<=450)CDDy = ybase2/50*10; 
      else { 
        bord = true ; 
        ybase2=ybase2-50;
      }
      CDD = CDDx + CDDy;
      if (Collision [CDD]==1) {
        bord = true ; 
        ybase2=ybase2-50;
      }
      AffTank();
    }
  }
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
  if (Collision [CDA] ==1 && Design==2)Collision [CDA]=0;
  //Si le tank veux aller dans un endroit qu'il ne peux traverser (Foret)
  if (Collision [CDA] ==4) CB=0;
}


void AffTank () {//Affiche le tank

  delay(50);
  if (Design==1)background(45, 139, 97);
  if (Design==2)background(196, 247, 255);
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
      if (Collision [A] == 1 && Design==1) image(Montagne, x*50, y*50);
      if (Collision [A] == 1 && Design==2) image(MontagneW, x*50, y*50);
      //Couleur Roche
      if (Collision [A] == 2) {
        //Eau
        if (Design==1)image(Eau, x*50, y*50);
        if (Design==2)image(EauW, x*50, y*50);
        //rebors eau
        if (A>10 && Collision [A-10] !=2) {
          if (Design==1)image(ContH, x*50, y*50);
          if (Design==2)image(ContHW, x*50, y*50);
          Haut=true;
        }
        if (A<90 && Collision [A+10] !=2) {
          if (Design==1)image(ContB, x*50, y*50);
          if (Design==2)image(ContBW, x*50, y*50);
          Bas=true;
        }
        if (A!=0 && A!=10 && A!=20 && A!=30 && A!=40 && A!=50 && A!=60 && A!=70 && A!=80 && A!=90 && Collision [A-1] !=2) {
          if (Design==1)image(ContG, x*50, y*50);
          if (Design==2)image(ContGW, x*50, y*50);
          Gauche=true;
        }
        if (A!=9 &&A!=19 && A!=29 && A!=39 && A!=49 && A!=59 && A!=69 && A!=79 && A!=89 && A!=99 && Collision [A+1] !=2) {
          if (Design==1)image(ContD, x*50, y*50);
          if (Design==2)image(ContDW, x*50, y*50);
          Droite=true;
        }
        //Coins/angles lave
        //Eté
        if (Haut==true && Droite==true && Design==1) image(ContHD, x*50, y*50);
        if (Haut==true && Gauche==true && Design==1) image(ContHG, x*50, y*50);
        if (Bas==true && Droite==true && Design==1) image(ContBD, x*50, y*50);
        if (Bas==true && Gauche==true && Design==1) image(ContBG, x*50, y*50);

        if (Haut==true && Droite==true && Design==2) image(ContHDW, x*50, y*50);
        if (Haut==true && Gauche==true && Design==2) image(ContHGW, x*50, y*50);
        if (Bas==true && Droite==true && Design==2) image(ContBDW, x*50, y*50);
        if (Bas==true && Gauche==true && Design==2) image(ContBGW, x*50, y*50);

        //Remise a 0 de la détection des tiles autours du blocs de lave
        Bas= false;
        Haut= false;
        Droite= false;
        Gauche= false;
      }

      if (Collision [A] ==3) {
        //Lave
        if (Design==1)image(Lave, x*50, y*50);
        if (Design==2)image(LaveW, x*50, y*50);
        //rebors lave
        if (A>10 && Collision [A-10] !=3) {
          if (Design==1)image(ContH, x*50, y*50);
          if (Design==2)image(ContHW, x*50, y*50);
          Haut=true;
        }
        if (A<90 && Collision [A+10] !=3) {
          if (Design==1)image(ContB, x*50, y*50);
          if (Design==2)image(ContBW, x*50, y*50);
          Bas=true;
        }
        if (A!=0 && A!=10 && A!=20 && A!=30 && A!=40 && A!=50 && A!=60 && A!=70 && A!=80 && A!=90 && Collision [A-1] !=3) {
          if (Design==1)image(ContG, x*50, y*50);
          if (Design==2)image(ContGW, x*50, y*50);
          Gauche=true;
        }
        if (A!=9 &&A!=19 && A!=29 && A!=39 && A!=49 && A!=59 && A!=69 && A!=79 && A!=89 && A!=99 && Collision [A+1] !=3) {
          if (Design==1)image(ContD, x*50, y*50);
          if (Design==2)image(ContDW, x*50, y*50);
          Droite=true;
        }

        //Coins/angles lave
        if (Haut==true && Droite==true && Design==1) image(ContHD, x*50, y*50);
        if (Haut==true && Gauche==true && Design==1) image(ContHG, x*50, y*50);
        if (Bas==true && Droite==true && Design==1) image(ContBD, x*50, y*50);
        if (Bas==true && Gauche==true && Design==1) image(ContBG, x*50, y*50);

        if (Haut==true && Droite==true && Design==2) image(ContHDW, x*50, y*50);
        if (Haut==true && Gauche==true && Design==2) image(ContHGW, x*50, y*50);
        if (Bas==true && Droite==true && Design==2) image(ContBDW, x*50, y*50);
        if (Bas==true && Gauche==true && Design==2) image(ContBGW, x*50, y*50);

        //Remise a 0 de la détection des tiles autours du blocs de lave
        Bas= false;
        Haut= false;
        Droite= false;
        Gauche= false;
      }//Couleur Lave

      //Foret/arbre en bas pour recouvrir les tank
      if (Collision [A] ==4 && Design==1) image(arbre, x*50, y*50);
      if (Collision [A] ==4 && Design==2) image(arbreW, x*50, y*50);
      //Couleur Foret
    }
  }

  //Affichage dégats lave
  if (DegatsLaveTank==true) {
    fill(255, 0, 0, 100);
    rect(0, 0, 500, 500);
  }

  //Selection entourage tank
  if (Player==1) image(STank1, xbase, ybase);
  if (Player==2) image(STank2, xbase2, ybase2);

  //Affichage Tank
  if (Collision[xbase/50+ybase/50*10]==4 && Design==2) {
  } else {
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
  }

  if (Collision[xbase2/50+ybase2/50*10]==4 && Design==2) {
  } else {
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
  MusicBackground(); // On charge la musique du jeu

  if (IsMulti == true) {
    // Si nous sommes en multijoueur et que je suis serveur, on envoie nos informations au client connecté et on recolte les siennes
    if (AmIServer == true) {
      //[Joueur : {id, Vie, PosX, PosY, Feu, DistFeu, Direction}, Info : {Map, Tour, State, Winner, Coeurs, Saison}]
      //Joueur 1
      myServer.write(str(vietank1)+"/");    //Vie       (int) (0 < vie < 11)
      myServer.write(str(xbase)+"/");       //PosX      (int) ()
      myServer.write(str(ybase)+"/");       //PosY      (int) ()
      myServer.write(str(IsFire1)+"/");     //Feu       (int) (0 ou 1)
      myServer.write(str(DistFeu1)+"/");    //DistFeu   (int) (0 < dist < )
      myServer.write(str(Direction)+"/");   //Direction (int) (1 / 2 / 3 / 4)
      //Joueur 2
      Client thisClient = myServer.available();
      if (thisClient != null) {
        dataIn = thisClient.readString();
        CdataList = split(dataIn, '/');
      }

      vietank2   = int(CdataList[0]);
      xbase2     = int(CdataList[1]);
      ybase2     = int(CdataList[2]);
      IsFire2    = int(CdataList[3]);
      DistFeu2   = int(CdataList[4]);
      Direction2 = int(CdataList[5]);
      //Serveur
      //myServer.write(str(Collision)+"/"); //Map       (int[]) A INTEGRER
      myServer.write(str(0)+"/");
      myServer.write(str(Player)+"/");      //Tour      (int) (0 < tour)
      myServer.write(str(0)+"/");           //State     (str) (?)
      myServer.write(str(Winner)+"/");      //Winner    (int) (1 ou 2)
      myServer.write(str(Design));          //Saison    (int) (1 ou 2 / été ou hiver)
      delay(10);
    }
    // Si nous sommes en multijoueur et que je suis client, on reçoit les informations envoyées par le serveur et on envoie les notres
    if (AmIClient == true && myClient.available() > 0) {
      dataIn = myClient.readString();
      SdataList = split(dataIn, '/');

      //Joueur 1
      vietank1  = int(SdataList[0]);
      xbase     = int(SdataList[1]);
      ybase     = int(SdataList[2]);
      IsFire1   = int(SdataList[3]);
      DistFeu1  = int(SdataList[4]);
      Direction = int(SdataList[5]);
      //Joueur 2
      myClient.write(str(vietank2)+"/");    //Vie       (int) (0 < vie < 11)
      myClient.write(str(xbase2)+"/");      //PosX      (int) ()
      myClient.write(str(ybase2)+"/");      //PosY      (int) ()
      myClient.write(str(IsFire2)+"/");     //Feu       (int) (0 ou 1)
      myClient.write(str(DistFeu2)+"/");    //DistFeu   (int) (0 < dist < )
      myClient.write(str(Direction2)+"/");  //Direction (int) (1 / 2 / 3 / 4)
      //Serveur
      //Collision = int[](dataList[6]); A INTEGRER
      Player = int(SdataList[7]);

      Winner = int(SdataList[9]);
      Design = int(SdataList[10]);
      delay(10);
    }
  }
  // Ici, on appelle le void qu'il faut en fonction de ce qu'on veut afficher
  if (toshow == "Menu") Menu();
  if (toshow == "MenuPlay") MenuPlay();
  if (toshow == "MenuEditor") MenuEditor();
  if (toshow == "Game") Game();
  if (toshow == "ServerJoin") ServerJoin();
  if (toshow == "ServerCreate") ServerCreate();
  if (toshow == "MenuMaps") MenuMaps();
  if (toshow == "Options") Options();
  if (toshow == "Credits") Credits();
}

void Compteur() {
  if (ComptTimer >= frameRate/20) { //S'il s'est écoulé une minute
    ComptTimer = 0;
    TimerSec --; //Réduire le timer d'une seconde
    if (TimerSec == -1) { //Si une minute s'est écoulée
      TimerSec = 59; //Remettre les secondes par défaut
      TimerMin --; //Réduire les minutes
    }
  }
}

void MusicBackground() {

  //Volume du son
  MusicBackground.amp((float)MusicVOL/1000);
  //Boucle musique de fond
  DecompteMusique--;
  if (DecompteMusique<0 || DecompteMusique==(19*FrameRate)) {
    MusicBackground.play();
    DecompteMusique=(19*FrameRate);
  }
}

void Reset() {
  vietank1 = DefaultVie;
  vietank2 = DefaultVie;
  xbase = 0;
  ybase = 0;
  xbase2 = 450;
  ybase2 = 450;
  Menu = 1;
  Player = 0;
  TimerSec = DefaultSec;
  TimerMin = DefaultMin;
  Winner = 0;
  toshow = "Menu";
}

void Game() {
  ComptTimer ++;
  Compteur(); //Ajouter du temps au compteur dès que nous somme en jeu
  Move.amp((float)SoundVOL/1000);
  Fire.amp((float)SoundVOL/1000);
  textAlign(LEFT);
  if (IsMulti == false || IsMulti == true && AmIServer == true) {
    if (Player==0 && Act==0 && vietank1>0 && vietank2>0 || Player==2 && Act==0 && vietank1>0 && vietank2>0) {
      background(0);
      stroke(0);
      fill(0, 0, 255);
      textSize(40);
      text("Player 1", 160, 220);
      text("Press Down", 130, 270);
      if (keyPressed==true && keyCode==DOWN) {
        Player=1;
        Act=3;
        MaxDepl = 0;
        needed = 1;
      }
    }
  }

  if (IsMulti == false || IsMulti == true && AmIClient == true) {
    if (Player==1 && Act==0 && vietank1>0 && vietank2>0) {
      background(0);  
      fill(255, 0, 0);
      textSize(40);
      text("Player 2", 160, 220);
      text("Press Down", 130, 270);
      if (IA == false && keyPressed==true && keyCode==DOWN || IA == true) {
        Player=2; 
        Act=3;
      }
    }
  }

  //--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  if (Winner == 0 && (IsMulti == false || IsMulti == true && (AmIServer == true && Player == 1 || AmIClient == true && Player == 2))) {
    if (Act>0) {

      AffTank();

      if (choix==0) {//Choix des actions (Left=Shoot/Right=Move)
        if (IA == false || IA == true && Player == 1) { //Si nous sommes en 1v1 contre l'IA et que c'est à nous de jouer

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
          if (Player==1) fill(0, 0, 255);
          if (Player==2) fill(255, 0, 0);
          ellipse(480, 190, 10, 10);

          textSize(23);
          fill(250, 250, 250, 255);
          text("Left(for Attack)     Right(for move)", 250, 250);
          fill(255);
          textSize(20);
          text("Press arrow", 250, 200);
          text("And then press Enter", 250, 300);
          textAlign(LEFT);
        } else if (IA == true && Player == 2) choix = IA("choix"); //Si nous jouons contre l'IA et que c'est à elle de jouer, nous lui demandons son choix
      }


      if (choix == 1) {//Shoot

        if (CB<1 || lock == 0) {
          CB = (int)random(0, 10);
          // println(CB);
          if (Player == 1) DistFeu1 = CB;
          if (Player == 2) DistFeu2 = CB;

          if (Player == 1) {
            xbasem = xbase;
            ybasem = ybase;
          }
          if (Player == 2) {
            xbasem = xbase2;
            ybasem = ybase2;
          }

          AffTank();

          if (IsMulti == false || IsMulti == true && (AmIServer == true && Player == 1 || AmIClient == true && Player == 2) || IA == true && Player == 1) {
            fill(200);
            textSize(20);
            text("Press arrows to shoot your bullet in a direction", 30, 430);
            text("Then press Enter", 180, 480);
          }

          if (IA == true && Player == 2) Direction2 = IA("shoot"); //Si nous jouons contre l'IA, elle décide dans quelle direction elle veut tirer

          if (IA == false && keyCode == UP || IA == true && (Player == 1 && keyCode ==  UP || Player == 2 && Direction2 == 1)) {
            lock2 = 1;
            lock3 = 1;
            if (Player == 1) triangle(xbase+10, ybase-10, xbase+40, ybase-10, xbase+25, ybase-30);
            if (Player == 1) Direction=1;
            if (Player == 2) triangle(xbase2+10, ybase2-10, xbase2+40, ybase2-10, xbase2+25, ybase2-30);
            if (Player == 2) Direction2=1;
          }
          if (IA == false && keyCode == DOWN || IA == true && (Player == 1 && keyCode == DOWN || Player == 2 && Direction2 == 2)) {
            lock2 = 2;
            lock3 = 1;
            if (Player == 1) triangle(xbase+10, ybase+60, xbase+40, ybase+60, xbase+25, ybase+80);
            if (Player == 1) Direction=2;
            if (Player == 2) triangle(xbase2+10, ybase2+60, xbase2+40, ybase2+60, xbase2+25, ybase2+80);
            if (Player == 2) Direction2=2;
          }
          if (IA == false && keyCode == LEFT || IA == true && (Player == 1 && keyCode == LEFT || Player == 2 && Direction2 == 3)) {
            lock2 = 3;
            lock3 = 1;
            if (Player == 1) triangle(xbase-10, ybase+10, xbase-10, ybase+40, xbase-30, ybase+25);
            if (Player == 1) Direction=3;
            if (Player == 2) triangle(xbase2-10, ybase2+10, xbase2-10, ybase2+40, xbase2-30, ybase2+25);
            if (Player == 2) Direction2=3;
          }
          if (IA == false && keyCode == RIGHT || IA == true && (Player == 1 && keyCode == RIGHT|| Player == 2 && Direction2 == 4)) {
            lock2 = 4;
            lock3 = 1;
            if (Player == 1) triangle(xbase+60, ybase+10, xbase+60, ybase+40, xbase+80, ybase+25);
            if (Player == 1) Direction=4;
            if (Player == 2) triangle(xbase2+60, ybase2+10, xbase2+60, ybase2+40, xbase2+80, ybase2+25);
            if (Player == 2) Direction2=4;
          }
          if (lock3 == 1 && (IA == false && keyCode == ENTER || IA == true && (Player == 1 && keyCode == ENTER || Player == 2 && IsFire2 == 1))) {
            Fire.play(3);
            lock = lock2;
            lock3 = 0;
            if (Player == 1) IsFire1 = 1;
            if (Player == 2) IsFire2 = 1;
            IsFire1 = 0;
            IsFire2 = 0;
          }
        }

        if (CB > 0 && lock != 0) {

          CB = CB - 1;
          AffTank();
          if (lock == 1) {
            ybasem = ybasem-50;
            CDA();
            Balle = BalleU;
            image(Balle, xbasem, ybasem);
          }
          if (lock == 2) {
            ybasem = ybasem+50;
            CDA();
            Balle = BalleD;
            image(Balle, xbasem, ybasem);
          }
          if (lock == 3) {
            xbasem = xbasem-50;
            CDA();
            Balle = BalleL;
            image(Balle, xbasem, ybasem);
          }
          if (lock == 4) {
            xbasem = xbasem+50;
            CDA();
            Balle = BalleR;
            image(Balle, xbasem, ybasem);
          }
          if (Player == 1 && xbasem == xbase2 && ybasem == ybase2) {
            CB = 0;
            vietank2 = vietank2-1;
          }
          if (Player == 2 && xbasem == xbase && ybasem == ybase) {
            CB = 0;
            vietank1 = vietank1-1;
          }



          fill(200);
          textSize(50);
          text(CB, 450, 490, 500);
        }

        if (CB<1 && lock!=0) {
          choix = 0;
          lock = 0;
          AffTank();
          Balle = BalleExplosion;
          image(Balle, xbasem, ybasem);
          Act = Act-1;
          ChangementSaison++;
        }
      }


      if (choix==2) {//Move
        //Initialisation du dès de déplacements
        if (CP<1) {
          CP = (int)random(0, 10);
          CP = 20;
        }

        //Déplacements lorsque CP est différent de 0 (Joueur a encore des déplacements)
        if (CP>0) {
          if (IA == true && Player == 2) Direction2 = IA("move"); //Si nous jouons contre l'IA, elle décide dans quelle direction elle veut se déplacer

          if (IA == false && keyPressed == true && keyCode == UP || IA == true && (Player == 1 && keyPressed == true && keyCode == UP || Player == 2 && Direction2 == 1)) {
            if (Player == 1) ybase = ybase-50;
            if (Player == 2) ybase2 = ybase2-50;
            CP = CP-1;
            if (Player == 1) CDD();
            if (Player == 2) CDD2();
            if (Player == 1) Direction = 1;
            if (Player == 2) Direction2 = 1;
            Move.play();
          }
          if (IA == false && keyPressed == true && keyCode == DOWN || IA == true && (Player == 1 && keyPressed == true && keyCode == DOWN || Player == 2 && Direction2 == 2)) {
            if (Player == 1) ybase = ybase+50;
            if (Player == 2) ybase2 = ybase2+50;
            CP = CP-1;
            if (Player == 1) CDD();
            if (Player == 2) CDD2();
            if (Player == 1) Direction = 2;
            if (Player == 2) Direction2 = 2;
            Move.play();
          }
          if (IA == false && keyPressed == true && keyCode == LEFT || IA == true && (Player == 1 && keyPressed == true && keyCode == LEFT || Player == 2 && Direction2 == 3)) {
            if (Player == 1) xbase = xbase-50;
            if (Player == 2) xbase2 = xbase2-50;
            CP = CP-1;
            if (Player == 1) CDD();
            if (Player == 2) CDD2();
            if (Player == 1) Direction = 3;
            if (Player == 2) Direction2 = 3;
            Move.play();
          }
          if (IA == false && keyPressed == true && keyCode == RIGHT || IA == true && (Player == 1 && keyPressed == true && keyCode == RIGHT || Player == 2 && Direction2 == 4)) {
            if (Player == 1) xbase = xbase+50;
            if (Player == 2) xbase2 = xbase2+50;
            CP = CP-1;
            if (Player == 1) CDD();
            if (Player == 2) CDD2();
            if (Player == 1) Direction = 4;
            if (Player == 2) Direction2 = 4;
            Move.play();
          }

          if (TestCadriD == 0 && (IA == false && keyCode == UP || IA == true && (Player == 1 && keyCode == UP || Player == 2 && Direction2 == 1))) {
            if (Player == 1) ybase = ybase+50;
            if (Player == 2) ybase2 = ybase2+50;
            CP = CP+1;
            TestCadriD = 1;
          }
          if (TestCadriD == 0 && (IA == false && keyCode == DOWN || IA == true && (Player == 1 && keyCode == DOWN || Player == 2 && Direction2 == 2))) {
            if (Player == 1) ybase = ybase-50;
            if (Player == 2) ybase2 = ybase2-50;
            CP = CP+1;
            TestCadriD = 1;
          }
          if (TestCadriD == 0 && (IA == false && keyCode == LEFT || IA == true && (Player == 1 && keyCode == LEFT || Player == 2 && Direction2 == 3))) {
            if (Player == 1) xbase = xbase+50;
            if (Player == 2) xbase2 = xbase2+50;
            CP = CP+1;
            TestCadriD = 1;
          }
          if (TestCadriD == 0 && (IA == false && keyCode == RIGHT || IA == true && (Player == 1 && keyCode == RIGHT || Player == 2 && Direction2 == 4))) {
            if (Player == 1) xbase = xbase-50;
            if (Player == 2) xbase2 = xbase2-50;
            CP = CP+1;
            TestCadriD = 1;
          }

          AffTank();
          fill(200);

          textSize(50);
          text(CP, 450, 490, 500);
        }

        //Déplacements lorsque CP est inférieur à 1 (Joueur n'a plus de déplacements)
        if (CP<1) {
          choix = 0;
          Act = Act-1;
          ChangementSaison++;
        }
      }
    }
  } else AffTank();

  if (TimerMin <= -1 && vietank1 < vietank2 || vietank1<1) { //Détéction de victoire (fin de timer / plus de vie)
    background(0);
    fill(255, 0, 0);
    textSize(40);
    textAlign(CENTER);
    text("Player 2 WIN", 250, 220);
    textSize(20);
    text("Click SPACE to return to menu", 250, 300);
    Winner = 2;
  }
  if (TimerMin <= -1 && vietank2 < vietank1 || vietank2<1) {
    background(0);
    fill(0, 0, 255);
    textSize(40);
    textAlign(CENTER);
    text("Player 1 WIN", 250, 220);
    textSize(20);
    text("Click SPACE to return to menu", 250, 300);
    Winner = 1;
  }
  if (TimerMin <= -1 && vietank1 == vietank2) { //Egalité
    background(0);
    fill(255, 0, 255);
    textSize(40);
    textAlign(CENTER);
    text("EQUALITY", 250, 220);
    textSize(20);
    text("Click SPACE to return to menu", 250, 300);
    Winner = -1;
  }

  if (Design==1 && Changementok == true && ChangementSaison==SummerDay) {
    Design=2;
    ChangementSaison=0;
  }
  if (Design==2 && Changementok == true && ChangementSaison==WinterDay) {
    Design=1;
    ChangementSaison=0;
  }
  if (Design>2)Design=1;
  if (Winner == 0) {
    textAlign(RIGHT);
    textSize(15);
    fill(255);
    text(TimerMin+":"+TimerSec, width-10, 20);
  }
}
