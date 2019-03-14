import pygame
import settings as v
from ProcToPy import *
v.init()

#Si une touche est appuyé, faire ce qui est demandé en fonction du menu affiché
# https://www.pygame.org/docs/ref/key.html

def keyPressed(keyCode):
	# if keyCode == pygame.K_UP:
	# 	print('space')
	v.keyCode = keyCode
	# print(k)
	
	if v.toshow == "Menu": #Si le jeu est sur le menu principal
		if keyCode == pygame.K_UP and v.Menu == 2:
			v.Menu = 1
		if keyCode == pygame.K_UP and v.Menu == 4:
			v.Menu = 3
		if keyCode == pygame.K_DOWN and v.Menu == 1:
			v.Menu = 2
		if keyCode == pygame.K_DOWN and v.Menu == 3:
			v.Menu = 4
		if keyCode == pygame.K_RIGHT and v.Menu == 1:
			v.Menu = 3
		if keyCode == pygame.K_RIGHT and v.Menu == 2:
			v.Menu = 4
		if keyCode == pygame.K_LEFT and v.Menu == 3:
			v.Menu = 1
		if keyCode == pygame.K_LEFT and v.Menu == 4:
			v.Menu = 2
		if v.Menu == 1 and keyCode == pygame.K_RETURN: #Lancer le menu de choix de jeu
			v.toshow = "MenuPlay"
			v.Menu = 0
		if v.Menu == 2 and keyCode == pygame.K_RETURN:
			v.toshow = "MenuEditor" #Lancer l'éditeur
		if v.Menu == 3 and keyCode  == pygame.K_RETURN: 
			v.toshow = "Options" #Lancer le menu d'option
		if v.Menu == 4 and keyCode == pygame.K_RETURN:
			v.toshow = "Credits"


	if v.toshow == "MenuPlay": #Si le jeu est sur la sélection de type de jeu
		if keyCode == pygame.K_DOWN:
			v.Menu += 1
		if keyCode == pygame.K_UP:
			v.Menu -= 1
		if keyCode == pygame.K_TAB:
			v.toshow = "Menu" #Touche retour, pour revenir sur le menu principal
		if v.Menu == 1 and keyCode == pygame.K_RETURN:
			v.toshow = "MenuMaps" #Lancer le jeu
			v.IA = False
		if v.Menu == 2 and keyCode == pygame.K_RETURN:
			v.toshow = "MenuMaps"
			v.IA = True

		if v.Menu == 3 and keyCode == pygame.K_RETURN:
			v.toshow = "ServerCreate" #Afficher la page de création de serveur
		if v.Menu == 4 and keyCode == pygame.K_RETURN:
			v.toshow = "ServerJoin" #Afficher la page pour rejoindre le serveur


	# if toshow == "ServerJoin": #récupérer l'entré des touches pour taper l'adresse ip du serveur à rejoindre
	# 	if (keyCode == BACKSPACE and ServerIP.length() > 0) ServerIP = ServerIP.substring(0, ServerIP.length()-1)
	# 	else if (keyCode == TAB) toshow = "MenuPlay"
	# 	else if (keyCode == ENTER and ServerIP.length() > 7) CanJoin = true
	# 	else if (key != CODED and keyCode != ENTER and keyCode != BACKSPACE) ServerIP += key

	if v.toshow == "MenuEditor" and keyCode == pygame.K_TAB:
		v.toshow = "MenuMaps"
		v.InteracMap = 1

	if v.toshow == "MenuMaps" and keyCode == pygame.K_RSHIFT or keyCode == pygame.K_LSHIFT:
		v.toshow = "Menu"
		v.InteracMap = 0

	if v.toshow == "Options":
		if keyCode == pygame.K_TAB and v.MenuOpt == 0 and v.Link == 0:
			v.toshow = "Reset"
		if keyCode == pygame.K_TAB and v.MenuOpt == 0 and v.Link == 1:
			v.toshow = "Game"
		if keyCode == pygame.K_RIGHT and v.MenuOpt == 0:
			v.MenuOpt = v.SMenuOpt
		if keyCode == pygame.K_TAB and v.MenuOpt > 0:
			v.MenuOpt = 0

	if v.toshow == "Game":
		if keyCode == pygame.K_RSHIFT or keyCode == pygame.K_LSHIFT:
			v.toshow = "Options"
			v.Link = 1

	if v.Winner != 0 and keyCode == pygame.K_SPACE:
		v.toshow = "Reset"


	if v.toshow == "Credits" and keyCode == pygame.K_TAB:
		v.toshow = "Menu"