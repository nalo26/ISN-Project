void MenuMaps(){
//Menu de sélection des maps

// /!\ Don't touch my creation Mouhahahahaha /!\
if (InteracMap==1){
background(0);
textAlign(CENTER);
text("Remplacer Map N°1",250,100);
text("Remplacer Map N°2",250,200);
text("Remplacer Map N°3",250,300);
textAlign(LEFT);
if(keyCode==DOWN && SelectMap<3){SelectMap++;delay(150);}
if(keyCode==UP && SelectMap>1){SelectMap--;delay(150);}
rect(150,SelectMap*100+10,200,5);
} 
  //Map1 = loadJSONObject("Map1.json");
  //Map2 = loadJSONObject("Map2.json");
  //Map3 = loadJSONObject("Map3.json");

  //json.setInt("id", 0);
  //json.setString("species", "Panthera leo");
  //json.setString("name", "Lion");

  //saveJSONObject(json, "data/new.json");
}

// Sketch saves the following to a file called "new.json":
// {
//   "id": 0,
//   "species": "Panthera leo",
//   "name": "Lion"
// }