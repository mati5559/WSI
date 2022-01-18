import random
import copy

class Board:
    def __init__(self, n, start=None, end=None):
        self.fields = [[" " for _ in range(0, n+2)] for _ in range(0, n+2)]

        if start is None:
            start = [int(random.uniform(1, n)), int(random.uniform(1, n))]
        if end is None:
            end = [int(random.uniform(1, n)), int(random.uniform(1, n))]

        self.randomize(start, end)

        while(not self.check(start)):
            self.randomize(start, end)


    def randomize(self, start, end):
        for row in self.fields:
            row[0] = "\u2588"
            row[-1] = "\u2588"
            for i in range(1, len(row)-1):
                row[i] = random.choice([" ", " ", " ", " ", "\u2588", "\u2588"]) # Generate more free space than obstacles

        self.fields[0] = ["\u2588" for _ in range(0, len(self.fields[0]))]
        self.fields[-1] = ["\u2588" for _ in range(0, len(self.fields[-1]))]

        self.fields[start[1]+1][start[0]+1] = "S"
        self.fields[end[1]+1][end[0]+1] = "E"

    def check(self, startPosittion) -> bool:
        # Check if there is any possible route between start and end
        fieldsCopy = copy.deepcopy(self.fields)

        def visitField(field):
            fieldsCopy[field[1]+1][field[0]+1] = "X"

            neighbours = [
                [field[0], field[1]+1],
                [field[0], field[1]-1],
                [field[0]+1, field[1]],
                [field[0]-1, field[1]]
            ]

            for neighbour in neighbours:
                if(fieldsCopy[neighbour[1]+1][neighbour[0]+1] == "E"):
                    return True
                elif(fieldsCopy[neighbour[1]+1][neighbour[0]+1] == " "):
                    result = visitField(neighbour)
                    if(result):
                        return True
            return False

        return visitField(startPosittion)

    def print(self):
        print("\u2588 - obstacles")
        print("  - free fields")
        print("S - start")
        print("E - end")
        print("")

        for rowIndex in range(1, len(self.fields)+1):
            for field in self.fields[-rowIndex]:
                print(field, end="")
            print("")
