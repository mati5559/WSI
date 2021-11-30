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
            if(self.board.isTerminated("1")): 
                print("Player 2 is the winner!")
                return "2"

            self.board.makeMove("1", self.player1.getMove(self.board))
            self.board.print()

            if(self.board.isTerminated("2")): 
                print("Player 1 is the winner!")
                return "1"

            self.board.makeMove("2", self.player2.getMove(self.board))
            self.board.print()
            


