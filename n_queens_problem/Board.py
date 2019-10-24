from Ant import Ant

class Board:
    def __init__(self, dimension=40):
        self.dimension = dimension
        self.vertex = []
        self.edge = []

    def score(self,  my_list):
        score = 0
        for element in my_list:
            iterator = my_list.index(element) + 1
            right = element + 1
            left = element - 1
            while (right<self.dimension and iterator < self.dimension):
                if(right == my_list[iterator]):
                    score += 1
                right += 1
                iterator += 1
            iterator = my_list.index(element) + 1
            while(left>0 and iterator < self.dimension):
                if(left == my_list[iterator]):
                    score += 1
                left -= 1
                iterator += 1
        return score

# a = Ant(10)
# a.choose_path()
# print(Board().score(a.visited_nodes))
# print(Board().score([i for i in range(0,40)]))