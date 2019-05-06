import pygame

def init():
	global Player, Act, xbase, ybase, xbase2, ybase2, DefaultVie, vietank1, vietank2, Direction, Direction2, CP, turn, arrows, choix, choix2, choix3, xbasem, ybasem, CB, MLock
	global lock, lock2, lock3, TestCadriD, TD2, Bas, Haut, Droite, Gauche, end, toshow, Menu, bord, DegatsLaveTank, ChangementSaison, Changementok, Winner, Selectile
	global Selectedtile, LockTile, XCursorEdit, YCursorEdit, InteracMap, SelectMap, MenuOpt, SMenuOpt, MusicVOL, SoundVOL, TSel, TypeDeSon, Design, SummerDay, WinterDay
	global DefaultMin, DefaultSec, Link, TimerSec, TimerMin, Tdiff, Tstart, ComptTimer, FrameRate, DecompteMusique, Collision
	global fontName, fontSize, font, screen, Music
	global BackMenu, BackOpt, Credits, arbre, Montagne, Eau, Lave, ContH, ContB, ContG, ContD, ContHD, ContHG, ContBD, ContBG
	global arbreW, MontagneW, EauW, LaveW, ContHW, ContBW, ContGW, ContDW, ContHDW, ContHGW, ContBDW, ContBGW, STile
	global STank1, STank2, Tank1, Tank1u, Tank1d, Tank1r, Tank1l, Tank2, Tank2u, Tank2d, Tank2r, Tank2l, Vies, BalleU, BalleD, BalleR, BalleL, BalleExplosion
	global IA, inDev, MaxDepl, max, needed, diffX, diffY, DeplNeed, Traj
	global ServerPort, ServerIP, NbPlayers, WhoIAm, IsMulti, tour, ThisClient, Winner, DistFeu1, DistFeu2, IsFire1, IsFire2, state
	global width, height, ColorMaster, TextAlignMaster
	global _y, Player1IG, Player2IG, EndRoll2, InfoSend, ActRemind

	screen = pygame.display.set_mode((500, 550)) # Définir la taille de l'écran

	width = 0
	height = 0

	ColorMaster = (255, 255, 255, 0)
	TextAlignMaster = "LEFT"

	BackgMenu = pygame.image.load("data/BackMenu.png").convert()
	BackOpt = pygame.image.load("data/Options.png").convert()
	Credits = pygame.image.load("data/Crédits.png").convert()

	arbre = pygame.image.load("data/arbre.png").convert_alpha()
	Montagne = pygame.image.load("data/Montagne.png").convert_alpha()
	Eau = pygame.image.load("data/Eau.png").convert_alpha()
	Lave = pygame.image.load("data/Lave.png").convert_alpha()
	ContH = pygame.image.load("data/Lavehaut.png").convert_alpha()
	ContB = pygame.image.load("data/Lavebas.png").convert_alpha()
	ContG = pygame.image.load("data/Lavegauche.png").convert_alpha()
	ContD = pygame.image.load("data/Lavedroite.png").convert_alpha()
	ContHD = pygame.image.load("data/Lavehaut+droite.png").convert_alpha()
	ContHG = pygame.image.load("data/Lavehaut+gauche.png").convert_alpha()
	ContBD = pygame.image.load("data/Lavebas+droite.png").convert_alpha()
	ContBG = pygame.image.load("data/Lavebas+gauche.png").convert_alpha()

	arbreW = pygame.image.load("data/arbreW.png").convert_alpha()
	MontagneW = pygame.image.load("data/MontagneW.png").convert_alpha()
	EauW = pygame.image.load("data/EauW.png").convert_alpha()
	LaveW = pygame.image.load("data/LaveW.png").convert_alpha()
	ContHW = pygame.image.load("data/LavehautW.png").convert_alpha()
	ContBW = pygame.image.load("data/LavebasW.png").convert_alpha()
	ContGW = pygame.image.load("data/LavegaucheW.png").convert_alpha()
	ContDW = pygame.image.load("data/LavedroiteW.png").convert_alpha()
	ContHDW = pygame.image.load("data/Lavehaut+droiteW.png").convert_alpha()
	ContHGW = pygame.image.load("data/Lavehaut+gaucheW.png").convert_alpha()
	ContBDW = pygame.image.load("data/Lavebas+droiteW.png").convert_alpha()
	ContBGW = pygame.image.load("data/Lavebas+gaucheW.png").convert_alpha()

	STile = pygame.image.load("data/Selection Tank2.png").convert_alpha()

	STank1 = pygame.image.load("data/Selection Tank1.png").convert_alpha()
	STank2 = pygame.image.load("data/Selection Tank2.png").convert_alpha()
	Tank1 = pygame.image.load("data/Tank1u.png").convert_alpha()
	Tank1u = pygame.image.load("data/Tank1u.png").convert_alpha()
	Tank1d = pygame.image.load("data/Tank1d.png").convert_alpha()
	Tank1r = pygame.image.load("data/Tank1r.png").convert_alpha()
	Tank1l = pygame.image.load("data/Tank1l.png").convert_alpha()
	Tank2 = pygame.image.load("data/Tank2d.png").convert_alpha()
	Tank2u = pygame.image.load("data/Tank2u.png").convert_alpha()
	Tank2d = pygame.image.load("data/Tank2d.png").convert_alpha()
	Tank2r = pygame.image.load("data/Tank2r.png").convert_alpha()
	Tank2l = pygame.image.load("data/Tank2l.png").convert_alpha()
	Vies = pygame.image.load("data/Vies.png").convert_alpha()
	BalleU = pygame.image.load("data/BalleU.png").convert_alpha()
	BalleD = pygame.image.load("data/BalleD.png").convert_alpha()
	BalleR = pygame.image.load("data/BalleR.png").convert_alpha()
	BalleL = pygame.image.load("data/BalleL.png").convert_alpha()
	BalleExplosion = pygame.image.load("data/Explosion.png").convert_alpha()

	fontName = "MS Reference Sans Serif"
	fontSize = 24
	font = 0

	Music = False

	Player = 1 #Joueur 1 et 2 changement
	Act = 3
	Player1IG = False
	Player2IG = False
	xbase = 0 #Emplacement tank 1 (0, 0)
	ybase = 0
	xbase2 = 450 #Emplacement tank 2 (450, 450)
	ybase2 = 450
	DefaultVie = 5 #Vie des tanks par défaut
	vietank1 = DefaultVie #Vie des tanks
	vietank2 = DefaultVie
	Direction = 2 #Direction des sprites des tanks
	Direction2 = 1
	CP = 0 #Compteur Placement
	turn = 0 #Un décompte de random éffectué
	arrows = 0 #Empèche le joueur de maintenir les flèches pour se déplacer ( un appui = un déplacement )
	choix = 0 #Validation Choix
	choix2 = 0 #Choix entre Attaque ou Déplacement
	choix3 = 0 #Anti Enter*2 ( effet d'un key pressed pour enter car non ascii)
	xbasem = -100 # Emplacement balle
	ybasem = -100
	CB = 0 #Compteur Balle
	MLock = 0
	lock = 0 #touche de tire vérouillée
	lock2 = 0 #direction du tir
	lock3 = 0 #Anti Enter*2 ( effet d'un key pressed pour enter car non ascii)
	TestCadriD = 0 #Test cadrillage renvoie 0 ou 1 => Si on peux passer ou pas
	TD2 = 0 
	Bas = False #Variable détectant si plusieurs bord existes pour un angle (texture)
	Haut = False
	Droite = False
	Gauche = False
	end = False
	toshow = "Menu"
	Menu = 1
	bord = False
	DegatsLaveTank = False
	ChangementSaison = 0
	Changementok = False 

	Winner = 0

	# Parties valeurs MenuEditeur
	Selectile = 0
	Selectedtile = 0
	LockTile = 0
	XCursorEdit = 0
	YCursorEdit = 0

	InteracMap = 0 #Interac(tion)Map permet de définir s'il s'agit d'une lecture (0) ou d'une écriture de map
	SelectMap = 1 #Annonce quelle map est sélectione

	#Menu option
	MenuOpt = 0
	SMenuOpt = 1
	MusicVOL = 50
	SoundVOL = 50
	TSel = 1
	TypeDeSon = 1
	Design = 1
	SummerDay = 1 
	WinterDay = 1 
	Link = 0 #Permet d'accéder au parametres de son en jeu
	DefaultMin = 5
	DefaultSec = 0
	TimerSec = DefaultSec
	TimerMin = DefaultMin
	Tdiff = 0
	Tstart = 0
	ComptTimer = 1

	#MusicBackground
	FrameRate = 60
	DecompteMusique = 19 * 60 + 1

	#Variables Multijoueur
	ServerPort = "1042"
	ServerIP = "localhost"

	ThisClient = ''
	tour = 1
	EndRoll2 = False
	InfoSend = False
	WhoIAm = 0
	ActRemind = 3
	NbPlayers = 0
	IsMulti = False

	state = 'offline'

	Winner = 0
	DistFeu1 = 0
	DistFeu2 = 0
	IsFire1 = False
	IsFire2 = False

	#Maps de base lorsqu'on édite une map dans le menu editeur
	#Collision = [
	#  0, 2, 2, 4, 4, 0, 0, 1, 1, 3, 
	#  0, 2, 2, 2, 4, 4, 0, 0, 0, 3, 
	#  0, 1, 2, 2, 0, 0, 0, 3, 0, 0, 
	#  0, 1, 2, 2, 2, 0, 0, 0, 1, 1, 
	#  0, 0, 2, 2, 2, 2, 0, 0, 0, 1, 
	#  1, 0, 0, 0, 2, 2, 2, 2, 0, 0, 
	#  1, 1, 0, 0, 0, 2, 2, 2, 1, 0, 
	#  0, 0, 3, 0, 0, 0, 2, 2, 1, 0, 
	#  3, 0, 0, 0, 4, 4, 2, 2, 2, 0, 
	#  3, 1, 1, 0, 0, 4, 4, 2, 2, 0
	#]
	Collision = [
	  0, 1, 2, 3, 4, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 0, 0
	]

	IA = False
	inDev = True
	MaxDepl = 0
	max = 0
	needed = 1
	diffX = 0
	diffY = 0
	DeplNeed = 0
	Traj = {
		0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
		0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
		0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
		0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
		0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
		0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
		0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
		0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
		0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
		0, 0, 0, 0, 0, 0, 0, 0, 0, 0}