void Menu2(){
  AffEditeur();
  int Selectile=0;
  
if(keyCode==ENTER && Selectile==0){Selectile=1;}
if(keyCode==ENTER && Selectile!=0){Selectile=0;}

if(keyPressed==true && keyCode==LEFT && Selectile==0){}
if(keyPressed==true && keyCode==RIGHT && Selectile==0){}
if(keyPressed==true && keyCode==DOWN && Selectile==0){}
if(keyPressed==true && keyCode==UP && Selectile==0){}

if(keyPressed==true && keyCode==LEFT && Selectile==1){}
if(keyPressed==true && keyCode==RIGHT && Selectile==1){}

  }
  
void AffEditeur (){//Affiche l'éditeur
delay(50);
background(45,139,97);
fill(0);
rect(0,500,500,50);
fill(200);
rect(0,500,500,3);
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
  fill(45,139,97);
  rect(20,505,50,50);
  PImage Montagne;Montagne = loadImage("Montagne.png");image(Montagne,90,505);
  PImage Eau; Eau = loadImage("Eau.png");image(Eau,160,505);
  PImage Lave; Lave = loadImage("Lave.png");image(Lave,240,505);
  PImage arbre; arbre = loadImage("arbre.png");image(arbre,300,505);
}
