import random
import copy

from board import Board

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
        self.depth = depth

    def _heuristicGrade(self, board:Board):
        p1moves = len(board.getPossibleMoves("1"))
        p2moves = len(board.getPossibleMoves("2"))
        return (p1moves-p2moves)/8

    def _minimax(self, board, depth, actualPlayer):
        winner = board.getWinner(actualPlayer)
        if winner is not None:
            # Rating > 0 menas that player 1 is winning, 0 means draw
            # Rating < 0 means that player 2 is winning
            if(winner == "draw"):
                return (0, None)
            if(winner == "1"):
                return (1, None)
            if(winner == "2"):
                return (-1, None)
            
        if(depth == 0):
            return (self._heuristicGrade(board), None)
        
        possibleMoves = board.getPossibleMoves(actualPlayer)
        successors = [[copy.deepcopy(board), move] for move in possibleMoves]
        successorsRatings = []

        for s in successors:
            s[0].makeMove(actualPlayer, s[1])
            successorsRatings.append((self._minimax(s[0], depth-1, "1" if actualPlayer == "2" else "2")[0], s[1]))

        # Player 1 is "max player"
        if(actualPlayer == "1"):
            maxRating = -1
            maxRatingMoves = []
            for rating in successorsRatings:
                if(rating[0] == maxRating):
                    maxRatingMoves.append(rating)
                    continue
                if(rating[0] > maxRating):
                    maxRating = rating[0]
                    maxRatingMoves = [rating]
            return random.choice(maxRatingMoves)
        else:
            minRating = 1
            minRatingMoves = []
            for rating in successorsRatings:
                if(rating[0] == minRating):
                    minRatingMoves.append(rating)
                    continue
                if(rating[0] < minRating):
                    minRating = rating[0]
                    minRatingMoves = [rating]
            return random.choice(minRatingMoves)
                

    def getMove(self, board):
        rating, move = self._minimax(board, self.depth, self.playerNumber)
        return move