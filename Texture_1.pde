    int Player = 0; //Joueur 1 et 2 changement
    int Act =0 ;
    int xbase = 0; // Emplacement tank 1
    int ybase = 0;
    int xbase2 = 450; // Emplacement tank 2
    int ybase2 = 450;
    int vietank1 = 5;
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
    int lock=0; //touche de tire vérouillée
    int lock2=0; //direction du tir
    int lock3=0;//Anti Enter*2 ( effet d'un key pressed pour enter car non ascii)
    int TestCadriD=0;//Test cadrillage renvoie 0 ou 1 => Si on peux passer ou pas
    int TD2 = 0 ;
    boolean Bas= false; //Variable détectant si plusieurs bord existes pour un angle (texture)
    boolean Haut= false;
    boolean Droite= false;
    boolean Gauche= false;
    int Menu=1;
    ////Maps
    int [] Collision = {
    0,2,2,4,4,0,0,1,1,3,
    0,2,2,2,4,4,0,0,0,3,
    0,1,2,2,0,0,0,3,0,0,
    0,1,2,2,2,0,0,0,1,1,
    0,0,2,2,2,2,0,0,0,1,
    1,0,0,0,2,2,2,2,0,0,
    1,1,0,0,0,2,2,2,1,0,
    0,0,3,0,0,0,2,2,1,0,
    3,0,0,0,4,4,2,2,2,0,
    3,1,1,0,0,4,4,2,2,0
    };
    //    int [] Collision = {
    //0,0,0,0,0,0,0,0,0,0,
    //0,1,1,3,2,2,3,1,1,0,
    //0,1,0,2,0,0,2,0,1,0,
    //0,3,2,0,4,4,0,2,3,0,
    //0,2,0,4,0,0,4,0,2,0,
    //0,2,0,4,0,0,4,0,2,0,
    //0,3,2,0,4,4,0,2,3,0,
    //0,1,0,2,0,0,2,0,1,0,
    //0,1,1,3,2,2,3,1,1,0,
    //0,0,0,0,0,0,0,0,0,0
    //};
    
void setup(){
size(500,500);
background(0);
//A changer pour changer la rapidité du jeu
frameRate(1000);

}
void CDD(){
    //Cadrillage Des Déplacements (Tanks)
  int CDDx = xbase/50;
  int CDDy = ybase/50*10;
  int CDD = CDDx + CDDy;
  
  //Colisions cotés de terrain (Déplacements)        si le tank rencontre la limite et qu'il se trouve sur de l'eau CP a besoin de +2 pour revenir a son etat initial
  if(CDDx<0){CDD=CDD+1;xbase=xbase+50;CP=CP+1;if (Collision [CDD] ==2){CP=CP+1;}}
  if(CDDy<0){CDD=CDD+10;ybase=ybase+50;CP=CP+1;if (Collision [CDD] ==2){CP=CP+1;}}
  if(CDDx>9){CDD=CDD-1;xbase=xbase-50;CP=CP+1;if (Collision [CDD] ==2){CP=CP+1;}}
  if(CDDy>90){CDD=CDD-10;ybase=ybase-50;CP=CP+1;if (Collision [CDD] ==2){CP=CP+1;}}
  
  
  //Si le tank veux aller dans un endroit qu'il ne peux traverser (Montagne)
  if (Collision [CDD] ==1){TestCadriD=0;TD2=1;}
    //Si le tank veux aller dans un endroit qu'il ne peux traverser (Lave)
  if (Collision [CDD] ==3){TestCadriD=0;TD2=1;}
  //Si le tank va dans l'eau (Il est alors ralenti)
  if (Collision [CDD] ==2){CP=CP-1;}
}
void CDD2(){
    //Cadrillage Des Déplacements (Tanks)
  int CDDx = xbase2/50;
  int CDDy = ybase2/50*10;
  int CDD = CDDx + CDDy;
  
  //Colisions cotés de terrain (Déplacements)        si le tank rencontre la limite et qu'il se trouve sur de l'eau CP a besoin de +2 pour revenir a son etat initial
  if(CDDx<0){CDD=CDD+1;xbase2=xbase2+50;CP=CP+1;if (Collision [CDD] ==2){CP=CP+1;}}
  if(CDDy<0){CDD=CDD+10;ybase2=ybase2+50;CP=CP+1;if (Collision [CDD] ==2){CP=CP+1;}}
  if(CDDx>9){CDD=CDD-1;xbase2=xbase2-50;CP=CP+1;if (Collision [CDD] ==2){CP=CP+1;}}
  if(CDDy>90){CDD=CDD-10;ybase2=ybase2-50;CP=CP+1;if (Collision [CDD] ==2){CP=CP+1;}}
  
  
  //Si le tank veux aller dans un endroit qu'il ne peux traverser (Montagne)
  if (Collision [CDD] ==1){TestCadriD=0;TD2=1;}
    //Si le tank veux aller dans un endroit qu'il ne peux traverser (Lave)
  if (Collision [CDD] ==3){TestCadriD=0;TD2=1;}
  //Si le tank va dans l'eau (Il est alors ralenti)
  if (Collision [CDD] ==2){CP=CP-1;}
}
void CDA(){
    //Cadrillage Des Attaques (Bullets)
  int CDAx = xbasem/50;
  int CDAy = ybasem/50*10;
  int CDA = CDAx + CDAy;
  
    //Colisions cotés de terrain (Attaque)
  if(CDAx<0){CDA=CDA+1;CB=0;}
  if(CDAy<0){CDA=CDA+10;CB=0;}
  if(CDAx>9){CDA=CDA-1;CB=0;}
  if(CDAy>90){CDA=CDA-10;CB=0;}
  
  //Si le tank veux aller dans un endroit qu'il ne peux traverser (Montagne)
  if (Collision [CDA] ==1){CB=0;}
    //Si le tank veux aller dans un endroit qu'il ne peux traverser (Foret)
  if (Collision [CDA] ==4){CB=0;}

}


void AffTank (){//Affiche le tank
delay(50);
background(45,139,97);
noStroke();

  for (int x=0;x<10;x++){
    for (int y=0;y<10;y++){
        int Ax = x;
        int Ay = y*10;
        int A = Ax + Ay;
        if(Collision [A] ==1){PImage Montagne;Montagne = loadImage("Montagne.png");image(Montagne,x*50,y*50);}//Couleur Roche
        if(Collision [A] ==2){
        //Eau
        PImage Eau; Eau = loadImage("Eau.png");image(Eau,x*50,y*50);
        
        //rebors eau
        if(A>10 && Collision [A-10] !=2){PImage Eauhaut; Eauhaut = loadImage("Lavehaut.png");image(Eauhaut,x*50,y*50);Haut=true;}
        if(A<90 && Collision [A+10] !=2){PImage Eaubas; Eaubas = loadImage("Lavebas.png");image(Eaubas,x*50,y*50);Bas=true;}
        if(A!=0 && A!=10 && A!=20 && A!=30 && A!=40 && A!=50 && A!=60 && A!=70 && A!=80 && A!=90 && Collision [A-1] !=2){PImage Eaugauche; Eaugauche = loadImage("Lavegauche.png");image(Eaugauche,x*50,y*50);Gauche=true;}
        if(A!=9 &&A!=19 && A!=29 && A!=39 && A!=49 && A!=59 && A!=69 && A!=79 && A!=89 && A!=99 && Collision [A+1] !=2){PImage Eaudroite; Eaudroite = loadImage("Lavedroite.png");image(Eaudroite,x*50,y*50);Droite=true;}

        //Coins/angles lave
        if(Haut==true && Droite==true){PImage Eauhetd; Eauhetd = loadImage("Lavehaut+droite.png");image(Eauhetd,x*50,y*50);}
        if(Haut==true && Gauche==true){PImage Eauhetg; Eauhetg = loadImage("Lavehaut+gauche.png");image(Eauhetg,x*50,y*50);}
        if(Bas==true && Droite==true){PImage Eaubetd; Eaubetd = loadImage("Lavebas+droite.png");image(Eaubetd,x*50,y*50);}
        if(Bas==true && Gauche==true){PImage Eaubetg; Eaubetg = loadImage("Lavebas+gauche.png");image(Eaubetg,x*50,y*50);}
        
        //Remise a 0 de la détection des tiles autours du blocs de lave
        Bas= false;
        Haut= false;
        Droite= false;
        Gauche= false;
    }//Couleur Eau
        
        if(Collision [A] ==3){
        //Lave
        PImage Lave; Lave = loadImage("Lave.png");image(Lave,x*50,y*50);
        //rebors lave
        if(A>10 && Collision [A-10] !=3){PImage Lavehaut; Lavehaut = loadImage("Lavehaut.png");image(Lavehaut,x*50,y*50);Haut=true;}
        if(A<90 && Collision [A+10] !=3){PImage Lavebas; Lavebas = loadImage("Lavebas.png");image(Lavebas,x*50,y*50);Bas=true;}
        if(A!=0 && A!=10 && A!=20 && A!=30 && A!=40 && A!=50 && A!=60 && A!=70 && A!=80 && A!=90 && Collision [A-1] !=3){PImage Lavegauche; Lavegauche = loadImage("Lavegauche.png");image(Lavegauche,x*50,y*50);Gauche=true;}
        if(A!=9 &&A!=19 && A!=29 && A!=39 && A!=49 && A!=59 && A!=69 && A!=79 && A!=89 && A!=99 && Collision [A+1] !=3){PImage Lavedroite; Lavedroite = loadImage("Lavedroite.png");image(Lavedroite,x*50,y*50);Droite=true;}

        //Coins/angles lave
        if(Haut==true && Droite==true){PImage Lavehetd; Lavehetd = loadImage("Lavehaut+droite.png");image(Lavehetd,x*50,y*50);}
        if(Haut==true && Gauche==true){PImage Lavehetg; Lavehetg = loadImage("Lavehaut+gauche.png");image(Lavehetg,x*50,y*50);}
        if(Bas==true && Droite==true){PImage Lavebetd; Lavebetd = loadImage("Lavebas+droite.png");image(Lavebetd,x*50,y*50);}
        if(Bas==true && Gauche==true){PImage Lavebetg; Lavebetg = loadImage("Lavebas+gauche.png");image(Lavebetg,x*50,y*50);}
        
        //Remise a 0 de la détection des tiles autours du blocs de lave
        Bas= false;
        Haut= false;
        Droite= false;
        Gauche= false;
        }//Couleur Lave
        
        //Foret/arbre en bas pour recouvrir les tank
        if(Collision [A] ==4){PImage arbre; arbre = loadImage("arbre.png");image(arbre,x*50,y*50);}//Couleur Foret
        
    }
  }
  
 //Selection entourage tank
      if(Player==1){PImage STank1; STank1 = loadImage("Selection Tank1.png");image(STank1,xbase,ybase);}
      if(Player==2){PImage STank2; STank2 = loadImage("Selection Tank2.png");image(STank2,xbase2,ybase2);}
      
 //Affichage Tank
      if (Direction == 1){PImage Tank1; Tank1 = loadImage("Tank1u.png");image(Tank1,xbase,ybase);}
      if (Direction == 2){PImage Tank1; Tank1 = loadImage("Tank1d.png");image(Tank1,xbase,ybase);}
      if (Direction == 3){PImage Tank1; Tank1 = loadImage("Tank1l.png");image(Tank1,xbase,ybase);}
      if (Direction == 4){PImage Tank1; Tank1 = loadImage("Tank1r.png");image(Tank1,xbase,ybase);}
      
      if (Direction2 == 1){PImage Tank2; Tank2 = loadImage("Tank2u.png");image(Tank2,xbase2,ybase2);}
      if (Direction2 == 2){PImage Tank2; Tank2 = loadImage("Tank2d.png");image(Tank2,xbase2,ybase2);}
      if (Direction2 == 3){PImage Tank2; Tank2 = loadImage("Tank2l.png");image(Tank2,xbase2,ybase2);}
      if (Direction2 == 4){PImage Tank2; Tank2 = loadImage("Tank2r.png");image(Tank2,xbase2,ybase2);}
      
      
 //Affichage des vies
      textSize(14);text("V1:",20,25);
      textSize(14);text(":V2",460,25);
      for(int viebarre1 = vietank1;viebarre1>0;viebarre1--){fill(150,32,32);PImage Vies; Vies = loadImage("Vies.png");image(Vies,12*viebarre1+40,20,8,8);}
      for(int viebarre2 = vietank2;viebarre2>0;viebarre2--){fill(150,32,32);PImage Vies; Vies = loadImage("Vies.png");image(Vies,-12*viebarre2+460,20,8,8);}
}


void draw(){
  
  background(0);
  textSize(12);
  text("Nom du jeu",220,50);
  text("Select with arrows and enter",170,150);
  text("Jeu",120,250);
  text("Editeur",220,250);
  text("Options",320,250);
  text("Press esc to back",200,350);
  rect(Menu*100+20,270,70,5);
  if(keyPressed==true && keyCode==RIGHT){Menu++;}
  if(keyPressed==true && keyCode==LEFT){Menu--;}
  if(Menu<1){Menu=1;}
  if(Menu>3){Menu=3;}
  delay(150);
  
  
//Menu 1 =Jeu
if(Menu==1 && keyPressed==true && keyCode==ENTER){
  
  if (Player==0 && Act==0 && vietank1>0 && vietank2>0|| Player==2 && Act==0 && vietank1>0 && vietank2>0){
    background(0);
    fill(0,0,255);
    textSize(40);
    text("Player 1",160,220);
    text("Press  Down",130,270);
    if (keyPressed==true && keyCode==DOWN){Player=1;Act=3;}
}

if (Player==1 && Act==0 && vietank1>0 && vietank2>0){
    background(0);  
    fill(255,0,0);
    textSize(40);
    text("Player 2",160,220);
    text("Press  Down",130,270);
    if (keyPressed==true && keyCode==DOWN){Player=2;Act=3;}
}

if (vietank1<1){background(0);fill(0,0,255);textSize(40);text("Player 1 WIN",130,220);}
if (vietank2<1){background(0);fill(255,0,0);textSize(40);text("Player 2 WIN",130,220);}

if(Player==1 && Act>0){
  
      AffTank();
  
  if (choix==0){//Choix des actions (Left=Shoot/Right=Move)
 
    if (keyCode==LEFT){//Lorsque le curseur est sur Shoot
      choix2=1;
      choix3=1;
      fill(200,50,0);//Souligne en rouge le choix Left
      rect(70,260,160,5);
    }
    
    if (keyCode==RIGHT){//Lorsque le curseur est sur Move
      choix2=2;
      choix3=1;
      fill(200,50,0);//Souligne en rouge le choix Right
      rect(250,260,160,5);
    }
    
    if (choix3==1 && keyCode==ENTER){choix=choix2;choix3=0;}//Lorsque l'action est choisie par Enter
    
    fill(200);
    textSize(20);
    text("Press arrow",175,200);
    text("Left(for Attack)     Right(for move)",75,250);
    text("And then press Enter",140,300);
  }
  
  
  if (choix==1){//Shoot

    if (CB<1 || lock==0){
      CB = random(10);
      CB = int(CB);
      println(CB);
      
      xbasem=xbase;
      ybasem=ybase; 
      
      AffTank();
      
      fill(200);
      textSize(20);
      text("Press arrows to shoot your bullet in a direction",30,430);
      text("Then press Enter",180,480);
      
      if ( keyCode==UP){lock2=1;lock3=1;triangle(xbase+10,ybase-10,xbase+40,ybase-10,xbase+25,ybase-30);Direction=1;}
      if ( keyCode==DOWN){lock2=2;lock3=1;triangle(xbase+10,ybase+60,xbase+40,ybase+60,xbase+25,ybase+80);Direction=2;}
      if ( keyCode==LEFT){lock2=3;lock3=1;triangle(xbase-10,ybase+10,xbase-10,ybase+40,xbase-30,ybase+25);Direction=3;}
      if ( keyCode==RIGHT){lock2=4;lock3=1;triangle(xbase+60,ybase+10,xbase+60,ybase+40,xbase+80,ybase+25);Direction=4;}
      if (lock3==1 && keyCode==ENTER){lock=lock2;lock3=0;}
    
    }
    
    if(CB>0 && lock!=0){
      
      CB=CB-1;
      
      if(lock==1){ybasem=ybasem-50;CDA();}
      if(lock==2){ybasem=ybasem+50;CDA();}
      if(lock==3){xbasem=xbasem-50;CDA();}
      if(lock==4){xbasem=xbasem+50;CDA();}
      
      if(xbasem==xbase2 && ybasem==ybase2){CB=0;vietank2=vietank2-1;}
      
      AffTank();
      if(lock==1){PImage Balle; Balle = loadImage("BalleU.png");image(Balle,xbasem,ybasem);}
      if(lock==2){PImage Balle; Balle = loadImage("BalleD.png");image(Balle,xbasem,ybasem);}
      if(lock==3){PImage Balle; Balle = loadImage("BalleL.png");image(Balle,xbasem,ybasem);}
      if(lock==4){PImage Balle; Balle = loadImage("BalleR.png");image(Balle,xbasem,ybasem);}
      //fill(0);
      //rect(xbasem+12,ybasem+12,25,25);
      fill(200);
      textSize(50);
      text(CB,450,490,500);
  
    }
    
    if(CB<1 && lock!=0){
      
      choix=0;
      lock=0;

      AffTank();
      
      fill(250,180,0);
      rect(xbasem+12,ybasem+12,25,25); 
      Act=Act-1;
    }
    
  }
  
  
  if (choix==2){//Move
  
  //Initialisation du dès de déplacements
  if (CP<1){
  CP = random(10);
  CP = int(CP);
  println(CP);
  }
  
  //Déplacements lorsque CP est != de 0 (Joueur a encore des déplacements)
  if (CP>0){
    
  if (keyPressed==true && keyCode==UP /*&& arrows==0*/){ybase= ybase-50;CP=CP-1;CDD();Direction=1;/*arrows=1;*/}
  if (keyPressed==true && keyCode==DOWN /*&& arrows==0*/){ybase= ybase+50;CP=CP-1;CDD();Direction=2;/*arrows=1;*/}
  if (keyPressed==true && keyCode==LEFT /*&& arrows==0*/){xbase= xbase-50;CP=CP-1;CDD();Direction=3;/*arrows=1;*/}
  if (keyPressed==true && keyCode==RIGHT /*&& arrows==0*/){xbase= xbase+50;CP=CP-1;CDD();Direction=4;/*arrows=1;*/}
  //if (keyPressed==false && arrows==1){arrows=0;}
  
  if (keyCode==UP && TestCadriD==0){ybase= ybase+50;CP=CP+1;TestCadriD=1;}
  if (keyCode==DOWN && TestCadriD==0){ybase= ybase-50;CP=CP+1;TestCadriD=1;}
  if (keyCode==LEFT && TestCadriD==0){xbase= xbase+50;CP=CP+1;TestCadriD=1;}
  if (keyCode==RIGHT && TestCadriD==0){xbase= xbase-50;CP=CP+1;TestCadriD=1;}
  
  AffTank();
  fill(200);
    
  textSize(50);
  text(CP,450,490,500);
  println(CP);
  }
  
    //Déplacements lorsque CP est inférieur à 0 (Joueur n'a plus de déplacements)
 if (CP<1){choix=0;Act=Act-1;}
  
}
}
if(Player==2 && Act>0){
  
      AffTank();
  
  if (choix==0){//Choix des actions (Left=Shoot/Right=Move)
 
    if (keyCode==LEFT){//Lorsque le curseur est sur Shoot
      choix2=1;
      choix3=1;
      fill(200,50,0);//Souligne en rouge le choix Left
      rect(70,260,160,5);
    }
    
    if (keyCode==RIGHT){//Lorsque le curseur est sur Move
      choix2=2;
      choix3=1;
      fill(200,50,0);//Souligne en rouge le choix Right
      rect(250,260,160,5);
    }
    
    if (choix3==1 && keyCode==ENTER){choix=choix2;choix3=0;}//Lorsque l'action est choisie par Enter
    
    fill(200);
    textSize(20);
    text("Press arrow",175,200);
    text("Left(for Attack)     Right(for move)",75,250);
    text("And then press Enter",140,300);
  }
  
  
  if (choix==1){//Shoot

    if (CB<1 || lock==0){
      CB = random(10);
      CB = int(CB);
      println(CB);
      
      xbasem=xbase2;
      ybasem=ybase2; 
      
      AffTank();
      
      fill(200);
      textSize(20);
      text("Press arrows to shoot your bullet in a direction",30,430);
      text("Then press Enter",180,480);
      
      if ( keyCode==UP){lock2=1;lock3=1;triangle(xbase2+10,ybase2-10,xbase2+40,ybase2-10,xbase2+25,ybase2-30);Direction2=1;}
      if ( keyCode==DOWN){lock2=2;lock3=1;triangle(xbase2+10,ybase2+60,xbase2+40,ybase2+60,xbase2+25,ybase2+80);Direction2=2;}
      if ( keyCode==LEFT){lock2=3;lock3=1;triangle(xbase2-10,ybase2+10,xbase2-10,ybase2+40,xbase2-30,ybase2+25);Direction2=3;}
      if ( keyCode==RIGHT){lock2=4;lock3=1;triangle(xbase2+60,ybase2+10,xbase2+60,ybase2+40,xbase2+80,ybase2+25);Direction2=4;}
      if (lock3==1 && keyCode==ENTER){lock=lock2;lock3=0;}
    
    }
    
    if(CB>0 && lock!=0){
      
      CB=CB-1;
      
      if(lock==1){ybasem=ybasem-50;CDA();}
      if(lock==2){ybasem=ybasem+50;CDA();}
      if(lock==3){xbasem=xbasem-50;CDA();}
      if(lock==4){xbasem=xbasem+50;CDA();}
      
      if(xbasem==xbase && ybasem==ybase){CB=0;vietank1=vietank1-1;}
      
      AffTank();
      if(lock==1){PImage Balle; Balle = loadImage("BalleU.png");image(Balle,xbasem,ybasem);}
      if(lock==2){PImage Balle; Balle = loadImage("BalleD.png");image(Balle,xbasem,ybasem);}
      if(lock==3){PImage Balle; Balle = loadImage("BalleL.png");image(Balle,xbasem,ybasem);}
      if(lock==4){PImage Balle; Balle = loadImage("BalleR.png");image(Balle,xbasem,ybasem);}
      //fill(0);
      //rect(xbasem+12,ybasem+12,25,25);
      fill(200);
      textSize(50);
      text(CB,450,490,500);
  
    }
    
    if(CB<1 && lock!=0){
      
      choix=0;
      lock=0;

      AffTank();
      
      fill(250,180,0);
      rect(xbasem+12,ybasem+12,25,25); 
      Act=Act-1;
    }
    
  }
  
  
  if (choix==2){//Move
  
  //Initialisation du dès de déplacements
  if (CP<1){
  CP = random(10);
  CP = int(CP);
  println(CP);
  }
  
  //Déplacements lorsque CP est != de 0 (Joueur a encore des déplacements)
  if (CP>0){
    
  if (keyPressed==true && keyCode==UP /*&& arrows==0*/){ybase2= ybase2-50;CP=CP-1;CDD2();Direction2=1;/*arrows=1;*/}
  if (keyPressed==true && keyCode==DOWN /*&& arrows==0*/){ybase2= ybase2+50;CP=CP-1;CDD2();Direction2=2;/*arrows=1;*/}
  if (keyPressed==true && keyCode==LEFT /*&& arrows==0*/){xbase2= xbase2-50;CP=CP-1;CDD2();Direction2=3;/*arrows=1;*/}
  if (keyPressed==true && keyCode==RIGHT /*&& arrows==0*/){xbase2= xbase2+50;CP=CP-1;CDD2();Direction2=4;/*arrows=1;*/}
  //if (keyPressed==false && arrows==1){arrows=0;}
  
  if (keyCode==UP && TestCadriD==0){ybase2= ybase2+50;CP=CP+1;TestCadriD=1;}
  if (keyCode==DOWN && TestCadriD==0){ybase2= ybase2-50;CP=CP+1;TestCadriD=1;}
  if (keyCode==LEFT && TestCadriD==0){xbase2= xbase2+50;CP=CP+1;TestCadriD=1;}
  if (keyCode==RIGHT && TestCadriD==0){xbase2= xbase2-50;CP=CP+1;TestCadriD=1;}
  
  AffTank();
  fill(200);
    
  textSize(50);
  text(CP,450,490,500);
  println(CP);
  }
  
    //Déplacements lorsque CP est inférieur à 0 (Joueur n'a plus de déplacements)
 if (CP<1){choix=0;Act=Act-1;}
  
}
}
}
//Menu 2 = Editeur de niveau
if(Menu==2 && keyPressed==true && keyCode==ENTER){}
//Menu 3 = Parametres
if(Menu==3 && keyPressed==true && keyCode==ENTER){}
}