import pygame, json
import settings as v
from ProcToPy import *
v.init()

def MenuMaps():
	#Menu de sélection des maps

	# /!\ Don't touch my creation Mouhahahahaha /!\
	if v.InteracMap == 0:
		background(0)
		textAlign("CENTER")
		image(v.BackgMenu, 0, 0)
		textSize(20)
		text("Play with Map N°1", 250, 200)
		text("Play with Map N°2", 250, 300)
		text("Play with Map N°3", 250, 400)
		textSize(14)
		text("Press arrows to select your folder and press RIGHT to load file", 250, 515)
		textAlign("LEFT")

		CurseurMenuMaps()

		#Chargement des maps
		with open("data/Map1.json", 'r') as mf:
			Map1 = json.load(mf)
		with open("data/Map2.json", 'r') as mf:
			Map2 = json.load(mf)
		with open("data/Map1.json", 'r') as mf:
			Map2 = json.load(mf)

		#Remplace la map par défault par celle sélectionée
		if v.keyCode == pygame.K_RIGHT:
			for i in range(99):
				CollisionID = str(i)
				if v.SelectMap == 1:
					v.Collision[i] = Map1[CollisionID]
				if v.SelectMap == 2:
					v.Collision[i] = Map2[CollisionID]
				if v.SelectMap == 3:
					v.Collision[i] = Map3[CollisionID]
			v.toshow = "Game"

	if v.InteracMap == 1:
		background(0)
		textAlign("CENTER")
		image(v.BackgMenu, 0, 0)
		fill(101,149,99)
		textSize(20)
		text("Remplace Map N°1", 250, 200)
		text("Remplace Map N°2", 250, 300)
		text("Remplace Map N°3", 250, 400)
		textSize(13)
		text("Press arrows to select a backup location and press Enter to save file", 250, 515)
		textAlign("LEFT")

		CurseurMenuMaps()

		#Le joueur choisir d'enregistrer sa Map 
		if v.keyCode == pygame.K_RETURN:
			'''
			if v.SelectMap == 1:
				# Map1 = new JSONObject()
				pass
			if v.SelectMap == 2:
				# Map2 = new JSONObject()
				pass
			if v.SelectMap == 3:
				# Map3 = new JSONObject()
				pass
			'''

			for i in range(100):
				ColisionID = str(i)
				if v.SelectMap == 1:
					Map1[CollisionID] = v.Collision[i]
				if v.SelectMap == 2:
					Map2[CollisionID] = v.Collision[i]
				if v.SelectMap == 3:
					Map3[CollisionID] = v.Collision[i]

			if v.SelectMap == 1:
				with open("data/Map1.json", 'w') as mf:
					json.dump(Map1, mf)
			if v.SelectMap == 2:
				with open("data/Map2.json", 'w') as mf:
					json.dump(Map2, mf)
			if v.SelectMap == 3:
				with open("data/Map2.json", 'w') as mf:
					json.dump(Map3, mf)

			v.toshow = "Menu"
			v.InteracMap = 0

def CurseurMenuMaps():
	#Déplacement du curseur de choix
	if v.keyCode == pygame.K_DOWN and v.SelectMap < 3:
		v.SelectMap += 1
		delay(150)
	if v.keyCode == pygame.K_UP and v.SelectMap > 1:
		v.SelectMap -= 1
		delay(150)

	#Souligne le choix du joueur
	image(v.BalleR, 100, v.SelectMap*100+70)
	image(v.BalleL, 350, v.SelectMap*100+70)