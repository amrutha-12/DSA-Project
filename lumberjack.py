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
        return abs(self.x - x) + abs(self.y - y) + self.d

class GridPoint:
    def __init__(self, x : int, y : int):
        self.x = x
        self.y = y
        self.tree = None

    def coordinate(self):
        return self.x, self.y

class Actions:
    moves = {1 : "cut left", 2: "cut up", 3: "cut right", 4: "cut down"}

class Grid:
    def __init__(self, n : int, t : int, k : int):
        self.grid = []
        self.n = n
        self.t = t
        self.k = k
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
        assert len(input) == self.k
        self.trees = input
        for tree in input:
            self.grid[tree.x][tree.y].tree = tree

    def score(self, value : int, time : int) -> int:
        return value/time

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
                            for i in range(current_tree.x, max(0,current_tree.x - current_tree.height), -1):
                                potential_tree = self.grid[i][current_tree.y].tree
                                if potential_tree != None:
                                    if not potential_tree.isTreeCut:
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
                            for i in range(current_tree.y, min(current_tree.y + current_tree.height, n)):
                                potential_tree = self.grid[current_tree.x][i].tree
                                if potential_tree != None:
                                    if not potential_tree.isTreeCut:
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
                            for i in range(current_tree.y, min(current_tree.x + current_tree.height, n)):
                                potential_tree = self.grid[i][current_tree.y].tree
                                if potential_tree != None:
                                    if not potential_tree.isTreeCut:
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
                            for i in range(current_tree.y, max(current_tree.y - current_tree.height, 0), -1):
                                potential_tree = self.grid[current_tree.x][i].tree
                                if potential_tree != None:
                                    if not potential_tree.isTreeCut:
                                        if potential_tree.weight() < current_tree.weight():
                                            tree_queue.append(potential_tree)
                                        break
                        score.append(point)
                        scores.append(score)
        return scores

    
    def findMax(self):
        pass

    def cutTree(self):
        pass

    def printGrid(self):
        for j in range(self.n-1, -1, -1):
            for i in range(self.n):
                if self.grid[i][j].tree != None:
                    print("1 ", end="")
                else:
                    print("0 ", end="")
            print("\n", end="")
    
    def printTrees(self):
        for tree in self.trees:
            print("X:", tree.x, "Y:", tree.y, "Height:", tree.height, "Weight", tree.weight(), "Value", tree.value())

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
    grid.printGrid()
    grid.printTrees()
    for i in grid.getScore():
        print("x:", i[0].x, "y:", i[0].y, i[1], i[2])

