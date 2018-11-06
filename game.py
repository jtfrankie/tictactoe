
from constants import *
import numpy as np
from math import factorial
import random
from board import *

class Game():

	def __init__(self):
		self.board = Board()
		self.players = []
		self.current_player = None

		
	def add_player(self, player):
		self.players.append(player)


	def process_player(self):
		board = self.board.numpy_representation()
		pos = self.current_player.get_next_position(board)
		self.board.insert(self.current_player.elem, pos)
		#self.insert(self.current_player.elem, self.rows[pos[0]], self.columns[pos[1]])


	def switch_players(self):
		if self.current_player == None:
			self.current_player = self.players[0]
		
		elif self.current_player == self.players[0]:
			self.current_player = self.players[1] 

		else:
			self.current_player = self.players[0]


	def starting_player(self):
		value = random.randint(0, 1)
		if self.current_player == None and value == 0:
			self.current_player = self.players[0]

		elif self.current_player == None and value == 1:
			self.current_player = self.players[1]


	def next_game(self):
			next_game = False
			statement = input('Do you wish to play again? Yes or No: ')
			if statement == 'Y' or statement == 'Yes':
				self.board = np.array([[_, _, _], [_, _, _], [_, _, _]])
				self.print()
				next_game = True
			return next_game

	def winner(self):
		return self.board.winner()

	def end_game(self):
		return self.board.winner() or self.board.full()

	def reset(self):
		return self.board.reset_board()
