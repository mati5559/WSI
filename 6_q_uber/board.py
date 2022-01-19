import random
import copy

class Board:
    def __init__(self, n, start=None, end=None):
        self.fields = [[" " for _ in range(0, n+2)] for _ in range(0, n+2)] 

        if start is None:
            start = [int(random.uniform(1, n)), int(random.uniform(1, n))]
        if end is None:
            end = [int(random.uniform(1, n)), int(random.uniform(1, n))]

        # Expand board to add borders
        start[0] += 1
        start[1] += 1
        end[0] += 1
        end[1] += 1

        self.randomize(start, end)

        while(not self.check(start)):
            self.randomize(start, end)

        self.playerPosition = start
        self.status = "running"

    def randomize(self, start, end):
        for row in self.fields:
            # Left and right borders
            row[0] = "\u2588"
            row[-1] = "\u2588"
            # Random space
            for i in range(1, len(row)-1):
                row[i] = random.choice([" ", " ", " ", " ", "\u2588", "\u2588"]) # Generate more free space than obstacles

        # Top and bottom borders
        self.fields[0] = ["\u2588" for _ in range(0, len(self.fields[0]))]
        self.fields[-1] = ["\u2588" for _ in range(0, len(self.fields[-1]))]

        # Start and end
        self.fields[start[1]][start[0]] = "S"
        self.fields[end[1]][end[0]] = "E"

    def check(self, startPosittion) -> bool:
        # Check if there is any possible route between start and end
        fieldsCopy = copy.deepcopy(self.fields)

        # DFS algorithm
        def visitField(field):
            fieldsCopy[field[1]][field[0]] = "X"

            neighbours = [
                [field[0], field[1]+1],
                [field[0], field[1]-1],
                [field[0]+1, field[1]],
                [field[0]-1, field[1]]
            ]

            for neighbour in neighbours:
                if(fieldsCopy[neighbour[1]][neighbour[0]] == "E"):
                    return True
                elif(fieldsCopy[neighbour[1]][neighbour[0]] == " "):
                    result = visitField(neighbour)
                    if(result):
                        return True
            return False

        return visitField(startPosittion)

    def print(self):
        print("\u2588 - obstacles")
        print("  - free fields")
        print("X - visited fields")
        print("P - player position")
        print("S - start")
        print("E - end")
        
        print("")

        for rowIndex in range(1, len(self.fields)+1):
            for field in self.fields[-rowIndex]:
                print(field, end="")
            print("")

    # Returns False when player hit obstacle
    def move(self, direction) -> bool:
        if(self.fields[self.playerPosition[1]][self.playerPosition[0]] not in ["S", "E"]):
            self.fields[self.playerPosition[1]][self.playerPosition[0]] = "X"

        if(direction == 0): # left
            self.playerPosition[0] -= 1
        if(direction == 1): # up
            self.playerPosition[1] += 1
        if(direction == 2): # right
            self.playerPosition[0] += 1
        if(direction == 3): # down
            self.playerPosition[1] -= 1
        
        
       
        if(self.fields[self.playerPosition[1]][self.playerPosition[0]] != "\u2588"):
            if(self.fields[self.playerPosition[1]][self.playerPosition[0]] == "E"):
                self.status = "win"
            self.fields[self.playerPosition[1]][self.playerPosition[0]] = "P"
            
            return True
        else:
            self.status = "lost"
            return False
