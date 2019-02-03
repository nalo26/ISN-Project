void Options(){
background(0);
fill(255);
textAlign(LEFT);
text("Music:",50,150);
text("Sound effect:",50,230);
text("Tank's Health:",50,310);
text("Type of songs:",50,390);
text("Game's Apparence:",50,470);
textSize(13);
text("Back: Press Tab",50,70);
text("OK: Press Right Arrow",50,50);


//Sélection du paramètre

if (MenuOpt==0){
if (keyPressed==true && keyCode == DOWN && SMenuOpt < 5)SMenuOpt++;
if (keyPressed==true && keyCode == UP && SMenuOpt > 1)SMenuOpt--;
rect(50,70+80*SMenuOpt+2,150,5);
delay(100);
}

//Fond des barres de volume

fill(150);
rect(320,130,100,20);
rect(320,210,100,20);

//Interface Musique

fill(230);
if (MenuOpt==1){
if(keyPressed == true && keyCode == RIGHT && MusicVOL<100)MusicVOL++;
if(keyPressed == true && keyCode == LEFT && MusicVOL>0)MusicVOL--;
//Triangle de pour montrer comment régler le son
triangledeselction();
//La Barre se colore lorsqu'elle est en stade de modification
fill(247,153,0);
}
//Affichage Barre de son
rect(320,130,(float)MusicVOL,20);

//Interface Effets Sonores

fill(230);
if (MenuOpt==2){
if(keyPressed == true && keyCode == RIGHT && SoundVOL<100)SoundVOL++;
if(keyPressed == true && keyCode == LEFT && SoundVOL>0)SoundVOL--;
//Triangle de pour montrer comment régler le son
triangledeselction();
//La Barre se colore lorsqu'elle est en stade de modification
fill(247,153,0);
}
//Affichage Barre de son
rect(320,210,(float)SoundVOL,20);

// Interface nombre de vie

fill(230);
//Dans le cas ou on arrive au menu option par le Menu principal
if(MenuOpt==3 && Link==0){
if(keyPressed == true && keyCode == RIGHT && vietank1<10){vietank1++;vietank2++;}
if(keyPressed == true && keyCode == LEFT && vietank2>1){vietank1--;vietank2--;}
//Triangle de pour montrer comment régler le son
triangledeselction();
delay(100);
}
//Dans le cas ou on arrive au menu option par le Jeu
if(MenuOpt==3 && Link==1){
fill(255,0,0);
text("You can't change the number ",280,280);
text("Tank's Health now",310,330);
triangledeselction();
}
for(int i=0;i<vietank1;i++)image(Vies,320+vietank1*i,290);

// Interface Type de son

fill(230);
if(MenuOpt==4){
if(keyPressed == true && keyCode == RIGHT && TypeDeSon<2)TypeDeSon++;
if(keyPressed == true && keyCode == LEFT && TypeDeSon>1)TypeDeSon--;
triangledeselction();
fill(247,153,0); 
}
textSize(15);
if(TypeDeSon==1)text("Default",330,390);
if(TypeDeSon==2)text("Crazy",330,390);

// Interface Design

fill(230);
if(MenuOpt==5){
if(keyPressed == true && keyCode == RIGHT && Design<2)Design++;
if(keyPressed == true && keyCode == LEFT && Design>1)Design--;
triangledeselction();
fill(247,153,0);
}
if(Design==1)text("V.1",330,470);
if(Design==2)text("V.2",330,470);

//Affichage des Paramêtre
fill(0);
textSize(15);
if(MusicVOL<10)text(MusicVOL,410,150);
else if (MusicVOL==100)text(MusicVOL,390,150);
else if (MusicVOL>9 && MusicVOL!=100)text(MusicVOL,400,150);
if(SoundVOL<10)text(SoundVOL,410,230);
else if (SoundVOL==100)text(SoundVOL,390,230);
else if (SoundVOL>9 && SoundVOL!=100)text(SoundVOL,400,230);
fill(255);
if(vietank1<10)text(vietank1,410,310);
else text(vietank1,400,310);


}

void triangledeselction(){
triangle(300,50+80*SMenuOpt+10,310,50+80*SMenuOpt,310,50+80*SMenuOpt+20);
triangle(430,50+80*SMenuOpt,430,50+80*SMenuOpt+20,440,50+80*SMenuOpt+10);
}