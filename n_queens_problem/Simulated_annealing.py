from Solution import Solution
from Board import Board

class Simulated_annealing:
	def __init__(self, dimension=40):
		self.dimension = dimension
		self.board = Board(dimension = self.dimension)
		self.solutions = [Solution(dimension = self.dimension) for i in range(0, self.dimension)]
		self.scores = [self.board.score(solve.solution) for solve in self.solutions]
		if 0 in self.scores:
			print(self.solutions[self.scores.index(0)])


algo = Simulated_annealing(dimension=4)