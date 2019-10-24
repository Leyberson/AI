import random as rd
import numpy as np

class Ant:
    def __init__(self, stock, start_position = None, dimension=40):
        self.dimension = dimension
        self.stock = stock
        self.neighbors = [i for i in range(0,self.dimension)]
        if start_position == None:
            self.visited_nodes = []
        else:
            self.visited_nodes = [start_position]
            del(self.neighbors[self.neighbors.index(start_position)])

    
    def choose_path(self, weight_matrix = None, default_weight=10):
        if (weight_matrix == None):
            rd.shuffle(self.neighbors)
            if self.visited_nodes != []:
                self.neighbors.insert(0,self.visited_nodes[0])
            self.visited_nodes = self.neighbors
        else:
            weight_matrix = weight_matrix + default_weight
            if (visited_nodes != []):
                weight_matrix