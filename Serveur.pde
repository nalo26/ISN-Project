import processing.net.*;
Server myServer;
Client myClient;
int ServerPort = 1042;
String ServerIP = "";
JSONArray data = new JSONArray();
JSONObject dataO;

boolean IsMulti = false;
boolean AmIServer = false;

void ServerCreate() {

  // Essaie de démarrer un serveur sur ce pc hébergé sur le port 'ServerPort'
 // try {
    myServer = new Server(this, ServerPort);
    AmIServer = true;
 // } 
  // Si erreur lors de la création, alors afficher l'erreur
 // catch (IOException e) {
  //  e.printStackTrace();
    fill(255, 10, 10);
    text("Error while attempting to create the server", 250, 250);
    fill(255);
    AmIServer = false;
//  }
  // Creation du fichier serveur
  dataO = new JSONObject();
  dataO.setInt("id", 1);
  dataO.setInt("Vie", 0);
  dataO.setInt("PosX", 0);
  dataO.setInt("PosY", 0);
  dataO.setBoolean("Feu", false);
  dataO.setInt("DistFeu", 0);
  dataO.setInt("Direction", 0);
  data.setJSONObject(1, dataO);

  dataO = new JSONObject();
  dataO.setInt("id", 2);
  dataO.setInt("Vie", 0);
  dataO.setInt("PosX", 0);
  dataO.setInt("PosY", 0);
  dataO.setBoolean("Feu", false);
  dataO.setInt("DistFeu", 0);
  dataO.setInt("Direction", 0);
  data.setJSONObject(2, dataO);

  /* dataO = new JSONObject();
   StrCollision = str(Collision);
   dataO.setString("map", ""+StrCollision);
   data.setJSONObject(3, dataO);*/

  dataO = new JSONObject();
  dataO.setInt("tour", 1);
  data.setJSONObject(4, dataO);

  dataO = new JSONObject();
  dataO.setString("state", "");
  data.setJSONObject(5, dataO);

  dataO = new JSONObject();
  dataO.setInt("winner", 0);
  data.setJSONObject(6, dataO);
  
  //enregistrement du fichier serveur
  saveJSONArray(data, "data/data.json");
}

void ServerJoin() {
  background(0);
  textSize(12);
  textAlign(CENTER);
  text("Type server ip to join", 250, 150);
  text(ServerIP, 250, 250);
  if (CanJoin == true) {
    CanJoin = false;
    println("joining server");
  //  try {
      myClient = new Client(this, ServerIP, ServerPort);
      IsMulti = true;
  //  }
  //  catch (IOException e) {
     // e.printStackTrace();
      fill(250, 10, 10);
      text("error while attempting to join the server.", 250, 250);
      fill(255);
   // }
  }
}

/*
JSON format :

1 : Data Player 1
2 : Data Player 2
3 : Map (pas encore implémenté)
4 : Joueur qui doit jouer
5 : Etat de la partie (en cours / fini...)
6 : Gagnant de la partie si fini (0 sinon)
*/


/*
Server.disconnect()
 Server.active()
 Server.available()
 Server.stop()
 Server.write()
 Server.ip()
 
 Client.stop()                //Déconnection du serveur
 Client.active()              //Retourne true si le serveur est actif
 Client.ip()                  //Retourne l'addresse ip du serveur 
 Client.available()           //Retourne le nombre de bits envoyé et près à être lu par le serveur
 Client.clear()               //Efface les documents envoyé par le serveur
 Client.read()                //Retourne la valeur d'un document lu
 Client.readChar()            //Retourne la valeur d'un decument en format charactère
 Client.readBytes             //Lis tout ce que le serveur a envoyé
 Client.readBytesUntil()      //Lis ce que le serveur a envoyé à partir d'un charactère
 Client.readString()          //Lis un fichier en texte
 Client.readStringUntil()     //Lit du texte d'un fichier à partir d'un charactère
 Client.write()               //Ecrit au serveur
 */
