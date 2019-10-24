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

    
    def choose_path(self, weight_matrix = np.zeros([2, 2]), default_weight=10):
        if(weight_matrix.shape == (2,2)):
            weight_matrix=np.zeros([self.dimension, self.dimension])
        weight_matrix = weight_matrix + default_weight
        if (self.visited_nodes != []):
            weight_matrix[:,self.visited_nodes[0]] = 0
            self.neighbors = [i for i in range(0,self.dimension)]
        while(len(self.visited_nodes) < self.dimension ):
            self.visited_nodes.append(rd.choices(self.neighbors, weights=weight_matrix[self.visited_nodes[-1]])[0])
            weight_matrix[:,self.visited_nodes[-1]] = 0