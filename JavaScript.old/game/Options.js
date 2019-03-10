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
  rect(320, 164, (float)MusicVOL, 20);

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
  rect(320, 228, (float)SoundVOL, 20);


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

  for (int i=0; i<DefaultVie; i++) image(Vies, 320+DefaultVie*i, 358);

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
}