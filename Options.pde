void Options() {
  image(BackOpt,0,0);
  fill(101,149,99);
  textAlign(LEFT);
  text("Music:", 100, 150+30);
  text("Sound effect:", 100, 230+30);
  text("Tank's Health:", 100, 310+30);
  text("Type of songs:", 100, 390+30);
  text("Season:", 100, 470+30);
  textSize(13);
  text("Back: Press Tab", 310, 105);
  text("OK: Press Right Arrow", 310, 85);
  noStroke();


  //Sélection du paramètre

  if (MenuOpt==0) {
    if (keyPressed==true && keyCode == DOWN && SMenuOpt < 5)SMenuOpt++;
    if (keyPressed==true && keyCode == UP && SMenuOpt > 1)SMenuOpt--;
    image(BalleR,40, 70+80*SMenuOpt);
    delay(100);
  }

  //Fond des barres de volume

  fill(55,77,54);
  rect(318, 130+28, 104, 24);
  rect(318, 210+28, 104, 24);
  fill(55,77,54);
  rect(320, 130+30, 100, 20);
  rect(320, 210+30, 100, 20);

  //Interface Musique

  fill(101,149,99);
  if (MenuOpt==1) {
    if (keyPressed == true && keyCode == RIGHT && MusicVOL<100)MusicVOL++;
    if (keyPressed == true && keyCode == LEFT && MusicVOL>0)MusicVOL--;
    //Triangle de pour montrer comment régler le son
    triangledeselction();
    //La Barre se colore lorsqu'elle est en stade de modification
    fill(247, 153, 0);
  }
  //Affichage Barre de son
  rect(320, 130+30, (float)MusicVOL, 20);

  //Interface Effets Sonores

  fill(101,149,99);
  if (MenuOpt==2) {
    if (keyPressed == true && keyCode == RIGHT && SoundVOL<100)SoundVOL++;
    if (keyPressed == true && keyCode == LEFT && SoundVOL>0)SoundVOL--;
    //Triangle de pour montrer comment régler le son
    triangledeselction();
    //La Barre se colore lorsqu'elle est en stade de modification
    fill(247, 153, 0);
  }
  //Affichage Barre de son
  rect(320, 210+30, (float)SoundVOL, 20);

  // Interface nombre de vie

  fill(101,149,99);
  //Dans le cas ou on arrive au menu option par le Menu principal
  if (MenuOpt==3 && Link==0) {
    if (keyPressed == true && keyCode == RIGHT && vietank1<10) {
      vietank1++;
      vietank2++;
    }
    if (keyPressed == true && keyCode == LEFT && vietank2>1) {
      vietank1--;
      vietank2--;
    }
    //Triangle de pour montrer comment régler le son
    triangledeselction();
    delay(100);
  }
  //Dans le cas ou on arrive au menu option par le Jeu
  if (MenuOpt==3 && Link==1) {
    fill(255, 0, 0);
    text("You can't change the number ", 280, 280+30);
    text("Tank's Health now", 310, 330+30);
    triangledeselction();
  }
  for (int i=0; i<vietank1; i++)image(Vies, 320+vietank1*i, 290+30);

  // Interface Type de son

  fill(101,149,99);
  if (MenuOpt==4) {
    if (keyPressed == true && keyCode == RIGHT && TypeDeSon<2)TypeDeSon++;
    if (keyPressed == true && keyCode == LEFT && TypeDeSon>1)TypeDeSon--;
    triangledeselction();
    fill(247, 153, 0);
  }
  textSize(15);
  if (TypeDeSon==1)text("Default", 330, 390+30);
  if (TypeDeSon==2)text("Crazy", 330, 390+30);

  // Interface Design

  fill(101,149,99);
  if (MenuOpt==5) {
    if (keyPressed == true && keyCode == RIGHT && Design<2)Design++;
    if (keyPressed == true && keyCode == LEFT && Design>1)Design--;
    triangledeselction();
    fill(247, 153, 0);
  }
  if (Design==1)text("Summer", 330, 470+30);
  if (Design==2)text("Winter", 330, 470+30);

  //Affichage des Paramêtre
  fill(136,222,145);
  textSize(15);
  if (MusicVOL<10)text(MusicVOL, 410, 150+30);
  else if (MusicVOL==100)text(MusicVOL, 390, 150+30);
  else if (MusicVOL>9 && MusicVOL!=100)text(MusicVOL, 400, 150+30);
  if (SoundVOL<10)text(SoundVOL, 410, 230+30);
  else if (SoundVOL==100)text(SoundVOL, 390, 230+30);
  else if (SoundVOL>9 && SoundVOL!=100)text(SoundVOL, 400, 230+30);
  if (vietank1<10)text(vietank1, 410, 310+30);
  else text(vietank1, 400, 310+30);
}

void triangledeselction() {
  triangle(300, 50+80*SMenuOpt+10+30, 310, 50+80*SMenuOpt+30, 310, 50+80*SMenuOpt+20+30);
  triangle(430, 50+80*SMenuOpt+30, 430, 50+80*SMenuOpt+20+30, 440, 50+80*SMenuOpt+10+30);
}