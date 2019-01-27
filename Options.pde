void Options(){
background(0);
fill(255);
textAlign(LEFT);
text("Music:",50,150);
text("Sound effect:",50,300);
text("Tank's Health:",50,450);
textSize(13);
text("Back: Press Tab",50,70);
text("OK: Press Right Arrow",50,50);


//Sélection du paramètre

if (MenuOpt==0){
if (keyPressed==true && keyCode == DOWN && SMenuOpt < 3)SMenuOpt++;
if (keyPressed==true && keyCode == UP && SMenuOpt > 1)SMenuOpt--;
rect(50,150*SMenuOpt+2,150,6);
delay(100);
}

//Interface Musique

fill(150);
rect(320,120,100,20);
fill(230);
if (MenuOpt==1){
if(keyPressed == true && keyCode == RIGHT && MusicVOL<100)MusicVOL++;
if(keyPressed == true && keyCode == LEFT && MusicVOL>0)MusicVOL--;
//Triangle de pour montrer comment régler le son
triangle(300,130,310,120,310,140);
triangle(430,120,430,140,440,130);
//La Barre se colore lorsqu'elle est en stade de modification
fill(247,153,0);
}
//Affichage Barre de son
rect(320,120,(float)MusicVOL,20);
//Affichage Volume en décimal
fill(0);
textSize(15);
if(MusicVOL<10)text(MusicVOL,410,140);
else if (MusicVOL==100)text(MusicVOL,390,140);
else if (MusicVOL>9 && MusicVOL!=100)text(MusicVOL,400,140);


//Interface Effets Sonores


fill(150);
rect(320,270,100,20);
fill(230);
if (MenuOpt==2){
if(keyPressed == true && keyCode == RIGHT && SoundVOL<100)SoundVOL++;
if(keyPressed == true && keyCode == LEFT && SoundVOL>0)SoundVOL--;
//Triangle de pour montrer comment régler le son
triangle(300,280,310,270,310,290);
triangle(430,270,430,290,440,280);
//La Barre se colore lorsqu'elle est en stade de modification
fill(247,153,0);
}
//Affichage Barre de son
rect(320,270,(float)SoundVOL,20);
//Affichage Volume en décimal
fill(0);
textSize(15);
if(SoundVOL<10)text(SoundVOL,410,290);
else if (SoundVOL==100)text(SoundVOL,390,290);
else if (SoundVOL>9 && SoundVOL!=100)text(SoundVOL,400,290);


// Interface nombre de vie


fill(230);
if(MenuOpt==3 && Link==0){
if(keyPressed == true && keyCode == RIGHT && vietank1<10){vietank1++;vietank2++;}
if(keyPressed == true && keyCode == LEFT && vietank2>1){vietank1--;vietank2--;}
//Triangle de pour montrer comment régler le son
triangle(300,430,310,420,310,440);
triangle(430,420,430,440,440,430);
delay(100);
}
for(int i=0;i<vietank1;i++){
image(Vies,320+vietank1*i,420);
}
fill(255);
textSize(15);
if(vietank1<10)text(vietank1,410,440);
else text(vietank1,400,440);
if(MenuOpt==3 && Link==1){
fill(255,0,0);
text("You can't change the number ",260,470);
text("Tank's Health now",290,500);
triangle(300,430,310,420,310,440);
triangle(430,420,430,440,440,430);
}
}