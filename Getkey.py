import pygame
from ProcToPy import *

#Si une touche est appuyé, faire ce qui est demandé en fonction du menu affiché
# https://www.pygame.org/docs/ref/key.html

def keyPressed():
	from Game import toshow, keyCode, Menu, InteracMap

	keyCode = pygame.key.get_pressed()
	if toshow == "Menu": #Si le jeu est sur le menu principal
		if keyCode[K_UP] and Menu == 2:
			Menu = 1
		if keyCode[K_UP] and Menu == 4:
			Menu = 3
		if keyCode[K_DOWN] and Menu == 1:
			Menu = 2
		if keyCode[K_DOWN] and Menu == 3:
			Menu = 4
		if keyCode[K_RIGHT] and Menu == 1:
			Menu = 3
		if keyCode[K_RIGHT] and Menu == 2:
			Menu = 4
		if keyCode[K_LEFT] and Menu == 3:
			Menu = 1
		if keyCode[K_LEFT] and Menu == 4:
			Menu = 2
		if Menu == 1 and keyCode[K_RETURN]: #Lancer le menu de choix de jeu
			toshow = "MenuPlay"
			Menu = 0
		if Menu == 2 and keyCode[K_RETURN]:
			toshow = "MenuEditor" #Lancer l'éditeur
		if Menu == 3 and keyCode [K_RETURN]: 
			toshow = "Options" #Lancer le menu d'option
		if Menu == 4 and keyCode[K_RETURN]:
			toshow = "Credits"


	if toshow == "MenuPlay": #Si le jeu est sur la sélection de type de jeu
		if keyCode[K_DOWN]:
			Menu += 1
		if keyCode[K_UP]:
			Menu -= 1
		if keyCode[K_TAB]:
			toshow = "Menu" #Touche retour, pour revenir sur le menu principal
		if Menu == 1 and keyCode[K_RETURN]:
			toshow = "MenuMaps" #Lancer le jeu
			IA = False
		if Menu == 2 and keyCode[K_RETURN]:
			toshow = "MenuMaps"
			IA = True

		if Menu == 3 and keyCode[K_RETURN]:
			toshow = "ServerCreate" #Afficher la page de création de serveur
		if Menu == 4 and keyCode[K_RETURN]:
			toshow = "ServerJoin" #Afficher la page pour rejoindre le serveur


	# if toshow == "ServerJoin": #récupérer l'entré des touches pour taper l'adresse ip du serveur à rejoindre
	# 	if (keyCode == BACKSPACE and ServerIP.length() > 0) ServerIP = ServerIP.substring(0, ServerIP.length()-1)
	# 	else if (keyCode == TAB) toshow = "MenuPlay"
	# 	else if (keyCode == ENTER and ServerIP.length() > 7) CanJoin = true
	# 	else if (key != CODED and keyCode != ENTER and keyCode != BACKSPACE) ServerIP += key

	if toshow == "MenuEditor" and keyCode[K_TAB]:
		toshow = "MenuMaps"
		InteracMap = 1

	if toshow == "MenuMaps" and keyCode[K_RSHIFT] or keyCode[K_LSHIFT]:
		toshow = "Menu"
		InteracMap = 0

	if toshow == "Options":
		if keyCode[K_TAB] and MenuOpt == 0 and Link == 0:
			Game.Reset()
		if keyCode[K_TAB] and MenuOpt == 0 and Link == 1:
			toshow = "Game"
		if keyCode[K_RIGHT] and MenuOpt == 0:
			MenuOpt = SMenuOpt
		if keyCode[K_RIGHT] and MenuOpt > 0:
			MenuOpt = 0

	if toshow == "Game":
		if keyCode[K_RSHIFT] or keyCode[K_LSHIFT]:
			toshow = "Options"
			Link = 1

	if Winner != 0 and keyCode[K_SPACE]:
		Game.Reset()


	if toshow == "Credits" and keyCode[K_TAB]:
		toshow = "Menu"