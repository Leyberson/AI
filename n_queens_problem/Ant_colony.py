from Ant import Ant
from Board import Board

import numpy as np

class Ant_colony:
    def __init__(self, dimension=40):
        self.dimension = dimension

        self.weight_matrix = np.zeros([self.dimension, self.dimension])
        self.myBoard = Board(dimension = self.dimension)
        ants = [Ant(10, start_position = i, dimension=self.dimension) for i in range(0,dimension)]
        for ant in ants:
            ant.choose_path()
            print(ant.visited_nodes)
            score = self.myBoard.score(ant.visited_nodes)
            print(score)
        for ant in ants:
            score = self.myBoard.score(ant.visited_nodes)
            if score == 0:
                break
            self.myBoard.weight_update(ant.visited_nodes, self.weight_matrix, score)
        del(ants)

        print(self.weight_matrix)

        ants = [Ant(10, start_position = i, dimension=self.dimension) for i in range(0,dimension)]
        for ant in ants:
            ant.choose_path(weight_matrix=self.weight_matrix.copy())
            print(ant.visited_nodes)
        del(ants)