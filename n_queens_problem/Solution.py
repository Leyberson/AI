import random as rd

from Board import Board

class Solution:
	def __init__(self, dimension = 40):
		self.dimension = dimension
		self.solution = [i for i in range(0, self.dimension)]
		rd.shuffle(self.solution)
		self.score = Board(dimension = self.dimension).score(self.solution)

	def __str__(self):
		return str(self.solution)