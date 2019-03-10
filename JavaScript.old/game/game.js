function fill(r, g, b){
  ctx.fillStyle = "rgb("+r+", "+g+", "+b+")";
}
function filla(r, g, b, a){
    a = (100 * a / 255) / 100; //remaping value from [0, 255] to [0, 100] then [0.0, 1.0]
  ctx.fillStyle = "rgba("+r+", "+g+", "+b+", "+a+")";
}

function rect(x, y, w, h){
  ctx.beginPath();
  ctx.rect(x, y, w, h);
  ctx.fill();
  ctx.closePath();
}

function triangle(a, b, c, d, e, f){
  ctx.beginPath();
  ctx.moveTo(a, b);
  ctx.lineTo(c, d);
  ctx.lineTo(e, f);
  ctx.fill();
  ctx.closePath();
}

function image(i, x, y){
  ctx.drawImage(i, x, y);
}

function ellipse(x, y, w, h){
  ctx.beginPath();
  ctx.arc(x, y, w, 0, 2 * Math.PI);
  ctx.fill();
  ctx.closePath();
}

function text(t, x, y){
  ctx.fillText(t, x, y);
}

function textAlign(a){
  ctx.textAlign = ""+a.toLowerCase();
}

function textSize(s){
  ctx.font = s+"px Sans Serif";
}

function random(min, max){
  return Math.floor(Math.random() * (Math.floor(max) - Math.floor(min)) + Math.floor(min));
}

function delay(t) {
  setTimeout(function() {}, t);
}

function background(r, g ,b){
  ctx.fillStyle = "rgb("+r+", "+g+", "+b+")";
  ctx.fillRect(0, 0, canvas.width, canvas.height);
}

function print(t){
  console.log(t);
}

function println(t){
  print(t);
}

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
//JSONObject Map1;
//JSONObject Map2;
//JSONObject Map3;
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

//Maps de base lorsqu'on édite une map dans le menu editeur
//var [] Collision = {
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
var Collision = [
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
];
//Chargement des images du jeu
var BackgMenu = new Image("data/BackMenu.png");
var BackOpt = new Image("data/Options.png");
var Credits = new Image("data/Crédits.png");

var arbre = new Image("data/arbre.png");
var Montagne = new Image("data/Montagne.png");
var Eau = new Image("data/Eau.png");
var Lave = new Image("data/Lave.png");
var ContH = new Image("data/Lavehaut.png");
var ContB = new Image("data/Lavebas.png");
var ContG = new Image("data/Lavegauche.png");
var ContD = new Image("data/Lavedroite.png");
var ContHD = new Image("data/Lavehaut+droite.png");
var ContHG = new Image("data/Lavehaut+gauche.png");
var ContBD = new Image("data/Lavebas+droite.png");
var ContBG = new Image("data/Lavebas+gauche.png");

var arbreW = new Image("data/arbreW.png");
var MontagneW = new Image("data/MontagneW.png");
var EauW = new Image("data/EauW.png");
var LaveW = new Image("data/LaveW.png");
var ContHW = new Image("data/LavehautW.png");
var ContBW = new Image("data/LavebasW.png");
var ContGW = new Image("data/LavegaucheW.png");
var ContDW = new Image("data/LavedroiteW.png");
var ContHDW = new Image("data/Lavehaut+droiteW.png");
var ContHGW = new Image("data/Lavehaut+gaucheW.png");
var ContBDW = new Image("data/Lavebas+droiteW.png");
var ContBGW = new Image("data/Lavebas+gaucheW.png");

var STank1 = new Image("data/Selection Tank1.png");
var STank2 = new Image("data/Selection Tank2.png");
var Tank1u = new Image("data/Tank1u.png");
var Tank1d = new Image("data/Tank1d.png");
var Tank1l = new Image("data/Tank1l.png");
var Tank1r = new Image("data/Tank1r.png");
var Tank2u = new Image("data/Tank2u.png");
var Tank2d = new Image("data/Tank2d.png");
var Tank2l = new Image("data/Tank2l.png");
var Tank2r = new Image("data/Tank2r.png");
var Vies = new Image("data/Vies.png");
var BalleU = new Image("data/BalleU.png");
var BalleD = new Image("data/BalleD.png");
var BalleR = new Image("data/BalleR.png");
var BalleL = new Image("data/BalleL.png");
var BalleExplosion = new Image("data/Explosion.png");

var STile = new Image("data/Selection Tank2.png");

var Fire = new Audio("game/data/tankfire.wav"); 
var Move = new Audio("game/data/Move.wav"); 
var MusicBackground = new Audio("game/data/MusicBackground.wav"); 

var CanvasGame = document.getElementById('canvas');
canvas.width = 500;
canvas.height = 550;
var ctx = CanvasGame.getContext("2d");

/*window.onload = function(){
  background(0, 0, 0);
}*/

function CDD() {
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
    if (Collision[CDD] ==2) CP=CP+1;
  }
  if (CDDy<0) {
    CDD=CDD+10;
    ybase=ybase+50;
    CP=CP+1;
    if (Collision[CDD] ==2) CP=CP+1;
  }
  if (CDDx>9) {
    CDD=CDD-1;
    xbase=xbase-50;
    CP=CP+1;
    if (Collision[CDD] ==2) CP=CP+1;
  }
  if (CDDy>90) {
    CDD=CDD-10;
    ybase=ybase-50;
    CP=CP+1;
    if (Collision[CDD] ==2) CP=CP+1;
  }


  //Si le tank veux aller dans un endroit qu'il ne peux traverser (Montagne)
  if (Collision[CDD] ==1) {
    TestCadriD=0;
    TD2=1;
  }
  //Si le tank veux aller dans un endroit qu'il ne peux traverser (Lave)
  if (Collision[CDD] ==3 && Design == 1) {
    TestCadriD=0;
    TD2=1;
  }
  if (Collision[CDD] ==3 && Design == 2) {
    TestCadriD=1;
    TD2=1;
    vietank1--;
    DegatsLaveTank  =true;
  } else DegatsLaveTank=false;
  //Si le tank va dans l'eau (Il est alors ralenti)
  if (Collision[CDD] ==2 && Design ==1) CP=CP-1;
  //Si le Tank va sur la glace (Il glisse jusqu'à un rebord ou un terrain différent de la glace)
  if (Collision[CDD] ==2 && Design ==2) {

    while (Collision[CDD] ==2 && keyPressed == true && key==39 && bord ==false) {
      xbase=xbase+50; 
      if (xbase<=450)CDDx = xbase/50; 
      else { 
        bord = true ; 
        xbase=xbase-50;
      }
      CDD = CDDx + CDDy;
      if (Collision[CDD]==1) {
        bord = true ; 
        xbase=xbase-50;
      }
      AffTank();
    }

    while (Collision[CDD] ==2 && keyPressed == true && key==37 && bord ==false) {
      xbase=xbase-50; 
      if (xbase>=0)CDDx = xbase/50; 
      else { 
        bord = true ; 
        xbase=xbase+50;
      }
      CDD = CDDx + CDDy;
      if (Collision[CDD]==1) {
        bord = true ; 
        xbase=xbase+50;
      }
      AffTank();
    }

    while (Collision[CDD] ==2 && keyPressed == true && key==38 && bord ==false) {
      ybase=ybase-50; 
      if (ybase>=0)CDDy = ybase/50*10; 
      else { 
        bord = true ; 
        ybase=ybase+50;
      }
      CDD = CDDx + CDDy;
      if (Collision[CDD]==1) {
        bord = true ; 
        ybase=ybase+50;
      }
      AffTank();
    }

    while (Collision[CDD] ==2 && keyPressed == true && key==40 && bord ==false) {
      ybase=ybase+50; 
      if (ybase<=450)CDDy = ybase/50*10; 
      else { 
        bord = true ; 
        ybase=ybase-50;
      }
      CDD = CDDx + CDDy;
      if (Collision[CDD]==1) {
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
    if (Collision[CDD] ==2) CP=CP+1;
  }
  if (CDDy<0) {
    CDD=CDD+10;
    ybase2=ybase2+50;
    CP=CP+1;
    if (Collision[CDD] ==2) CP=CP+1;
  }
  if (CDDx>9) {
    CDD=CDD-1;
    xbase2=xbase2-50;
    CP=CP+1;
    if (Collision[CDD] ==2) CP=CP+1;
  }
  if (CDDy>90) {
    CDD=CDD-10;
    ybase2=ybase2-50;
    CP=CP+1;
    if (Collision[CDD] ==2) CP=CP+1;
  }

  //Si le tank veux aller dans un endroit qu'il ne peux traverser (Montagne)
  if (Collision[CDD] ==1) {
    TestCadriD=0;
    TD2=1;
  }
  //Si le tank veux aller dans un endroit qu'il ne peux traverser (Lave)
  if (Collision[CDD] ==3 && Design == 1) {
    TestCadriD=0;
    TD2=1;
  }
  if (Collision[CDD] ==3 && Design == 2) {
    TestCadriD=1;
    TD2=1;
    vietank2--;
    DegatsLaveTank  =true;
  } else DegatsLaveTank=false;
  //Si le tank va dans l'eau (Il est alors ralenti)
  if (Collision[CDD] ==2 && Design ==1) CP=CP-1;
  //Si le Tank va sur la glace (Il glisse jusqu'à un rebord ou un terrain différent de la glace)
  if (Collision[CDD] ==2 && Design ==2) {

    while (Collision[CDD] ==2 && keyPressed == true && key==39 && bord ==false) {
      xbase2=xbase2+50; 
      if (xbase2<=450)CDDx = xbase2/50; 
      else { 
        bord = true ; 
        xbase2=xbase2-50;
      }
      CDD = CDDx + CDDy;
      if (Collision[CDD]==1) {
        bord = true ; 
        xbase2=xbase2-50;
      }
      AffTank();
    }

    while (Collision[CDD] ==2 && keyPressed == true && key==37 && bord ==false) {
      xbase2=xbase2-50; 
      if (xbase2>=0)CDDx = xbase2/50; 
      else { 
        bord = true ; 
        xbase2=xbase2+50;
      }
      CDD = CDDx + CDDy;
      if (Collision[CDD]==1) {
        bord = true ; 
        xbase2=xbase2+50;
      }
      AffTank();
    }

    while (Collision[CDD] ==2 && keyPressed == true && key==38 && bord ==false) {
      ybase2=ybase2-50; 
      if (ybase2>=0)CDDy = ybase2/50*10; 
      else { 
        bord = true ; 
        ybase2=ybase2+50;
      }
      CDD = CDDx + CDDy;
      if (Collision[CDD]==1) {
        bord = true ; 
        ybase2=ybase2+50;
      }
      AffTank();
    }

    while (Collision[CDD] ==2 && keyPressed == true && key==40 && bord ==false) {
      ybase2=ybase2+50; 
      if (ybase2<=450)CDDy = ybase2/50*10; 
      else { 
        bord = true ; 
        ybase2=ybase2-50;
      }
      CDD = CDDx + CDDy;
      if (Collision[CDD]==1) {
        bord = true ; 
        ybase2=ybase2-50;
      }
      AffTank();
    }
  }
}
function CDA() {
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
  if (Collision[CDA] ==1) CB=0;
  if (Collision[CDA] ==1 && Design==2)Collision[CDA]=0;
  //Si le tank veux aller dans un endroit qu'il ne peux traverser (Foret)
  if (Collision[CDA] ==4) CB=0;
}


function AffTank () {//Affiche le tank

  delay(50);
  if (Design==1)background(45, 139, 97);
  if (Design==2)background(196, 247, 255);
  //Affichage barre d'info
  fill(0, 0, 0);
  rect(0, 500, 500, 50);
  fill(200, 200, 200);
  rect(0, 500, 500, 3);

  for (var x=0; x<10; x++) {
    for (var y=0; y<10; y++) {
      var Ax = x;
      var Ay = y*10;
      var A = Ax + Ay;
      if (Collision[A] == 1 && Design==1) image(Montagne, x*50, y*50);
      if (Collision[A] == 1 && Design==2) image(MontagneW, x*50, y*50);
      //Couleur Roche
      if (Collision[A] == 2) {
        //Eau
        if (Design==1)image(Eau, x*50, y*50);
        if (Design==2)image(EauW, x*50, y*50);
        //rebors eau
        if (A>10 && Collision[A-10] !=2) {
          if (Design==1)image(ContH, x*50, y*50);
          if (Design==2)image(ContHW, x*50, y*50);
          Haut=true;
        }
        if (A<90 && Collision[A+10] !=2) {
          if (Design==1)image(ContB, x*50, y*50);
          if (Design==2)image(ContBW, x*50, y*50);
          Bas=true;
        }
        if (A!=0 && A!=10 && A!=20 && A!=30 && A!=40 && A!=50 && A!=60 && A!=70 && A!=80 && A!=90 && Collision[A-1] !=2) {
          if (Design==1)image(ContG, x*50, y*50);
          if (Design==2)image(ContGW, x*50, y*50);
          Gauche=true;
        }
        if (A!=9 &&A!=19 && A!=29 && A!=39 && A!=49 && A!=59 && A!=69 && A!=79 && A!=89 && A!=99 && Collision[A+1] !=2) {
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

      if (Collision[A] ==3) {
        //Lave
        if (Design==1)image(Lave, x*50, y*50);
        if (Design==2)image(LaveW, x*50, y*50);
        //rebors lave
        if (A>10 && Collision[A-10] !=3) {
          if (Design==1)image(ContH, x*50, y*50);
          if (Design==2)image(ContHW, x*50, y*50);
          Haut=true;
        }
        if (A<90 && Collision[A+10] !=3) {
          if (Design==1)image(ContB, x*50, y*50);
          if (Design==2)image(ContBW, x*50, y*50);
          Bas=true;
        }
        if (A!=0 && A!=10 && A!=20 && A!=30 && A!=40 && A!=50 && A!=60 && A!=70 && A!=80 && A!=90 && Collision[A-1] !=3) {
          if (Design==1)image(ContG, x*50, y*50);
          if (Design==2)image(ContGW, x*50, y*50);
          Gauche=true;
        }
        if (A!=9 &&A!=19 && A!=29 && A!=39 && A!=49 && A!=59 && A!=69 && A!=79 && A!=89 && A!=99 && Collision[A+1] !=3) {
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
      if (Collision[A] ==4 && Design==1) image(arbre, x*50, y*50);
      if (Collision[A] ==4 && Design==2) image(arbreW, x*50, y*50);
      //Couleur Foret
    }
  }

  //Affichage dégats lave
  if (DegatsLaveTank==true) {
    filla(255, 0, 0, 100);
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
  fill(255, 255, 255);
  textSize(14);
  text("V1:", 20, 530);
  text(":V2", 460, 530);
  for (var viebarre1 = vietank1; viebarre1>0; viebarre1--) {
    fill(150, 32, 32);
    image(Vies, 12*viebarre1+40, 523, 8, 8);
  }
  for (var viebarre2 = vietank2; viebarre2>0; viebarre2--) {
    fill(150, 32, 32);
    image(Vies, -12*viebarre2+460, 523, 8, 8);
  }

  //Affichage de la Commande pour accéder aux options en jeu
  textAlign(CENTER);
  fill(255, 255, 255);
  text("Press Shift", 250, 520);
  text("For Options", 250, 540);
  textAlign(LEFT);
}

//MusicBackground(); // On charge la musique du jeu

  /*if (IsMulti == true) {
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
  }*/
  // Ici, on appelle le function qu'il faut en fonction de ce qu'on veut afficher
if (toshow == "Menu") MainMenu();
if (toshow == "MenuPlay") MenuPlay();
if (toshow == "MenuEditor") MenuEditor();
if (toshow == "Game") Game();
if (toshow == "MenuMaps") MenuMaps();
if (toshow == "Options") Options();
if (toshow == "Credits") Credits();

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

function MusicBackground() {

  //Volume du son
  MusicBackground.volume(MusicVOL/100);
  //Boucle musique de fond
  DecompteMusique--;
  if (DecompteMusique<0 || DecompteMusique==(19*60)) {
    MusicBackground.play();
    DecompteMusique=(19*60);
  }
}

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
  Move.volume(SoundVOL/100);
  Fire.volume(SoundVOL/100);
  textAlign(LEFT);
  if (IsMulti == false || IsMulti == true && AmIServer == true) {
    if (Player==0 && Act==0 && vietank1>0 && vietank2>0 || Player==2 && Act==0 && vietank1>0 && vietank2>0) {
      background(0, 0, 0);
      fill(0, 0, 255);
      textSize(40);
      text("Player 1", 160, 220);
      text("Press Down", 130, 270);
      if (keyPressed==true && key==40) {
        Player=1;
        Act=3;
        MaxDepl = 0;
        needed = 1;
      }
    }
  }

  if (IsMulti == false || IsMulti == true && AmIClient == true) {
    if (Player==1 && Act==0 && vietank1>0 && vietank2>0) {
      background(0, 0, 0);  
      fill(255, 0, 0);
      textSize(40);
      text("Player 2", 160, 220);
      text("Press Down", 130, 270);
      if (IA == false && keyPressed==true && key==40 || IA == true) {
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

          if (keyPressed == true && key == 37) {//Lorsque le curseur est sur Shoot
            choix2=1;
            choix3=1;
            filla(255, 255, 255, 100);//Souligne en rouge le choix Left
            rect(55, 227, 180, 30);
          }

          if (keyPressed == true && key == 39) {//Lorsque le curseur est sur Move
            choix2=2;
            choix3=1;
            filla(255, 255, 255, 100);//Souligne en rouge le choix Right
            rect(263, 227, 180, 30);
          }

          if (choix3==1 && keyPressed == true && key == 13) {
            choix=choix2;
            choix3=0;
          }//Lorsque l'action est choisie par Enter


          //Affichage du choix des Actions (shoot ou move)
          filla(0, 0, 0, 125);
          rect(0, 175, 500, 140);

          filla(0, 0, 0, 65);
          rect(0, 175+140, 500, 500-(175+140));
          rect(0, 0, 500, 175);

          filla(255, 255, 255, 30);
          rect(0, 175+140, 500, 3);
          rect(0, 172, 500, 3);

          textAlign("CENTER");
          textSize(45);
          filla(255, 255, 255, 200);
          ellipse(480, 190, 15, 15);
          if (Player==1) fill(0, 0, 255);
          if (Player==2) fill(255, 0, 0);
          ellipse(480, 190, 10, 10);

          textSize(23);
          filla(250, 250, 250, 255);
          text("Left(for Attack)     Right(for move)", 250, 250);
          fill(255, 255, 255);
          textSize(20);
          text("Press arrow", 250, 200);
          text("And then press Enter", 250, 300);
          textAlign(LEFT);
        } else if (IA == true && Player == 2) choix = IA("choix"); //Si nous jouons contre l'IA et que c'est à elle de jouer, nous lui demandons son choix
      }


      if (choix == 1) {//Shoot

        if (CB<1 || lock == 0) {
          CB = random(0, 10);
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
            fill(200, 200, 200);
            textSize(20);
            text("Press arrows to shoot your bullet in a direction", 30, 430);
            text("Then press Enter", 180, 480);
          }

          if (IA == true && Player == 2) Direction2 = IA("shoot"); //Si nous jouons contre l'IA, elle décide dans quelle direction elle veut tirer

          if (IA == false && keyPressed == true && key == 38 || IA == true && (Player == 1 && keyPressed == true && key ==  38 || Player == 2 && Direction2 == 1)) {
            lock2 = 1;
            lock3 = 1;
            if (Player == 1) triangle(xbase+10, ybase-10, xbase+40, ybase-10, xbase+25, ybase-30);
            if (Player == 1) Direction=1;
            if (Player == 2) triangle(xbase2+10, ybase2-10, xbase2+40, ybase2-10, xbase2+25, ybase2-30);
            if (Player == 2) Direction2=1;
          }
          if (IA == false && keyPressed == true && key == 40 || IA == true && (Player == 1 && keyPressed == true && key == 40 || Player == 2 && Direction2 == 2)) {
            lock2 = 2;
            lock3 = 1;
            if (Player == 1) triangle(xbase+10, ybase+60, xbase+40, ybase+60, xbase+25, ybase+80);
            if (Player == 1) Direction=2;
            if (Player == 2) triangle(xbase2+10, ybase2+60, xbase2+40, ybase2+60, xbase2+25, ybase2+80);
            if (Player == 2) Direction2=2;
          }
          if (IA == false && keyPressed == true && key == 37 || IA == true && (Player == 1 && keyPressed == true && key == 37 || Player == 2 && Direction2 == 3)) {
            lock2 = 3;
            lock3 = 1;
            if (Player == 1) triangle(xbase-10, ybase+10, xbase-10, ybase+40, xbase-30, ybase+25);
            if (Player == 1) Direction=3;
            if (Player == 2) triangle(xbase2-10, ybase2+10, xbase2-10, ybase2+40, xbase2-30, ybase2+25);
            if (Player == 2) Direction2=3;
          }
          if (IA == false && keyPressed == true && key == 39 || IA == true && (Player == 1 && keyPressed == true && key == 39 || Player == 2 && Direction2 == 4)) {
            lock2 = 4;
            lock3 = 1;
            if (Player == 1) triangle(xbase+60, ybase+10, xbase+60, ybase+40, xbase+80, ybase+25);
            if (Player == 1) Direction=4;
            if (Player == 2) triangle(xbase2+60, ybase2+10, xbase2+60, ybase2+40, xbase2+80, ybase2+25);
            if (Player == 2) Direction2=4;
          }
          if (lock3 == 1 && (IA == false && keyPressed == true && key == 13 || IA == true && (Player == 1 && keyPressed == true && key == 13 || Player == 2 && IsFire2 == 1))) {
            Fire.play();
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



          fill(200, 200, 200);
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
          CP = random(0, 10);
          CP = 20;
        }

        //Déplacements lorsque CP est différent de 0 (Joueur a encore des déplacements)
        if (CP>0) {
          if (IA == true && Player == 2) Direction2 = IA("move"); //Si nous jouons contre l'IA, elle décide dans quelle direction elle veut se déplacer

          if (IA == false && keyPressed == true && key == 38 || IA == true && (Player == 1 && keyPressed == true && key == 38 || Player == 2 && Direction2 == 1)) {
            if (Player == 1) ybase = ybase-50;
            if (Player == 2) ybase2 = ybase2-50;
            CP = CP-1;
            if (Player == 1) CDD();
            if (Player == 2) CDD2();
            if (Player == 1) Direction = 1;
            if (Player == 2) Direction2 = 1;
            Move.play();
          }
          if (IA == false && keyPressed == true && key == 40 || IA == true && (Player == 1 && keyPressed == true && key == 40 || Player == 2 && Direction2 == 2)) {
            if (Player == 1) ybase = ybase+50;
            if (Player == 2) ybase2 = ybase2+50;
            CP = CP-1;
            if (Player == 1) CDD();
            if (Player == 2) CDD2();
            if (Player == 1) Direction = 2;
            if (Player == 2) Direction2 = 2;
            Move.play();
          }
          if (IA == false && keyPressed == true && key == 37 || IA == true && (Player == 1 && keyPressed == true && key == 37 || Player == 2 && Direction2 == 3)) {
            if (Player == 1) xbase = xbase-50;
            if (Player == 2) xbase2 = xbase2-50;
            CP = CP-1;
            if (Player == 1) CDD();
            if (Player == 2) CDD2();
            if (Player == 1) Direction = 3;
            if (Player == 2) Direction2 = 3;
            Move.play();
          }
          if (IA == false && keyPressed == true && key == 39 || IA == true && (Player == 1 && keyPressed == true && key == 39 || Player == 2 && Direction2 == 4)) {
            if (Player == 1) xbase = xbase+50;
            if (Player == 2) xbase2 = xbase2+50;
            CP = CP-1;
            if (Player == 1) CDD();
            if (Player == 2) CDD2();
            if (Player == 1) Direction = 4;
            if (Player == 2) Direction2 = 4;
            Move.play();
          }

          if (TestCadriD == 0 && (IA == false && keyPressed == true && key == 38 || IA == true && (Player == 1 && keyPressed == true && key == 38 || Player == 2 && Direction2 == 1))) {
            if (Player == 1) ybase = ybase+50;
            if (Player == 2) ybase2 = ybase2+50;
            CP = CP+1;
            TestCadriD = 1;
          }
          if (TestCadriD == 0 && (IA == false && keyPressed == true && key == 40 || IA == true && (Player == 1 && keyPressed == true && key == 40 || Player == 2 && Direction2 == 2))) {
            if (Player == 1) ybase = ybase-50;
            if (Player == 2) ybase2 = ybase2-50;
            CP = CP+1;
            TestCadriD = 1;
          }
          if (TestCadriD == 0 && (IA == false && keyPressed == true && key == 37 || IA == true && (Player == 1 && keyPressed == true && key == 37 || Player == 2 && Direction2 == 3))) {
            if (Player == 1) xbase = xbase+50;
            if (Player == 2) xbase2 = xbase2+50;
            CP = CP+1;
            TestCadriD = 1;
          }
          if (TestCadriD == 0 && (IA == false && keyPressed == true && key == 39 || IA == true && (Player == 1 && keyPressed == true && key == 39 || Player == 2 && Direction2 == 4))) {
            if (Player == 1) xbase = xbase-50;
            if (Player == 2) xbase2 = xbase2-50;
            CP = CP+1;
            TestCadriD = 1;
          }

          AffTank();
          fill(200, 200, 200);

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
    background(0, 0, 0);
    fill(255, 0, 0);
    textSize(40);
    textAlign(CENTER);
    text("Player 2 WIN", 250, 220);
    textSize(20);
    text("Click SPACE to return to menu", 250, 300);
    Winner = 2;
  }
  if (TimerMin <= -1 && vietank2 < vietank1 || vietank2<1) {
    background(0, 0, 0);
    fill(0, 0, 255);
    textSize(40);
    textAlign(CENTER);
    text("Player 1 WIN", 250, 220);
    textSize(20);
    text("Click SPACE to return to menu", 250, 300);
    Winner = 1;
  }
  if (TimerMin <= -1 && vietank1 == vietank2) { //Egalité
    background(0, 0, 0);
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
    fill(255, 255, 255);
    text(TimerMin+":"+TimerSec, width-10, 20);
  }
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



/*function Credits(){
  image(Credits,0,0);
  fill(101,149,99);
  textAlign(CENTER);
  text("Programmation : Nathan Vey & Benjamin Robert",250,200);
  text("Texture : Benjamin Robert & RPG Maker",250,270);
  text("Sound : FreeSound, La Sonothèque & Nathan Vey",250,340);
  text("Music : Rémi Ginzburg",250,410);
  text("Press TAB to back",250,515);
}

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
/*
//Si une touche est appuyé, faire ce qui est demandé en fonction du menu affiché
document.addEventListener('keydown', function(event) {
  key = event.keyCode;
  console.log("toshow : "+toshow+", new key :" + key + ", menu : "+Menu);
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

//Nous voila parti pour quelque chose de plutôt complexe -.-'
//JSONObject Traj;
var IA = false, inDev = true;
var MaxDepl = 0, max = 0, needed = 1;
var diffX, diffY, DeplNeed;
var Traj = [
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0];

function IA(state) { // Ici sont effectuées toutes les décisions de l'IA

  if (state == "choix") { //Si c'est au tour de l'IA de jouer, elle choisit ce qu'elle veut faire
    //println("x1 : "+xbase/50+", x2 : "+xbase2/50+", diff y : "+abs(ybase - ybase2)/50+", y1 : "+ybase/50+", y2 : "+ybase2/50+", diff x : "+abs(xbase - xbase2)/50);
    if (Act > 1 && (xbase == xbase2 && Math.abs(ybase - ybase2) < 7*50 || ybase == ybase2 && Math.abs(xbase - xbase2) < 7*50)) { //Si le tank ennemi est aligné à nous et qu'il nous reste au moins une action
      choix = 1; //Choisir de tirer
    } else choix = 2; //Choisir de bouger (s'approcher si elle est trop loin, fuir s'il ne lui reste qu'une action)
    delay(200);
    return choix; //Renvoyer son choix
  }

  if (state == "shoot") { //Si elle veut tirer
    if (xbase == xbase2 && Math.abs(ybase - ybase2) < 7*50) { //Si elle est aligné au joueur en x
      if (ybase < ybase2) Direction2 = 1; //Tirer en haut
      if (ybase > ybase2) Direction2 = 2; //Tirer en bas
    }
    if (ybase == ybase2 && Math.abs(xbase - xbase2) < 7*50) { //Si elle est aligné au joueur en y
      if (xbase < xbase2) Direction2 = 3; //Tirer à gauche
      if (xbase > xbase2) Direction2 = 4; //Tirer à droite
    }
    delay(200);
    IsFire2 = 1; //Indiquer qu'elle tire
    return Direction2; //Renvoyer la direction de son tir
  }

  if (state == "move") { //Si elle veut se déplacer
    if (inDev == false) {
      if (Act == 3 && CP > MaxDepl) CalculTraj(); //Calculer la nouvelle trajectoire optimale
      else {
        for (var y = 0; y<10; y++) { //Chercher la case suivante à laquelle elle doit aller
          for (var x = 0; x<10; x++) {
            if (Traj[x+y*10] == needed) { //Une fois qu'elle est trouvé, savoir dans quelle direction elle est par rapport à l'IA
              if (y < ybase2/50) Direction2 = 1; //S'orienter vers le haut
              if (y > ybase2/50) Direction2 = 2; //S'orienter vers le bas
              if (x < xbase2/50) Direction2 = 3; //S'orienter vers la gauche
              if (x > xbase2/50) Direction2 = 4; //S'orienter vers la droite
            }
          }
        }
          if (needed + 1 == max) needed--;
          else needed ++;
          //Traj[xbase2/50+ybase2/50*10] = 0;
        }
      } else Direction2 = random(1, 5); //TEMPORAIRE, juste le temps que j'implante les décisions de déplacement. Pour le moment il se contente d'avancer aléatoirement

      delay(1000);
      return Direction2; //Renvoyer la direction vers laquelle elle avance
    }
    return -1; //En cas d'erreur, renvoyer -1
  }


  /*
Si nous ne sommes pas alligné
   S'il nous reste de la vie
   S'il reste des choix
   S'il reste des déplacments
   
   Prendre en compte :
   Ete:
   Peut pas aller sur la lave / montagne
   Vitesse/2 sur l'eau
   
   Hiver:
   Eviter la lave (perte de vie)
   Peut pas aller sur les montagnes
   Glisse sur la glace (toute une longueur = 1 déplacement)
   */
/*
  function CalculTraj() {
    MaxDepl = CP;
    for (var l = 0; l<10; l++) for (var j = 0; j<10; j++) Traj[j+l*10] = 0; //reset de la map de déplacement
    var i = 0;
    Traj[xbase/50+ybase/50*10] = -1;
    var tempX = xbase2/50, tempY = ybase2/50;

    if (xbase > xbase2) {
      for (i = i; tempX != xbase/50; i++) {
        Traj[tempX+tempY*10] = i;
        tempX++;
      }
    }
    if (xbase < xbase2) {
      for (i = i; tempX != xbase/50; i++) {
        Traj[tempX+tempY*10] = i;
        tempX--;
      }
    }
    if (ybase > ybase2) {
      for (i = i; tempY != ybase/50; i++) {
        Traj[tempX+tempY*10] = i;
        tempY++;
      }
    }
    if (ybase < ybase2) {
      for (i = i; tempY != ybase/50; i++) {
        Traj[tempX+tempY*10] = i;
        tempY--;
      }
    }
    max = i;
    for (var l = 0; l<10; l++) {
      for (var j = 0; j<10; j++) {
        print(Traj[j+l*10]+" ");
      }
      println("");
    }
    //delay(10000000);
  }

function MainMenu() {
  fill(255, 255, 255);
  background(0, 0, 0);
  fill(101,149,99);
  textSize(20);
  textAlign("CENTER");
  image(BackgMenu,0,0);
  text("Game", 125+30, 150+60);
  text("Editor", 125+30, 350+50);
  text("Options", 375-30, 150+60);
  text("Credits", 375-30, 350+50);
  textSize(15);
  text("Select with arrows and enter and press esc to back", 250, 515);
  if (Menu==1) {
    image(BalleR, 25+30, 120+60);
    image(BalleL, 175+30, 120+60);
  }
  if (Menu==2) {
    image(BalleR, 25+30, 320+50);
    image(BalleL, 175+30, 320+50);
  }
  if (Menu==3) {
    image(BalleR, 275-30, 120+60);
    image(BalleL, 425-30, 120+60);
  }
  if (Menu==4) {
    image(BalleR, 275-30, 320+50);
    image(BalleL, 425-30, 320+50);
  }
  delay(10);
}

function MenuPlay() {
  if (Menu<1) Menu=1;
  if (Menu>4) Menu=4;
  background(0, 0, 0);
  textSize(20);
  textAlign(CENTER);
  image(BackgMenu,0,0);
  text("1 vs 1 Local", 250, 200);
  text("1 vs IA Local", 250, 270);
  text("Create Server", 250, 340);
  text("Join Server", 250, 410);
  textSize(15);
  text("Select with arrows and enter and press tab to back", 250, 515);
  image(BalleR, 100, Menu*70+100);
  image(BalleL, 350, Menu*70+100);
  delay(10);
}

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

  for (var x=0; x<10; x++) {
    for (var y=0; y<10; y++) {
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
  if (Selectile!=0) image(STile, Selectile*80-60, 505);
  //Affichage curseur sur la map pour le changement des textures
  if (Selectile==0) image(STile, XCursorEdit*50, YCursorEdit*50);
}

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
      for (var i=0; i<99; i++) {
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

      for (var i=0; i<99; i++) {
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

function Options() {
  image(BackOpt, 0, 0);
  fill(101, 149, 99);
  textAlign(LEFT);
  text("Music :", 100, 180);
  text("Sound effect :", 100, 244); //260
  text("Timer : ", 100, 308);
  text("Tank's Health :", 100, 372); //340
  text("Type of songs :", 100, 436); //420
  text("Season :", 100, 500); //500
  textSize(13);
  text("Back: Press Tab", 310, 105);
  text("OK: Press Right Arrow", 310, 85);


  //Sélection du paramètre

  if (MenuOpt==0) {
    if (keyPressed==true && key == 40 && SMenuOpt < 6) SMenuOpt++;
    if (keyPressed==true && key == 38 && SMenuOpt > 1) SMenuOpt--;
    image(BalleR, 40, 85+64*SMenuOpt);
    delay(100);
  }

  //Fond des barres de volume

  fill(55, 77, 54);
  rect(318, 162, 104, 24);
  rect(318, 226, 104, 24);
  fill(55, 77, 54);
  rect(320, 164, 100, 20);
  rect(320, 228, 100, 20);

  //Interface Musique

  fill(101, 149, 99);
  if (MenuOpt==1) {
    if (keyPressed == true && key == 39 && MusicVOL<100) MusicVOL++;
    if (keyPressed == true && key == 37 && MusicVOL>0) MusicVOL--;
    //Triangle de pour montrer comment régler le son
    triangledeselction();
    //La Barre se colore lorsqu'elle est en stade de modification
    fill(247, 153, 0);
  }
  //Affichage Barre de son
  rect(320, 164, MusicVOL, 20);

  //Interface Effets Sonores

  fill(101, 149, 99);
  if (MenuOpt==2) {
    if (keyPressed == true && key == 39 && SoundVOL<100) SoundVOL++;
    if (keyPressed == true && key == 37 && SoundVOL>0) SoundVOL--;
    //Triangle de pour montrer comment régler le son
    triangledeselction();
    //La Barre se colore lorsqu'elle est en stade de modification
    fill(247, 153, 0);
  }
  //Affichage Barre de son
  rect(320, 228, SoundVOL, 20);


  // Interface timer

  fill(101, 149, 99);
  if (MenuOpt == 3 && Link == 0) {
    if (keyPressed == true && key == 39) TSel = 2;
    if (keyPressed == true && key == 37) TSel = 1;
    fill(247, 153, 0);
    triangledeselction();

    if (TSel == 1) {
      triangle(327, 290, 337, 280, 347, 290);
      triangle(327, 315, 337, 325, 347, 315);
    }
    if (TSel == 2) {
      triangle(380, 290, 390, 280, 400, 290);
      triangle(380, 315, 390, 325, 400, 315);
    }

    if (keyPressed == true && key == 40) {
      if (TSel == 1 && DefaultMin > 0) DefaultMin --;
      if (TSel == 2 && DefaultSec > 0) DefaultSec --;
      delay(100);
    }
    if (keyPressed == true && key == 38) {
      if (TSel == 1 && DefaultMin < 60) DefaultMin ++;
      if (TSel == 2 && DefaultSec < 60) DefaultSec ++;
      delay(100);
    }
  }
  textSize(15);
  textAlign(RIGHT);
  text(DefaultMin+"   : ", 370, 308);
  textAlign(LEFT);
  text(DefaultSec, 380, 308);


  // Interface nombre de vie

  fill(101, 149, 99);
  //Dans le cas ou on arrive au menu option par le Menu principal
  if (MenuOpt==4 && Link==0) {
    if (keyPressed == true && key == 39 && DefaultVie<10) DefaultVie ++;
    if (keyPressed == true && key == 37 && DefaultVie>1) DefaultVie --;
    //Triangle de pour montrer comment régler le son
    triangledeselction();
    delay(100);
  }

  for (var i=0; i<DefaultVie; i++) image(Vies, 320+DefaultVie*i, 358);

  // Interface Type de son

  fill(101, 149, 99);

  if (MenuOpt==5) {
    if (keyPressed == true && key == 39 && TypeDeSon<2) TypeDeSon++;
    if (keyPressed == true && key == 37 && TypeDeSon>1) TypeDeSon--;
    triangledeselction();
    fill(247, 153, 0);
  }
  textSize(15);
  if (TypeDeSon==1) text("Default", 330, 436);
  if (TypeDeSon==2) text("Crazy", 330, 436);

  // Interface Design

  fill(101, 149, 99);
  if (MenuOpt==6 && Link==0) {
    if (keyPressed == true && key == 39 && Design<4) {
      Design++;
      delay(100);
    }
    if (keyPressed == true && key == 37 && Design>1) {
      Design--;
      delay(100);
    }
    triangledeselction();
    fill(247, 153, 0);
  }
  if (Design==3 && MenuOpt==6 && Link==0) {
    triangle(280, 470, 290, 460, 300, 470);
    triangle(280, 510, 290, 520, 300, 510);
    if (keyPressed == true && key == 38 && SummerDay<99) {
      SummerDay++;
      delay(100);
    }
    if (keyPressed == true && key == 40 && SummerDay>1) {
      SummerDay--;
      delay(100);
    }
  }
  if (Design==4 && MenuOpt==6 && Link==0) {
    triangle(380, 470, 390, 460, 400, 470);
    triangle(380, 510, 390, 520, 400, 510);
    if (keyPressed == true && key == 38 && WinterDay<99) {
      WinterDay++;
      delay(100);
    }
    if (keyPressed == true && key == 40 && WinterDay>1) {
      WinterDay--;
      delay(100);
    }
  }
  if (Design==1 && Link==0)text("Summer", 330, 500);
  if (Design==2 && Link==0)text("Winter", 330, 500);
  if (Design==1 && Link==0 || Design==2 && Link==0)Changementok = false;
  if (Design>2 && Link==0) {
    text("Summer: "+SummerDay+" & Winter: "+WinterDay, 243, 500);
    Changementok = true;
  }

  if (Design==1 && Link==1 && Changementok == false)text("Summer", 330, 500);
  if (Design==2 && Link==1 && Changementok == false)text("Winter", 330, 500);
  if (Changementok == true)text("Summer: "+SummerDay+" & Winter: "+WinterDay, 243, 500);

  //Dans le cas ou on arrive au menu option par le Jeu
  //if (MenuOpt==4 && Link==1) {
  //  fill(255, 0, 0);
  //  text("You can't change the number ", 280, 280+30);
  //  text("Tank's Health now", 310, 330+30);
  //  triangledeselction();
  //}
  if (Link == 1 && (MenuOpt == 6 || MenuOpt == 4 || MenuOpt == 3)) {
    fill(255, 0, 0);
    textAlign(CENTER);
    text("You can't change this one in game", 250, 490+30);
    textAlign(LEFT);
    triangledeselction();
  }

  //Affichage des Paramêtre
  fill(136, 222, 145);
  textSize(15);
  textAlign(RIGHT);

  text(MusicVOL, 420, 180);
  text(SoundVOL, 420, 244);
  text(DefaultVie, 420, 372);
}

function triangledeselction() {
  if (Design>2 || Changementok == true) triangle(230, 90+64*SMenuOpt+20, 240, 80+64*SMenuOpt+20, 240, 100+64*SMenuOpt+20);
  else triangle(300, 90+64*SMenuOpt+20, 310, 80+64*SMenuOpt+20, 310, 100+64*SMenuOpt+20);
  triangle(430, 80+64*SMenuOpt+20, 430, 100+64*SMenuOpt+20, 440, 90+64*SMenuOpt+20);
}*/