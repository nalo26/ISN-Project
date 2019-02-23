//Nous voila parti pour quelque chose de plutôt complexe -.-'

boolean IA = false;
int MaxDepl = 0;

int IA(String state) { // Ici sont effectuées toutes les décisions de l'IA

  if (state == "choix") { //Si c'est au tour de l'IA de jouer, elle choisit ce qu'elle veut faire
    println("x1 : "+xbase/50+", x2 : "+xbase2/50+", diff y : "+abs(ybase - ybase2)/50+", y1 : "+ybase/50+", y2 : "+ybase2/50+", diff x : "+abs(xbase - xbase2)/50);
    if (Act > 1 && (xbase == xbase2 && abs(ybase - ybase2) < 7*50 || ybase == ybase2 && abs(xbase - xbase2) < 7*50)) { //Si le tank ennemi est aligné à nous et qu'il nous reste au moins une action
      choix = 1; //Choisir de tirer
    } else choix = 2; //Choisir de bouger
    delay(500);
    return choix; //Renvoyer notre choix
  }

  if (state == "shoot") { //Si elle veut tirer
    if (xbase == xbase2 && abs(ybase - ybase2) < 7*50) { //Si elle est aligné au joueur en x
      if (ybase < ybase2) Direction2 = 1; //Tirer en haut
      if (ybase > ybase2) Direction2 = 2; //Tirer en bas
    }
    if (ybase == ybase2 && abs(xbase - xbase2) < 7*50) { //Si elle est aligné au joueur en y
      if (xbase < xbase2) Direction2 = 3; //Tirer à gauche
      if (xbase > xbase2) Direction2 = 4; //Tirer à droite
    }
    delay(500);
    IsFire2 = 1; //Indiquer qu'elle tire
    return Direction2; //Renvoyer la direction de son tir
  }

  if (state == "move") { //Si elle veut se déplacer
   // if (CP > MaxDepl) CalculTraj(); //Calculer la nouvelle trajectoire optimale

    Direction2 = (int)random(1, 5); //TEMPORAIRE, juste le temps que j'implante les décisions de déplacement. Pour le moment il se contente d'avancer aléatoirement
    
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
    Glisse sur la glace (oute une longueur = 1 déplacement)
*/


void CalculTraj(){
  
}