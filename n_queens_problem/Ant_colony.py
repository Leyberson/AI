from Ant import Ant
from Board import Board

import numpy as np

class Ant_colony:
    def __init__(self, dimension=40):
        self.dimension = dimension

        ants = [Ant(10, start_position = i, dimension=self.dimension) for i in range(0,dimension)]
        for ant in ants:
            ant.choose_path()
            print(ant.visited_nodes)

        
