import random as rd

from Board import Board

class Solution:
	def __init__(self, dimension = 40):
		self.dimension = dimension
		self.board = Board(dimension=self.dimension)
		self.solution = [i for i in range(0, self.dimension)]
		rd.shuffle(self.solution)
		self.score = self.board.score(self.solution)

	def get_child(self):
		position1 = rd.randint(0, self.dimension-1)
		position2 = rd.randint(0, self.dimension-1)
		aux = self.solution[position1]
		self.solution[position1] = self.solution[position2]
		self.solution[position2] = aux
		self.score = self.board.score(self.solution)
		return self

	def copy(self):
		new_solution = Solution(dimension = self.dimension)
		new_solution.solution = self.solution.copy()
		new_solution.score = self.score
		return new_solution


	def accepted(self, my_list):
		return self.board.score(self.solution)>self.board.score(self.my_list)

	def __str__(self):
		return str(self.solution)