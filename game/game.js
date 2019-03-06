var socket = io();
socket.on('message', function(data) {
  console.log(data);
});


var Player = 0; //Joueur 1 et 2 changement
var Act = 0;
var xbase = 0; // Emplacement tank 1 (0, 0)
var ybase = 0;
var xbase2 = 450; // Emplacement tank 2 (450, 450)
var ybase2 = 450;
var DefaultVie = 5; //Vie des tanks par défaut
var vietank1 = DefaultVie; //Vie des tanks
var vietank2 = DefaultVie;
var Direction = 2; //Direction des sprites des tanks
var Direction2 = 2;
var CP = 0; //Compteur Placement
var turn=0; //Un décompte de random éffectué
var arrows=0; //Empèche le joueur de maintenir les flèches pour se déplacer ( un appui = un déplacement )
var choix=0; //Validation Choix
var choix2=0;//Choix entre Attaque ou Déplacement
var choix3=0;//Anti Enter*2 ( effet d'un key pressed pour enter car non ascii)
var xbasem = 0; // Emplacement balle
var ybasem = 0;
var CB = 0; //Compteur Balle
var MLock = 0;
var lock=0; //touche de tire vérouillée
var lock2=0; //direction du tir
var lock3=0;//Anti Enter*2 ( effet d'un key pressed pour enter car non ascii)
var TestCadriD=0;//Test cadrillage renvoie 0 ou 1 => Si on peux passer ou pas
var TD2 = 0 ;
var Bas= false; //Variable détectant si plusieurs bord existes pour un angle (texture)
var Haut= false;
var Droite= false;
var Gauche= false;
var end = false;
var toshow = "Menu";
var Menu=1;
var bord = false;
var DegatsLaveTank=false;
var ChangementSaison = 0;
var Changementok = false ;

// Parties valeurs MenuEditeur
var Selectile=0;
var Selectedtile=0;
var LockTile=0;
var XCursorEdit=0;
var YCursorEdit=0;

//MenuMaps
/*JSONObject Map1;
JSONObject Map2;
JSONObject Map3;*/

//Interac(tion)Map permet de définir s'il s'agit d'une lecture (0) ou d'une écriture de map
var InteracMap = 0; 
//Annonce quelle map est sélectione
var SelectMap = 1;

//Menu option
var MenuOpt = 0;
var SMenuOpt = 1;
var MusicVOL = 1; //  <---------------------------------------------------------------------
var SoundVOL = 50;
var TSel = 1;
var TypeDeSon = 1;
var Design = 1;
var SummerDay = 1 ;
var WinterDay = 1 ;
var DefaultMin = 5, DefaultSec = 0;
//Permet d'accéder au parametres de son en jeu
var Link = 0;

var TimerSec = DefaultSec, TimerMin = DefaultMin;
var ComptTimer;

//MusicBackground
var FrameRate = 60;
var DecompteMusique = 19 * FrameRate + 1;

/*var [] Collision = {
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
};*/

//function setup(){

var CanvasGame = document.getElementById('canvas');
canvas.width = 500;
canvas.height = 600;
var ctx = CanvasGame.getContext("2d");
/*
# -----  FONCTION ctx.fillRect()  ----- #
ctx.fillStyle = "rgb(r, g, b)";
ctx.fillRect(x, y, width, height);

# -----  FONCTION ctx.fillText()  ----- #
ctx.font = "30px Comic Sans MS"; //"TAILLEpx NOM DE LA POLICE"
ctx.fillStyle = "rgb(r, g, b)";
ctx.textAlign = "center"; //center / left / right / up / down
ctx.fillText("text", x, y); 
*/

//}

function CDD(){
	//Cadrillage Des Déplacements (Tanks)
  var CDDx = xbase/50;
  var CDDy = ybase/50*10;
  var CDD = CDDx + CDDy;
  //Permet de fixer des limites pour la glisse sur la glace
  bord = false;

  //Colisions cotés de terrain (Déplacements)        si le tank rencontre la limite et qu'il se trouve sur de l'eau CP a besoin de +2 pour revenir a son etat initial
  if (CDDx<0) {
    CDD=CDD+1;
    xbase=xbase+50;
    CP=CP+1;
    if (Collision [CDD] == 2) CP=CP+1;
  }
  if (CDDy<0) {
    CDD=CDD+10;
    ybase=ybase+50;
    CP=CP+1;
    if (Collision [CDD] == 2) CP=CP+1;
  }
  if (CDDx>9) {
    CDD=CDD-1;
    xbase=xbase-50;
    CP=CP+1;
    if (Collision [CDD] == 2) CP=CP+1;
  }
  if (CDDy>90) {
    CDD=CDD-10;
    ybase=ybase-50;
    CP=CP+1;
    if (Collision [CDD] == 2) CP=CP+1;
  }


  //Si le tank veux aller dans un endroit qu'il ne peux traverser (Montagne)
  if (Collision [CDD] == 1) {
    TestCadriD = 0;
    TD2 = 1;
  }
  //Si le tank veux aller dans un endroit qu'il ne peux traverser (Lave)
  if (Collision [CDD] == 3 && Design == 1) {
    TestCadriD = 0;
    TD2 = 1;
  }
  if (Collision [CDD] == 3 && Design == 2) {
    TestCadriD = 1;
    TD2 = 1;
    vietank1--;
    DegatsLaveTank = true;
  } else DegatsLaveTank = false;
  //Si le tank va dans l'eau (Il est alors ralenti)
  if (Collision [CDD] == 2 && Design ==1) CP=CP-1;
  //Si le Tank va sur la glace (Il glisse jusqu'à un rebord ou un terrain différent de la glace)
  if (Collision [CDD] == 2 && Design ==2) {

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


function CDD2() {
  //Cadrillage Des Déplacements (Tanks)
  var CDDx = xbase2/50;
  var CDDy = ybase2/50*10;
  var CDD = CDDx + CDDy;
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
  var CDAx = xbasem/50;
  var CDAy = ybasem/50*10;
  var CDA = CDAx + CDAy;

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
  setTimeout(function() {}, 50);

  if (Design==1) ctx.fillStyle = "blue"; "rgb(45,139,97)";
  if (Design==2) ctx.fillStyle = "blue"; "rgb(196, 247, 255)";
  ctx.fillctx.fillRect(0, 0, canvas.width, canvas.height);
  //Affichage barre d'info
  ctx.fillStyle = "rgb(0, 0, 0)";
  ctx.fillctx.fillRect(0, 500, 500, 50);

  ctx.fillStyle = "rgb(200, 200, 200)";
  ctx.fillctx.fillRect(0, 500, 500, 3);

  for (var x=0; x<10; x++) {
    for (var y=0; y<10; y++) {
      var Ax = x;
      var Ay = y*10;
      var A = Ax + Ay;
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
    ctx.fillStyle = "rgb(255, 0, 0, 100);";
    ctx.fillctx.fillRect(0, 0, 500, 500);
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
  ctx.font = "14px Sans Serif";
  ctx.fillStyle = "rgb(255, 255, 255)";
  ctx.textAlign = "left";
  ctx.fillctx.fillText("V1", 20, 530); 
  ctx.fillctx.fillText(":V2", 460, 530)

  for (var viebarre1 = vietank1; viebarre1>0; viebarre1--) {
    ctx.fillStyle = "rgb(150, 32, 32)";
    image(Vies, 12*viebarre1+40, 523, 8, 8);
  }
  for (var viebarre2 = vietank2; viebarre2>0; viebarre2--) {
    ctx.fillStyle = "rgb(150, 32, 32)";
    image(Vies, -12*viebarre2+460, 523, 8, 8);
  }

  //Affichage de la Commande pour accéder aux options en jeu
  ctx.font = "14px Sans Serif";
  ctx.fillStyle = "rgb(255, 255, 255)";
  ctx.textAlign = "center";
  ctx.fillctx.fillText("Press Shift", 250, 520); 
  ctx.fillctx.fillText("For Options", 250, 540);
}

// function draw() {

MusicBackground();
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

// }

function Compteur() {
  if (ComptTimer >= frameRate/20) { //S'il s'est écoulé une minute
    ComptTimer = 0;
    TimerSec --; //Réduire le timer d'une seconde
    if (TimerSec == -1) { //Si une minute s'est écoulée
      TimerSec = 59; //Remettre les secondes par défaut
      TimerMin --; //Réduire les minutes
    }
  }
}

/*function MusicBackground() {

  //Volume du son
  MusicBackground.amp((float)MusicVOL/1000);
  //Boucle musique de fond
  DecompteMusique--;
  if (DecompteMusique<0 || DecompteMusique==(19*FrameRate)) {
    MusicBackground.play();
    DecompteMusique=(19*FrameRate);
  }
}*/


function Reset() {
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

function Game() {
  ComptTimer ++;
  Compteur(); //Ajouter du temps au compteur dès que nous somme en jeu
  //Move.amp((float)SoundVOL/1000);
  //Fire.amp((float)SoundVOL/1000);
  ctx.textAlign = "left";
  if (IsMulti == false || IsMulti == true && AmIServer == true) {
    if (Player==0 && Act==0 && vietank1>0 && vietank2>0 || Player==2 && Act==0 && vietank1>0 && vietank2>0) {
      ctx.fillStyle = "rgb(0, 0, 0)";
      ctx.fillRect(0, 0, canvas.width, canvas.height);
      ctx.fillStyle = "rgb(0, 0, 255)";
      ctx.font = "40px Sans Serif"
      ctx.fillText("Player 1", 160, 220);
      ctx.fillText("Press Down", 130, 270);
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
      ctx.fillStyle = "rgb(0, 0, 0)";
      ctx.fillRect(0, 0, canvas.width, canvas.height);
      ctx.fillStyle = "rgb(255, 0, 0)";
      ctx.font = "40px Sans Serif"
      ctx.fillText("Player 2", 160, 220);
      ctx.fillText("Press Down", 130, 270);
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
            ctx.fillStyle = "rgb(255, 255, 255, 100)";//Souligne en rouge le choix Left
            ctx.fillRect(55, 227, 180, 30);
          }

          if (keyCode==RIGHT) {//Lorsque le curseur est sur Move
            choix2=2;
            choix3=1;
            ctx.fillStyle = "rgb(255, 255, 255, 100)";//Souligne en rouge le choix Right
            ctx.fillRect(263, 227, 180, 30);
          }

          if (choix3==1 && keyCode==ENTER) {
            choix=choix2;
            choix3=0;
          }//Lorsque l'action est choisie par Enter


          //Affichage du choix des Actions (shoot ou move)
          ctx.fillStyle = "rgb(0, 0, 0, 125)";
          ctx.fillRect(0, 175, 500, 140);

          ctx.fillStyle = "rgb(0, 0, 0, 65)";
          ctx.fillRect(0, 175+140, 500, 500-(175+140));
          ctx.fillRect(0, 0, 500, 175);

          ctx.fillStyle = "rgb(255, 255, 255, 30)";
          ctx.fillRect(0, 175+140, 500, 3);
          ctx.fillRect(0, 172, 500, 3);

          ctx.font = "45px Sans Serif";
          ctx.fillStyle = "rgb(255, 255, 255, 200)";
          ctx.textAlign = "center";
          ctx.beginPath();
          ctx.arc(480, 190, 15, 0, 2 * Math.PI);
          if (Player==1) ctx.fillStyle = "rgb(0, 0, 255)";
          if (Player==2) ctx.fillStyle = "rgb(255, 0, 0)";
          ctx.beginPath();
          ctx.arc(480, 190, 10, 0, 2 * Math.PI);

          ctx.font = "23px Sans Serif";
          ctx.fillStyle = "rgb(250, 250, 250, 255)";
          ctx.fillText("Left(for Attack)     Right(for move)", 250, 250);
          ctx.fillStyle = "rgb(255, 255, 255)";
          ctx.font = "20px Sans Serif";
          ctx.fillText("Press arrow", 250, 200);
          ctx.fillText("And then press Enter", 250, 300);
          ctx.textAlign = "left";
        } else if (IA == true && Player == 2) choix = IA("choix"); //Si nous jouons contre l'IA et que c'est à elle de jouer, nous lui demandons son choix
      }


      if (choix == 1) {//Shoot

        if (CB<1 || lock == 0) {
          CB = random(0, 10);
          // console.log(CB);
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
            ctx.fillStyle = "rgb(200, 200, 200)";
            ctx.font = "20px Sans Serif";
            ctx.fillText("Press arrows to shoot your bullet in a direction", 30, 430);
            ctx.fillText("Then press Enter", 180, 480);
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
            //Fire.play(3);
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



          ctx.fillStyle = "rgb(200, 200, 200)";
          ctx.text = "50px Sans Serif";
          ctx.fillText(CB, 450, 490, 500);
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
          CP = random(0, 10);
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
            //Move.play();
          }
          if (IA == false && keyPressed == true && keyCode == DOWN || IA == true && (Player == 1 && keyPressed == true && keyCode == DOWN || Player == 2 && Direction2 == 2)) {
            if (Player == 1) ybase = ybase+50;
            if (Player == 2) ybase2 = ybase2+50;
            CP = CP-1;
            if (Player == 1) CDD();
            if (Player == 2) CDD2();
            if (Player == 1) Direction = 2;
            if (Player == 2) Direction2 = 2;
            //Move.play();
          }
          if (IA == false && keyPressed == true && keyCode == LEFT || IA == true && (Player == 1 && keyPressed == true && keyCode == LEFT || Player == 2 && Direction2 == 3)) {
            if (Player == 1) xbase = xbase-50;
            if (Player == 2) xbase2 = xbase2-50;
            CP = CP-1;
            if (Player == 1) CDD();
            if (Player == 2) CDD2();
            if (Player == 1) Direction = 3;
            if (Player == 2) Direction2 = 3;
            //Move.play();
          }
          if (IA == false && keyPressed == true && keyCode == RIGHT || IA == true && (Player == 1 && keyPressed == true && keyCode == RIGHT || Player == 2 && Direction2 == 4)) {
            if (Player == 1) xbase = xbase+50;
            if (Player == 2) xbase2 = xbase2+50;
            CP = CP-1;
            if (Player == 1) CDD();
            if (Player == 2) CDD2();
            if (Player == 1) Direction = 4;
            if (Player == 2) Direction2 = 4;
            //Move.play();
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
          ctx.fillStyle = "rgb(200, 200, 200)";

          ctx.text = "50px Sans Serif";
          ctx.fillText(CP, 450, 490, 500);
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
  	ctx.fillStyle = "rgb(0, 0, 0)";
  	ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = "rgb(255, 0, 0)";
    ctx.text = "40px Sans Serif";
    ctx.textAlign = "center";
    ctx.fillText("Player 2 WIN", 250, 220);
    ctx.text = "20px Sans Serif";
    ctx.fillText("Click SPACE to return to menu", 250, 300);
    Winner = 2;
  }
  if (TimerMin <= -1 && vietank2 < vietank1 || vietank2<1) {
    ctx.fillStyle = "rgb(0, 0, 0)";
  	ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = "rgb(0, 0, 255)";
    ctx.text = "40px Sans Serif";
    ctx.textAlign = "center";
    ctx.fillText("Player 1 WIN", 250, 220);
    ctx.text = "20px Sans Serif";
    ctx.fillText("Click SPACE to return to menu", 250, 300);
    Winner = 1;
  }
  if (TimerMin <= -1 && vietank1 == vietank2) { //Egalité
    ctx.fillStyle = "rgb(0, 0, 0)";
  	ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = "rgb(255, 0, 255)";
    ctx.text = "40px Sans Serif";
    ctx.textAlign = "center";
    ctx.fillText("EQUALITY", 250, 220);
    ctx.text = "20px Sans Serif";
    ctx.fillText("Click SPACE to return to menu", 250, 300);
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
    ctx.textAlign = "right";
    ctx.text = "15px Sans Serif";
    ctx.fillStyle = "rgb(255, 255, 255)";
    ctx.fillText(TimerMin+":"+TimerSec, width-10, 20);
  }

  ctx.closePath();
}


function random(min, max){
	return Math.floor(Math.random() * (Math.floor(max) - Math.floor(min)) + Math.floor(min));
}

function triangle(a, b, c, d, e, f){
ctx.beginPath();
ctx.moveTo(a, b);
ctx.lineTo(c, d);
ctx.lineTo(e, f);
ctx.fill();
}


/*socket.emit('new player');
setInterval(function() {
  socket.emit('movement', movement);
}, 1000 / 60);

socket.on('state', function(players) {
  context.clearRect(0, 0, 500, 500);
  context.fillStyle = 'green';
  for (var id in players) {
    var player = players[id];
    context.beginPath();
    context.arc(player.x, player.y, 10, 0, 2 * Math.PI);
    context.fill();
  }
});*/