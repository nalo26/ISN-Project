import processing.net.*;
Server myServer;
Client myClient;
int ServerPort = 1042;
String ServerIP = "";
JSONArray data = new JSONArray();
JSONObject dataO;

boolean IsMulti = false;
boolean AmIServer = false;
boolean AmIClient = false;

int Winner, DistFeu1, DistFeu2, IsFire1, IsFire2, DefaultLife = 5;

String dataIn;
String [] SdataList = {"0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"};
String [] CdataList = {"0", "0", "0", "0", "0", "0"};

void ServerCreate() {
  DefaultLife = vietank1;
  // Essaie de démarrer un serveur sur ce pc hébergé sur le port 'ServerPort'
  if (AmIServer == false) {
    myServer = new Server(this, ServerPort);
    IsMulti = true;
    AmIServer = true;
    AmIClient = false;
    toshow = "MenuMaps";
  }
}

void ServerJoin() {
  background(0);
  textSize(12);
  textAlign(CENTER);
  text("Type server ip to join", 250, 150);
  text(ServerIP, 250, 250);
  if (CanJoin == true) {
    CanJoin = false;
    //println("joining server");
    myClient = new Client(this, ServerIP, ServerPort);
    IsMulti = true;
    AmIClient = true;
    AmIServer = false;
    toshow = "Game";
  }
}



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
