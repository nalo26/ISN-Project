from ProcToPy import *

def MenuMaps():
	from Game import *
	#Menu de sélection des maps

	# /!\ Don't touch my creation Mouhahahahaha /!\
	if InteracMap == 0:
		background(0)
		textAlign(CENTER)
		image(BackgMenu, screen,0,0)
		font = textSize(20)
		text("Play with Map N°1", 250, 200)
		text("Play with Map N°2", 250, 300)
		text("Play with Map N°3", 250, 400)
		font = textSize(14)
		text("Press arrows to select your folder and press RIGHT to load file", 250, 515)
		textAlign(LEFT)

		CurseurMenuMaps()

		#Chargement des maps
		# Map1 = loadJSONObject("Map1.json")
		# Map2 = loadJSONObject("Map2.json")
		# Map3 = loadJSONObject("Map3.json")

		#Remplace la map par défault par celle sélectionée
		if keyCode == RIGHT:
			for i in range(100):
				CollisionID = str(i)
				if SelectMap == 1:
					pass
					# Collision[i] = Map1.getInt(CollisionID)
				if SelectMap == 2:
					pass
					# Collision[i] = Map2.getInt(CollisionID)
				if SelectMap == 3:
					pass
					# Collision[i] = Map3.getInt(CollisionID)
			toshow = "Game"

	if InteracMap == 1:
		background(0)
		textAlign(CENTER)
		image(BackgMenu, screen,0,0)
		ColorMaster = fill(101,149,99)
		font = textSize(20)
		text("Remplace Map N°1", 250, 200)
		text("Remplace Map N°2", 250, 300)
		text("Remplace Map N°3", 250, 400)
		font = textSize(13)
		text("Press arrows to select a backup location and press Enter to save file", 250, 515)
		textAlign(LEFT)

		CurseurMenuMaps()

		#Le joueur choisir d'enregistrer sa Map 
		if keyCode == ENTER:

			if SelectMap == 1:
				# Map1 = new JSONObject()
				pass
			if SelectMap == 2:
				# Map2 = new JSONObject()
				pass
			if SelectMap == 3:
				# Map3 = new JSONObject()
				pass

			for i in range(100):
				ColisionID = str(i)
				if SelectMap == 1:
					Map1.setInt(ColisionID, Collision[i])
				if SelectMap == 2:
					Map2.setInt(ColisionID, Collision[i])
				if SelectMap == 3:
					Map3.setInt(ColisionID, Collision[i])

			if SelectMap == 1:
				saveJSONObject(Map1, "data/Map1.json")
			if SelectMap == 2:
				saveJSONObject(Map2, "data/Map2.json")
			if SelectMap == 3:
				saveJSONObject(Map3, "data/Map3.json")

			toshow = "Menu"
			InteracMap = 0

def CurseurMenuMaps():
	from Game import *
	#Déplacement du curseur de choix
	if keyCode == DOWN and keyPressed == True and SelectMap < 3:
		SelectMap += 1
		delay(150)
	if keyCode == UP and keyPressed == True and SelectMap > 1:
		SelectMap -= 1
		delay(150)

	#Souligne le choix du joueur
	image(BalleR, screen, 100, SelectMap*100+70)
	image(BalleL, screen, 350, SelectMap*100+70)