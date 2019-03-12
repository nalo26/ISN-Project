from ProcToPy import *

def MenuEditor():
	from Game import *
	AffEditeur()
	font = textSize(10)
	text("SHIFT=Print",450,515)
	text("ENTER=Switch",450,525)
	text("TAB=Save",450,535)
	text("TAB+SHIFT=Menu",450,545)

	#Enter permet d'accéder au choix des types de terrains (ex:montagne,lave...) qui vont remplacer ceux choisit par le curseur  
	if keyCode == ENTER and Selectile == 0 and LockTile == 0:
		Selectile = 1
		LockTile = 1
	if keyCode == ENTER and Selectile != 0 and LockTile == 0:
		Selectedtile -= 1
		Selectile = 0
		LockTile = 1
	#A changer plus tard (Force le joueur a choisir une texture avec les fleches avant de valider
	if keyPressed == True:
		LockTile = 0

	#Déplacement du curseur
	if keyPressed == True and keyCode == LEFT and Selectile == 0 and XCursorEdit != 0:
		XCursorEdit -= 1
	if keyPressed == True and keyCode == RIGHT and Selectile == 0 and XCursorEdit != 9:
		XCursorEdit += 1
	if keyPressed == True and keyCode == UP and Selectile == 0 and YCursorEdit != 0:
		YCursorEdit -= 1
	if keyPressed == True and keyCode == DOWN and Selectile == 0 and YCursorEdit != 9:
		YCursorEdit += 1
	if keyPressed == True and keyCode == LEFT and Selectile != 0 and Selectile != 1:
		Selectile -= 1
	if keyPressed == True and keyCode == RIGHT and Selectile != 0 and Selectile != 5:
		Selectile += 1

	#Remplace le terrain choisit par le curseur par celui choisit dans la barre d'info (En appuyant sur Shift)
	if keyPressed == True and keyCode == SHIFT and Selectile == 0:
		Collision[XCursorEdit+YCursorEdit*10] = Selectedtile

def AffEditeur (): #Affiche l'éditeur
	from Game import *
	delay(150)
	background(45, 139, 97)
	ColorMaster = fill(0)
	rect(0, 500, 500, 50)
	ColorMaster = fill(200)
	rect(0, 500, 500, 3)
	noStroke()

	for x in range(10):
		for y in range(10):
			Ax = x
			Ay = y*10
			A = Ax + Ay
			if Collision[A] == 1: #Couleur Roche
				image(Montagne, screen, x*50, y*50) 
			if Collision[A] == 2: #Couleur Eau
				image(Eau, screen, x*50, y*50) #Eau

				#rebors eau
				if A > 10 and Collision[A-10] != 2:
					image(ContH, screen, x*50, y*50)
					Haut = True
				if A < 90 and Collision[A+10] != 2:
					image(ContB, screen, x*50, y*50)
					Bas = True
				if A!=0 and A!=10 and A!=20 and A!=30 and A!=40 and A!=50 and A!=60 and A!=70 and A!=80 and A!=90 and Collision[A-1] != 2:
					image(ContG, screen, x*50, y*50)
					Gauche = True
				if A!=9 and A!=19 and A!=29 and A!=39 and A!=49 and A!=59 and A!=69 and A!=79 and A!=89 and A!=99 and Collision[A+1] != 2:
					image(ContD, screen, x*50, y*50)
					Droite = True

				#Coins/angles lave
				if Haut == True and Droite == True:
					image(ContHD, screen, x*50, y*50)
				if Haut == True and Gauche == True:
					image(ContHG, screen, x*50, y*50)
				if Bas == True and Droite == True:
					image(ContBD, screen, x*50, y*50)
				if Bas == True and Gauche == True:
					image(ContBG, screen, x*50, y*50)

				#Remise a 0 de la détection des tiles autours du blocs de lave
				Bas = False
				Haut = False
				Droite = False
				Gauche = False

			if Collision[A] == 3: #Lave
				image(Lave, screen, x*50, y*50) #rebors lave
				if A > 10 and Collision[A-10] != 3:
					image(ContH, screen, x*50, y*50)
					Haut = True
				if A < 90 and Collision[A+10] != 3:
					image(ContB, screen, x*50, y*50)
					Bas = True
				if A!=0 and A!=10 and A!=20 and A!=30 and A!=40 and A!=50 and A!=60 and A!=70 and A!=80 and A!=90 and Collision[A-1] != 3:
					image(ContG, screen, x*50, y*50)
					Gauche = True
				if A!=9 and A!=19 and A!=29 and A!=39 and A!=49 and A!=59 and A!=69 and A!=79 and A!=89 and A!=99 and Collision[A+1] != 3:
					image(ContD, screen, x*50, y*50)
					Droite = True

				#Coins/angles lave
				if Haut == True and Droite == True:
					image(ContHD, screen, x*50, y*50)
				if Haut == True and Gauche == True:
					image(ContHG, screen, x*50, y*50)
				if Bas == True and Droite == True:
					image(ContBD, screen, x*50, y*50)
				if Bas == True and Gauche == True:
					image(ContBG, screen, x*50, y*50)

				#Remise a 0 de la détection des tiles autours du blocs de lave
				Bas = False
				Haut = False
				Droite = False
				Gauche = False

			#Foret/arbre en bas pour recouvrir les tank
			if (Collision [A] ==4):
				image(arbre, screen, x*50, y*50) #Couleur Foret

	#Affiche les terrains proposées en barre d'info
	ColorMaster = fill(45, 139, 97)
	rect(20, 505, 50, 50)
	image(Montagne, screen, 100, 505)
	image(Eau, screen, 180, 505)
	image(Lave, screen, 260, 505)
	image(arbre, screen, 340, 505)

	#Affichage selection dans la barre d'info lors du choix de la texture
	if Selectile != 0:
		# PImage STile 
		# STile = loadimage("Selection Tank2.png")
		image(STile, screen, Selectile*80-60, 505)
	#Affichage curseur sur la map pour le changement des textures
	if Selectile == 0:
		# PImage STile 
		# STile = loadimage("Selection Tank2.png")
		image(STile, screen, XCursorEdit*50, YCursorEdit*50)