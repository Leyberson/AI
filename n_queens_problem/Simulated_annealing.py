from Solution import Solution
from Board import Board

class Simulated_annealing:
	def __init__(self, dimension=40):
		self.dimension = dimension
		self.board = Board(dimension = self.dimension)
		self.solutions = [Solution(dimension = self.dimension) for i in range(0, self.dimension)]
		self.scores = [self.board.score(solve.solution) for solve in self.solutions]
		while(True):
			if 0 in self.scores:
				break
			for i in range(0, len(self.solutions)):
				new_solution = self.solutions[i].copy()
				new_solution = new_solution.get_child()
				if new_solution.score < self.solutions[i].score:
					self.solutions[i] = new_solution
					self.scores[i] = new_solution.score
				elif self.board.accepted(self.solutions[i].score, new_solution.score):
					solutions.append(new_solution)
					scores.append(new_solution.score)

		print(self.solutions[self.scores.index(0)])
		# self.board.print_list(self.solutions[self.scores.index(0)])


algo = Simulated_annealing(dimension=40)