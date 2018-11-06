from constants import *
import numpy as np
from math import factorial
import random


x = Constants.tic
o = Constants.tac 
_ = Constants.empty


class Board():


	def __init__(self, np_board = np.array([[_, _, _], [_, _, _], [_, _, _]])):
		self.board = np.copy(np_board)
		self.elems = { -1: 'o', 0: '_', 1: 'x'}
		self.rows = {'A':0, 'B':1, 'C':2, 0:'A', 1: 'B', 2:'C'}
		self.columns = {'1':0, '2':1, '3':2, 0: '1', 1: '2', 2: '3'}


	def insert(self, elem, pos):
		self.board[self.rows[pos[0]], self.columns[pos[1]]] = elem

	def get(self, row, column):
		return self.board[row][column]

	def numpy_representation(self):
		return np.copy(self.board)

	def print(self):
		print('')

		for i in range(len(self.board)):
			for j in range(len(self.board[i])):
				print(self.elems[self.board[i][j]] + ' ', end = '')
			print('')
		print('')


	def elem(self, pos):
			return self.board[self.rows[pos[0]], self.columns[pos[1]]]


	def coords(self, elem):

		ret = []
		for i in range(len(self.board)):
			for j in range(len(self.board[i])):
				if self.board[i][j] == elem:
					ret.append(self.rows[i] + self.columns[j])
					
		return ret

	def winner(self):

		axis_sum_left = self.board[0][0] + self.board[1][1] + self.board[2][2]
		axis_sum_right = self.board[0][2] + self.board[1][1] + self.board[2][0]

		if axis_sum_right == x + x + x or axis_sum_left == x + x + x:
			return x

		elif axis_sum_right == o + o + o or axis_sum_left == o + o + o:
			return o

		else:
			for i in range(3):
				rows_sum = self.board[i][0] + self.board[i][1] + self.board[i][2]
				columns_sum = self.board[0][i] + self.board[1][i] + self.board[2][i]
				
				if rows_sum == x + x + x or columns_sum == x + x + x:
					return x

				elif rows_sum == o + o + o or columns_sum == o + o + o:
					return o

			return _

	def full(self):
			return len(self.coords(_)) == 0

	def reset_board(self):
			self.board = np.array([[_, _, _], [_, _, _], [_, _, _]])
			
	

class AI_Player():

	def __init__(self, elem):
		#self.board = board
		self.elem = elem

	def get_next_position(self, board): # np.array(3x3)
		b = Board(board)
		empty_spaces = b.coords(_)
		best_coords = None 
		best_value = None

		if len(empty_spaces) > 0:
			for i in range(len(empty_spaces)):
				coords_value = self.__position_coords_value(board, empty_spaces[i], o)
				if best_coords == None:
					best_coords = empty_spaces[i]
					best_value = coords_value

				elif best_value < coords_value:
					best_value = coords_value
					best_coords = empty_spaces[i]

				
			print('AI Player move: ', best_coords)
			return best_coords

	def __position_value(self, board, row, column, player):
			
		new_board = np.array(board)
		new_board[row][column] = player

		table = Board()

		table.board = new_board
		winner = table.winner()

		count = len(table.coords(_))
		if winner == player:
			ret = factorial(count) * 2**count

		else:
			ret = 0

			if player == o:
				new_player = x

			else:
				new_player = o

			for i in range(len(new_board)):
				for j in range(len(new_board[i])):
					if new_board[i][j] == _:
						value = self.__position_value(new_board, i, j, new_player)
						
						ret = ret + value
			ret = -ret
		return ret

	def __position_coords_value(self, board, coords, player):
			
		temporary = Board()
		row = temporary.rows[coords[0]]
		column = temporary.columns[coords[1]]
		ret = self.__position_value(board, row, column, player)
		#print('row + column', coords, 'ret', ret)
		return ret
	

class Human_Player():

	def __init__(self, board, elem):
		self.board = board
		self.elem = elem

	def get_next_position(self):
		position_incorrect = True
		while position_incorrect:
			pos = input('Position:')
			if self.board.elem(pos) == _:
				position_incorrect = False
				return pos
			else:
				print('Incorrect position! Try again!')


