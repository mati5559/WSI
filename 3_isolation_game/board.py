def moveToCoordinate(move):
    x = move[1]
    y = ord(move[0])-65
    return (int(x), int(y))

class Board:
    def __init__(self, width, height, player1Position, player2Position):
        if((width<1) | (height<1) | ((width*height)<2) | (player1Position == player2Position)):
            raise ValueError("Board.__init__")
        
        self.fields = []

        # " " = field not visited
        # "#" = field visited
        # "1"/"2" = players position
        for _ in range(0, height):
            line = []
            for _ in range(0, width):
                line.append(" ")
            self.fields.append(line)
        
        self.fields[player1Position[1]][player1Position[0]] = "1"
        self.fields[player2Position[1]][player2Position[0]] = "2"

        self.player1Position = player1Position
        self.player2Position = player2Position


    def getPossibleMoves(self, playerNumber):
        neighbourFields = []
        possibleMoves = []
        playerPosition = self.player1Position if(str(playerNumber)=="1") else self.player2Position
        
        for x in range(playerPosition[0]-1, playerPosition[0]+2):
            if((x>=0) & (x<len(self.fields[0]))):
                for y in range(playerPosition[1]-1, playerPosition[1]+2):
                    if((y>=0) & (y<len(self.fields))):
                        neighbourFields.append((x, y))
        
        # Include only unvisited, free fields
        for index, coords in enumerate(neighbourFields):
            if(self.fields[coords[1]][coords[0]] == " "):
                possibleMoves.append(chr(65+coords[1]) + str(coords[0]))

        return possibleMoves
    
    # Game over when player have no legal moves
    def isTerminated(self, player):
        possibleMoves = self.getPossibleMoves(player)
        return (len(possibleMoves) == 0)
    
    def makeMove(self, player, move):
        possibleMoves = self.getPossibleMoves(player)
        playerPosition = self.player1Position if player == "1" else self.player2Position
        
        if move not in possibleMoves:
            return False

        coordinates = moveToCoordinate(move)
        self.fields[coordinates[1]][coordinates[0]] = player
        self.fields[playerPosition[1]][playerPosition[0]] = "#"
        
        if player == "1":
            self.player1Position = coordinates
        else:
            self.player2Position = coordinates

        return True

    def print(self):
        print("# - visited fields")
        print("1 - player 1 position")
        print("2 - player 2 position\n")

        lineLength = len(self.fields[0])
        
        # header
        print("   ", end="")
        for i in range(0, lineLength):
            print(str(i) + " ", end="")
        print("")

        # "\033[4m" and "\033[0m" are special characters for underlining text in console
        print("  \033[4m " + ("  " * lineLength) + "\033[0m")

        # fields
        for index, line in enumerate(self.fields):
            print(str(chr(65 + index)) + " \033[4m|", end="")
            for field in line:
                print(field + "|", end="")
            print("\033[0m")
