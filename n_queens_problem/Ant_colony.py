from Ant import Ant
from Board import Board

from os import system
import numpy as np

class Ant_colony:
    def __init__(self, dimension=40):
        self.dimension = dimension

        self.weight_matrix = np.zeros([self.dimension, self.dimension])
        self.myBoard = Board(dimension = self.dimension)
        count = 0
        ants = [Ant(10, start_position = i, dimension=self.dimension) for i in range(0,dimension)]
        while(count < 20000):
            del(ants)
            ants = [Ant(10, start_position = i, dimension=self.dimension) for i in range(0,dimension)]
            score_information = []
            for ant in ants:
                ant.choose_path(weight_matrix=self.weight_matrix.copy())
                score = self.myBoard.score(ant.visited_nodes)
                score_information.append(score)
            if 0 in score_information:
                break
            for score in score_information:
                self.myBoard.weight_update(ant.visited_nodes, self.weight_matrix, score)
            count += 1
            system("clear")
            print(min(score_information))

        minimo = min(score_information)

        index = score_information.index(minimo)

        print(ants[index].visited_nodes)
        print(minimo)

        # print(self.weight_matrix)

        # ants = [Ant(10, start_position = i, dimension=self.dimension) for i in range(0,dimension)]
        # for ant in ants:
        #     ant.choose_path(weight_matrix=self.weight_matrix.copy())
        #     print(ant.visited_nodes)
        # del(ants)