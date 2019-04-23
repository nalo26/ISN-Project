from __future__ import print_function

import pygame
import settings as v
from ProcToPy import *

import sys
from time import sleep
from sys import stdin, exit
from PodSixNet.Connection import connection, ConnectionListener
from _thread import *

v.init()

class Client(ConnectionListener): #Echnange de données pour le multijoueur
	def __init__(self, host, port):
		textAlign('LEFT')
		self.Connect((host, port)) #Connection au serveur
		connection.Send({"action": "nickname", "nickname": "useless"})

	def Loop(self): #Envoie de toutes les données au serveur
		connection.Pump()
		self.Pump()
		# envoyer toutes les informations au serveur
		if v.WhoIAm == 1:
			connection.Send({"action": "dataPlayer", "dataPlayer": {"vie": str(v.vietank1), "x": str(v.xbase), "y": str(v.ybase), "IsFire": str(v.IsFire1), "Dir": str(v.Direction), "PlayerIG": str(v.Player1IG)}})
			connection.Send({"action": "dataServer", "dataServer": {"player": str(v.Player), "winner": str(v.Winner), "season": str(v.Design), "state": str(v.state), "act": str(v.Act), "min": str(v.TimerMin), "sec": str(v.TimerSec), "map": v.Collision}}) #todo : map
			if v.IsFire1 == True:
				# v.IsFire1 = False
				connection.Send({"action": "PosBalle", "PosBalle": {"x": str(v.xbasem), "y": str(v.ybasem)}})
		if v.WhoIAm == 2:
			connection.Send({"action": "dataPlayer", "dataPlayer": {"vie": str(v.vietank2), "x": str(v.xbase2), "y": str(v.ybase2), "IsFire": str(v.IsFire2), "Dir": str(v.Direction2), "PlayerIG": str(v.Player2IG)}})
			if v.EndRoll2 == True:
				v.EndRoll2 = False
				v.InfoSend = True
				connection.Send({"action": "Roll2Ended", "Roll2Ended": str(v.InfoSend)})
				v.InfoSend = False
			if v.IsFire2 == True:
				# v.IsFire2 = False
				connection.Send({"action": "PosBalle", "PosBalle": {"x": str(v.xbasem), "y": str(v.ybasem)}})


	def Network_players(self, data): #Récupération du nombre de joueurs en ligne + définition de notre "nom" (1 ou 2)
		# print("*** players: "+", ".join([p for p in data['players']]))
		v.NbPlayers = len(data['players'])
		if v.WhoIAm == 0:
			v.WhoIAm = int(len(data['players']))
			connection.Send({"action": "nickname", "nickname": str(v.WhoIAm)})

	def Network_message(self, data): #Message (non implanté dans le jeu, mais il est quand même la au cas où)
		print(data['who'] + ": " + data['message'])

	def Network_dataPlayer(self, data): #Récupérer les informations envoyées sur les joueurs
		if v.WhoIAm == 1 and int(data['who']) == 2:
			v.vietank2 = int(data['dataPlayer']['vie'])
			v.xbase2 = int(data['dataPlayer']['x'])
			v.ybase2 = int(data['dataPlayer']['y'])
			v.IsFire2 = bool(data['dataPlayer']['IsFire'])
			# v.DistFeu2 = int(data['dataPlayer']['DistFire'])
			v.Direction2 = int(data['dataPlayer']['Dir'])
			v.Player2IG = bool(data['dataPlayer']['PlayerIG'])

		if v.WhoIAm == 2 and int(data['who']) == 1:
			v.vietank1 = int(data['dataPlayer']['vie'])
			v.xbase = int(data['dataPlayer']['x'])
			v.ybase = int(data['dataPlayer']['y'])
			v.IsFire1 = bool(data['dataPlayer']['IsFire'])
			# v.DistFeu1 = int(data['dataPlayer']['DistFire'])
			v.Direction = int(data['dataPlayer']['Dir'])
			v.Player1IG = bool(data['dataPlayer']['PlayerIG'])

	def Network_dataServer(self, data): #Récupérer les informations envoyées sur la partie
		if v.WhoIAm == 2:
			v.Player = int(data['dataServer']['player'])
			v.Winner = int(data['dataServer']['winner'])
			v.Design = int(data['dataServer']['season'])
			v.Act = int(data['dataServer']['act'])
			v.state = str(data['dataServer']['state'])
			v.TimerMin = int(data['dataServer']['min'])
			v.TimerSec = int(data['dataServer']['sec'])
			v.Collision = data['dataServer']['map']

	def Network_PosBalle(self, data):
		if v.WhoIAm != int(data['who']):
			v.xbasem = int(data['PosBalle']['x'])
			v.ybasem = int(data['PosBalle']['y'])

	def Network_Roll2Ended(self, data): #Récupérer le fin de tour du joueur 2
		if v.WhoIAm == 1:
			v.InfoSend = bool(data['Roll2Ended'])

	def Network_connected(self, data):
		print("You are now connected to the server")

	def Network_error(self, data): #En cas d'erreur réseau
		print('error:'+str(data['error'][1]))
		v.toshow = 'Reset'
		connection.Close()

	def Network_disconnected(self, data):
		print('Server disconnected')
		v.toshow = 'Reset'
		# exit()

def ServerJoin():
	background(0)
	v.IsMulti = True
	v.state = 'picking'
	v.toshow = "Multiplayer"
	host = '78.218.72.47'
	port = '1042'
	v.ThisClient = Client(host, int(port)) #Connection au serveur (fixe)

def Multiplayer():
	v.ThisClient.Loop() #Récupérer les informations du serveur
	sleep(0.001)
	if v.WhoIAm == 1 and v.state == 'picking': #Si je suis le joueur 1, choisir une map
		v.toshow = 'MenuMaps' 
	if v.NbPlayers != 2: #S'il manque de joueur
		background(0)
		textAlign('CENTER')
		text("En attente d'un autre joueur...", 250, 250)
	if v.WhoIAm == 2 and v.state == 'picking': #Si le joueur choisit une map
		background(0)
		textAlign('CENTER')
		text("L'host choisit une map...", 250, 250)
	if v.state == 'ingame': #Sinon, afficher le jeu
		v.toshow = 'Game'