from board import *
from game import *
from constants import *
import numpy as np
import random

x = Constants.tic
o = Constants.tac 
_ = Constants.empty

game = Game()
game.add_player(AI_Player(x))
game.add_player(AI_Player(o))




for i in range(2):
	while (game.end_game() == False):
		game.starting_player()
		game.switch_players()
		game.process_player()
		#board.print()
		
	w = game.winner()
	if w == o:
		print('o wins')
	elif w == x:
		print('x wins')
	else:
		print("it's a tie")

	game.reset()
	
