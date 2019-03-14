import pygame
import settings as v
from ProcToPy import *
v.init()

def MenuEditor():
	AffEditeur()
	v.font = textSize(10)
	text("SHIFT=Print",450,515)
	text("ENTER=Switch",450,525)
	text("TAB=Save",450,535)
	text("TAB+SHIFT=Menu",450,545)

	#Enter permet d'accéder au choix des types de terrains (ex:montagne,lave...) qui vont remplacer ceux choisit par le curseur  
	if v.keyCode == pygame.K_RETURN and v.Selectile == 0 and v.LockTile == 0:
		v.Selectile = 1
		v.LockTile = 1
	if v.keyCode == pygame.K_RETURN and v.Selectile != 0 and v.LockTile == 0:
		v.Selectedtile -= 1
		v.Selectile = 0
		v.LockTile = 1
	#A changer plus tard (Force le joueur a choisir une texture avec les fleches avant de valider
	if v.keyCode != 0:
		v.LockTile = 0

	#Déplacement du curseur
	if v.keyCode == pygame.K_LEFT and v.Selectile == 0 and v.XCursorEdit != 0:
		v.XCursorEdit -= 1
	if v.keyCode == pygame.K_RIGHT and v.Selectile == 0 and v.XCursorEdit != 9:
		v.XCursorEdit += 1
	if v.keyCode == pygame.K_UP and v.Selectile == 0 and v.YCursorEdit != 0:
		v.YCursorEdit -= 1
	if v.keyCode == pygame.K_DOWN and v.Selectile == 0 and v.YCursorEdit != 9:
		v.YCursorEdit += 1
	if v.keyCode == pygame.K_LEFT and v.Selectile != 0 and v.Selectile != 1:
		v.Selectile -= 1
	if v.keyCode == pygame.K_RIGHT and v.Selectile != 0 and v.Selectile != 5:
		v.Selectile += 1

	#Remplace le terrain choisit par le curseur par celui choisit dans la barre d'info (En appuyant sur Shift)
	if v.keyCode == pygame.K_RSHIFT or v.keyCode == pygame.K_LSHIFT and v.Selectile == 0:
		v.Collision[v.XCursorEdit+v.YCursorEdit*10] = v.Selectedtile

def AffEditeur (): #Affiche l'éditeur
	delay(150)
	background(45, 139, 97)
	v.ColorMaster = fill(0)
	rect(0, 500, 500, 50)
	v.ColorMaster = fill(200)
	rect(0, 500, 500, 3)
	# noStroke()

	for x in range(10):
		for y in range(10):
			Ax = x
			Ay = y*10
			A = Ax + Ay
			if v.Collision[A] == 1: #Couleur Roche
				image(v.Montagne, x*50, y*50) 
			if v.Collision[A] == 2: #Couleur Eau
				image(v.Eau, x*50, y*50) #Eau

				#rebors eau
				if A > 10 and v.Collision[A-10] != 2:
					image(v.ContH, x*50, y*50)
					v.Haut = True
				if A < 90 and v.Collision[A+10] != 2:
					image(v.ContB, x*50, y*50)
					v.Bas = True
				if A!=0 and A!=10 and A!=20 and A!=30 and A!=40 and A!=50 and A!=60 and A!=70 and A!=80 and A!=90 and v.Collision[A-1] != 2:
					image(v.ContG, x*50, y*50)
					v.Gauche = True
				if A!=9 and A!=19 and A!=29 and A!=39 and A!=49 and A!=59 and A!=69 and A!=79 and A!=89 and A!=99 and v.Collision[A+1] != 2:
					image(v.ContD, x*50, y*50)
					v.Droite = True

				#Coins/angles lave
				if v.Haut == True and v.Droite == True:
					image(v.ContHD, x*50, y*50)
				if v.Haut == True and v.Gauche == True:
					image(v.ContHG, x*50, y*50)
				if v.Bas == True and v.Droite == True:
					image(v.ContBD, x*50, y*50)
				if v.Bas == True and v.Gauche == True:
					image(v.ContBG, x*50, y*50)

				#Remise a 0 de la détection des tiles autours du blocs de lave
				v.Bas = False
				v.Haut = False
				v.Droite = False
				v.Gauche = False

			if v.Collision[A] == 3: #Lave
				image(v.Lave, x*50, y*50) #rebors lave
				if A > 10 and v.Collision[A-10] != 3:
					image(v.ContH, x*50, y*50)
					v.Haut = True
				if A < 90 and v.Collision[A+10] != 3:
					image(v.ContB, x*50, y*50)
					v.Bas = True
				if A!=0 and A!=10 and A!=20 and A!=30 and A!=40 and A!=50 and A!=60 and A!=70 and A!=80 and A!=90 and v.Collision[A-1] != 3:
					image(v.ContG, x*50, y*50)
					v.Gauche = True
				if A!=9 and A!=19 and A!=29 and A!=39 and A!=49 and A!=59 and A!=69 and A!=79 and A!=89 and A!=99 and v.Collision[A+1] != 3:
					image(v.ContD, x*50, y*50)
					v.Droite = True

				#Coins/angles lave
				if v.Haut == True and v.Droite == True:
					image(v.ContHD, x*50, y*50)
				if v.Haut == True and v.Gauche == True:
					image(v.ContHG, x*50, y*50)
				if v.Bas == True and v.Droite == True:
					image(v.ContBD, x*50, y*50)
				if v.Bas == True and v.Gauche == True:
					image(v.ContBG,x*50, y*50)

				#Remise a 0 de la détection des tiles autours du blocs de lave
				v.Bas = False
				v.Haut = False
				v.Droite = False
				v.Gauche = False

			#Foret/arbre en bas pour recouvrir les tank
			if (v.Collision[A] ==4):
				image(v.arbre, x*50, y*50) #Couleur Foret

	#Affiche les terrains proposées en barre d'info
	v.ColorMaster = fill(45, 139, 97)
	rect(20, 505, 50, 50)
	image(v.Montagne, 100, 505)
	image(v.Eau, 180, 505)
	image(v.Lave, 260, 505)
	image(v.arbre, 340, 505)

	#Affichage selection dans la barre d'info lors du choix de la texture
	if v.Selectile != 0:
		image(v.STile, v.Selectile*80-60, 505)
	#Affichage curseur sur la map pour le changement des textures
	if v.Selectile == 0:
		image(v.STile, v.XCursorEdit*50, v.YCursorEdit*50)