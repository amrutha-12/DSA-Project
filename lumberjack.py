from operator import itemgetter
from os import curdir
import time
import heapq

class Tree:
    def __init__(self, x : int, y : int, height : int, thickness : int, unit_weight : int, unit_value : int):
        self.x = x
        self.y = y
        self.height = height
        self.thickness = thickness
        self.uweight = unit_weight
        self.uvalue = unit_value
        self.isTreeCut = False

    def cutTree(self):
        self.isTreeCut = True

    def value(self) -> int:
        return self.uvalue*self.height*self.thickness
    
    def weight(self) -> int:
        return self.uweight*self.height*self.thickness

    def isTreeCut(self) -> bool:
        return self.isTreeCut

    def time(self, x : int, y : int) -> int:
        return abs(self.x - x) + abs(self.y - y) + self.thickness
    
    def printTree(self):
        print("X:", self.x, "Y:", self.y, "Height:", self.height, "Weight", self.weight(), "Value", self.value())

class Node(object):
    def __init__(self, tree: Tree, direction: str, value: int, score: float):
        self.tree = tree
        self.direction = direction
        self.value = value
        self.score = score

    def __repr__(self):
        return f'Node value: {self.score}'

    def __gt__(self, other):
        return self.score > other.score

class GridPoint:
    def __init__(self, x : int, y : int):
        self.x = x
        self.y = y
        self.tree = None

    def coordinate(self):
        return self.x, self.y

class Actions:
    moves = {1 : "cut left", 2: "cut up", 3: "cut right", 4: "cut down"}
    steps = {1: "move left",2: "move up",3: "move right",4: "move down"}

class Grid:
    def __init__(self, n : int, t : int, k : int):
        self.grid = []
        self.grid_size = n
        self.time = t
        self.num_of_trees = k
        self.trees = None
        self.curx = 0
        self.cury = 0
        for i in range(n):
            row = []
            for j in range(n):
                grid_point = GridPoint(i,j)
                row.append(grid_point)
            self.grid.append(row)
    
    def initialise_grid(self, input : list):
        assert len(input) == self.num_of_trees
        self.trees = input
        for tree in input:
            self.grid[tree.x][tree.y].tree = tree

    def score(self, value : int, time : int) -> int:
        x = value/time
        points = x + 2/x
        return x

    def getScore(self) -> list:
        scores = []
        for tree in self.trees:
            if not tree.isTreeCut:
                for direction in Actions.moves.keys():
                    score = [tree]
                    if direction == 1:
                        point = 0
                        score.append(Actions.moves[direction])
                        tree_queue = [tree]
                        while tree_queue:
                            current_tree = tree_queue.pop(0)
                            point += current_tree.value()
                            # print("Current Tree", Actions.moves[direction])
                            # current_tree.printTree()
                            for i in range(current_tree.x, max(0,current_tree.x - current_tree.height), -1):
                                potential_tree = self.grid[i][current_tree.y].tree
                                if potential_tree != None:
                                    if not potential_tree.isTreeCut and current_tree != potential_tree:
                                        # print("Potential Tree")
                                        # potential_tree.printTree()
                                        if potential_tree.weight() < current_tree.weight():
                                            tree_queue.append(potential_tree)
                                        break
                        score.append(point)
                        scores.append(score)
                    elif direction == 2:
                        point = 0
                        score.append(Actions.moves[direction])
                        tree_queue = [tree]
                        while tree_queue:
                            current_tree = tree_queue.pop(0)
                            point += current_tree.value()
                            # print("Current Tree", Actions.moves[direction])
                            # current_tree.printTree()
                            for i in range(current_tree.y, min(current_tree.y + current_tree.height, n)):
                                potential_tree = self.grid[current_tree.x][i].tree
                                if potential_tree != None:
                                    if not potential_tree.isTreeCut and current_tree != potential_tree:
                                        # print("Potential Tree")
                                        # potential_tree.printTree()
                                        if potential_tree.weight() < current_tree.weight():
                                            tree_queue.append(potential_tree)
                                        break
                        score.append(point)
                        scores.append(score)
                    elif direction == 3:
                        point = 0
                        score.append(Actions.moves[direction])
                        tree_queue = [tree]
                        while tree_queue:
                            current_tree = tree_queue.pop(0)
                            point += current_tree.value()
                            # print("Current Tree", Actions.moves[direction])
                            # current_tree.printTree()
                            for i in range(current_tree.y, min(current_tree.x + current_tree.height, n)):
                                potential_tree = self.grid[i][current_tree.y].tree
                                if potential_tree != None:
                                    if not potential_tree.isTreeCut and current_tree != potential_tree:
                                        # print("Potential Tree")
                                        # potential_tree.printTree()
                                        if potential_tree.weight() < current_tree.weight():
                                            tree_queue.append(potential_tree)
                                        break
                        score.append(point)
                        scores.append(score)
                    elif direction == 4:
                        point = 0
                        score.append(Actions.moves[direction])
                        tree_queue = [tree]
                        while tree_queue:
                            current_tree = tree_queue.pop(0)
                            point += current_tree.value()
                            # print("Current Tree", Actions.moves[direction])
                            # current_tree.printTree()
                            for i in range(current_tree.y, max(current_tree.y - current_tree.height, 0), -1):
                                potential_tree = self.grid[current_tree.x][i].tree
                                if potential_tree != None:
                                    if not potential_tree.isTreeCut and current_tree != potential_tree:
                                        # print("Potential Tree")
                                        # potential_tree.printTree()
                                        if potential_tree.weight() < current_tree.weight():
                                            tree_queue.append(potential_tree)
                                        break
                        score.append(point)
                        scores.append(score)
        return scores

    
    def findMax(self, scores : list) -> list:
        heap = []
        for score in scores:
            score.append(self.score(score[2], score[0].time(self.curx, self.cury)))
            obj = Node(score[0], score[1], score[2], -score[3])
            heap.append(obj)
        heapq.heapify(heap)
        # scores = sorted(scores, key=itemgetter(3), reverse=True)
        return heap
        

    def moveToTree(self, scores : list):
        # for i in scores:
        #     print("x:", i[0].x, "y:", i[0].y, i[1], i[2], i[3])
        flag = False
        while scores:
            potential = heapq.heappop(scores)
            if potential.tree.time(self.curx, self.cury) < self.time:
                self.updateTime(potential.tree.time(self.curx, self.cury))
                if self.curx > potential.tree.x:
                    while self.curx > potential.tree.x:
                        print(Actions.steps[1])
                        self.curx -= 1
                elif self.curx < potential.tree.x:
                    while self.curx < potential.tree.x:
                        print(Actions.steps[3])
                        self.curx += 1
                if self.cury > potential.tree.y:
                    while self.cury > potential.tree.y:
                        print(Actions.steps[4])
                        self.cury -= 1
                elif self.cury < potential.tree.y:
                    while self.cury < potential.tree.y:
                        print(Actions.steps[2])
                        self.cury += 1
                # print(self.curx, self.cury)
                self.cutTree(potential.tree, potential.direction)
                flag = True
                break
        return flag
    
    def cutTree(self, tree : Tree, direction : str):
        print(direction)
        if direction == Actions.moves[1]:
            tree_queue = [tree]
            while tree_queue:
                current_tree = tree_queue.pop(0)
                self.grid[current_tree.x][current_tree.y].tree = None
                current_tree.cutTree()
                # print("Current Tree", Actions.moves[direction])
                # current_tree.printTree()
                for i in range(current_tree.x, max(0,current_tree.x - current_tree.height), -1):
                    potential_tree = self.grid[i][current_tree.y].tree
                    if potential_tree != None:
                        if not potential_tree.isTreeCut and current_tree != potential_tree:
                            # print("Potential Tree")
                            # potential_tree.printTree()
                            if potential_tree.weight() < current_tree.weight():
                                tree_queue.append(potential_tree)
                            break
        if direction == Actions.moves[2]:
            tree_queue = [tree]
            while tree_queue:
                current_tree = tree_queue.pop(0)
                self.grid[current_tree.x][current_tree.y].tree = None
                current_tree.cutTree()
                # print("Current Tree", Actions.moves[direction])
                # current_tree.printTree()
                for i in range(current_tree.y, min(current_tree.y + current_tree.height, n)):
                    # print(self.grid[current_tree.x][i])
                    potential_tree = self.grid[current_tree.x][i].tree
                    if potential_tree != None:
                        if not potential_tree.isTreeCut and current_tree != potential_tree:
                            # print("Potential Tree")
                            # potential_tree.printTree()
                            if potential_tree.weight() < current_tree.weight():
                                tree_queue.append(potential_tree)
                            break
        if direction == Actions.moves[3]:
            tree_queue = [tree]
            while tree_queue:
                current_tree = tree_queue.pop(0)
                self.grid[current_tree.x][current_tree.y].tree = None
                current_tree.cutTree()
                # print("Current Tree", Actions.moves[direction])
                # current_tree.printTree()
                for i in range(current_tree.y, min(current_tree.x + current_tree.height, n)):
                    potential_tree = self.grid[i][current_tree.y].tree
                    if potential_tree != None:
                        if not potential_tree.isTreeCut and current_tree != potential_tree:
                            # print("Potential Tree")
                            # potential_tree.printTree()
                            if potential_tree.weight() < current_tree.weight():
                                tree_queue.append(potential_tree)
                            break
        if direction == Actions.moves[4]:
            tree_queue = [tree]
            while tree_queue:
                current_tree = tree_queue.pop(0)
                self.grid[current_tree.x][current_tree.y].tree = None
                current_tree.cutTree()
                # print("Current Tree", Actions.moves[direction])
                # current_tree.printTree()
                for i in range(current_tree.y, max(current_tree.y - current_tree.height, 0), -1):
                    potential_tree = self.grid[current_tree.x][i].tree
                    if potential_tree != None:
                        if not potential_tree.isTreeCut and current_tree != potential_tree:
                            # print("Potential Tree")
                            # potential_tree.printTree()
                            if potential_tree.weight() < current_tree.weight():
                                tree_queue.append(potential_tree)
                            break

    def solve(self):
        flag = True
        while flag:
            flag = self.moveToTree(self.findMax(self.getScore()))

    def printGrid(self):
        for j in range(self.grid_size-1, -1, -1):
            for i in range(self.grid_size):
                if self.grid[i][j].tree != None:
                    print("1 ", end="")
                else:
                    print("0 ", end="")
            print("\n", end="")
    
    def updateTime(self, time : int):
        self.time -= time

    def printTrees(self):
        for tree in self.trees:
            print("X:", tree.x, "Y:", tree.y, "Height:", tree.height, "Weight", tree.weight(), "Value:", tree.value(), "Time:", tree.time(self.curx, self.cury))

if __name__ == "__main__":
    t, n, k = map(int, input().split())
    grid = Grid(n, t, k)
    trees = []
    for i in range(k):
        x, y, h, d, c, p = map(int, input().split())
        assert x < n
        assert y < n
        tree = Tree(x, y, h, d, c, p)
        trees.append(tree)
    grid.initialise_grid(trees)
    # grid.printGrid()
    # grid.printTrees()
    grid.solve()
    # start_time = time.time()
    # flag = True
    # difference = 0
    # while flag and difference < 50:
    #     flag = grid.moveToTree(grid.findMax(grid.getScore()))
    #     current_time = time.time()
    #     difference = current_time - start_time
    # grid.printGrid()