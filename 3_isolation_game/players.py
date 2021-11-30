import random

# All players must implement getMove(board) method 
class Player:
    def changePlayerNumber(self, playerNumber):
        self.playerNumber = playerNumber

class HumanPlayer(Player):
    def getMove(self, board):
        while True:
            print("Player " + self.playerNumber + ": Enter move code (example: A5, B3...):", end="")
            move = input()

            if move in board.getPossibleMoves(self.playerNumber):
                return move
            
            print("Invaild move, please try again.")

class RandomPlayer(Player):
    def getMove(self, board):
        possibleMoves = board.getPossibleMoves(self.playerNumber)
        return random.choice(possibleMoves)

class MinimaxPlayer(Player):
    def __init__(self, depth):
        pass # TODO

    def getMove(self, board):
        pass # TODO

        