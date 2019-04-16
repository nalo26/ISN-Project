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

class Client(ConnectionListener):
	def __init__(self, host, port):
		textAlign('LEFT')
		self.Connect((host, port))
		print("Chat client started")
		print("TAB to exit")
		connection.Send({"action": "nickname", "nickname": "useless"})

	def Loop(self):
		connection.Pump()
		self.Pump()
		# envoyer toutes les informations au serveur
		if v.WhoIAm == 1:
			connection.Send({"action": "dataPlayer", "dataPlayer": {"vie": str(v.vietank1), "x": str(v.xbase), "y": str(v.ybase), "IsFire": str(v.IsFire1), "DistFire": str(v.DistFeu1), "Dir": str(v.Direction)}})
			connection.Send({"action": "dataServer", "dataServer": {"player": str(v.Player), "winner": str(v.Winner), "season": str(v.Design), "act": str(v.Act), "state": str(v.state), "P1IG": str(v.Player1IG), "P2IG": str(v.Player2IG), "map": v.Collision}}) #todo : map
		if v.WhoIAm == 2:
			connection.Send({"action": "dataPlayer", "dataPlayer": {"vie": str(v.vietank2), "x": str(v.xbase2), "y": str(v.ybase2), "IsFire": str(v.IsFire2), "DistFire": str(v.DistFeu2), "Dir": str(v.Direction2)}})


	def Network_players(self, data):
		print("*** players: "+", ".join([p for p in data['players']]))
		v.NbPlayers = len(data['players'])
		if v.WhoIAm == 0:
			v.WhoIAm = int(len(data['players']))
			connection.Send({"action": "nickname", "nickname": str(v.WhoIAm)})

	def Network_message(self, data):
		print(data['who'] + ": " + data['message'])

	def Network_dataPlayer(self, data):
		# récupérer les informations envoyées sur les joueurs
		if v.WhoIAm == 1 and int(data['who']) == 2:
			v.vietank2 = int(data['dataPlayer']['vie'])
			v.xbase2 = int(data['dataPlayer']['x'])
			v.ybase2 = int(data['dataPlayer']['y'])
			v.IsFire2 = int(data['dataPlayer']['IsFire'])
			v.DistFeu2 = int(data['dataPlayer']['DistFire'])
			v.Direction2 = int(data['dataPlayer']['Dir'])
			# v.Player2IG = data['dataPlayer']['P2IG']

		if v.WhoIAm == 2 and int(data['who']) == 1:
			v.vietank1 = int(data['dataPlayer']['vie'])
			v.xbase = int(data['dataPlayer']['x'])
			v.ybase = int(data['dataPlayer']['y'])
			v.IsFire1 = int(data['dataPlayer']['IsFire'])
			v.DistFeu1 = int(data['dataPlayer']['DistFire'])
			v.Direction = int(data['dataPlayer']['Dir'])
			# v.Player1IG = data['dataPlayer']['P1IG']

	def Network_dataServer(self, data):
		# récupérer les informations envoyées sur la partie
		if v.WhoIAm == 2:
			v.Player = int(data['dataServer']['player'])
			v.Winner = int(data['dataServer']['winner'])
			v.Design = int(data['dataServer']['season'])
			v.Act = int(data['dataServer']['act'])
			v.state = str(data['dataServer']['state'])
			v.Player1IG = data['dataServer']['P1IG']
			v.Player2IG = data['dataServer']['P2IG']
			v.Collision = data['dataServer']['map']

	def Network_connected(self, data):
		print("You are now connected to the server")

	def Network_error(self, data):
		print('error:'+str(data['error'][1]))
		v.toshow = 'Menu'
		connection.Close()

	def Network_disconnected(self, data):
		print('Server disconnected')
		v.toshow = 'Menu'
		# exit()

def ServerJoin():
	background(0)
	v.IsMulti = True
	v.state = 'picking'
	v.toshow = "Multiplayer"
	host = 'localhost'
	port = '1042'
	v.ThisClient = Client(host, int(port))

def Multiplayer():
	v.ThisClient.Loop()
	sleep(0.001)
	if v.WhoIAm == 1 and v.state == 'picking':
		v.toshow = 'MenuMaps' 
	if v.WhoIAm == 1 and v.NbPlayers != 2:
		background(0)
		textAlign('CENTER')
		text("En attente d'un autre joueur...", 250, 250)
	if v.WhoIAm == 2 and v.state == 'picking':
		background(0)
		textAlign('CENTER')
		text("L'host choisit une map...", 250, 250)
	if v.state == 'ingame':
		v.toshow = 'Game'