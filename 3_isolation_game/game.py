from board import Board
from players import Player

class Game:
    def __init__(self, board:Board, player1:Player, player2:Player):
        self.player1 = player1
        self.player2 = player2
        self.player1.changePlayerNumber("1")
        self.player2.changePlayerNumber("2")
        self.board = board

    def start(self):
        self.board.print()
        while True:
            winner = self.board.getWinner("1")
            if(winner is not None): 
                if(winner == "draw"):
                    print("It's a draw!")
                    return winner
                print("Player " + winner + " is the winner!")
                return winner

            if(self.board.makeMove("1", self.player1.getMove(self.board)) == False):
                raise ValueError("Player tried to make illegal move!")
            
            self.board.print()

            winner = self.board.getWinner("2")
            if(winner is not None): 
                if(winner == "draw"):
                    print("It's a draw!")
                    return winner
                print("Player " + winner + " is the winner!")
                return winner

            if(self.board.makeMove("2", self.player2.getMove(self.board)) == False):
                raise ValueError("Player tried to make illegal move!")

            self.board.print()
            


