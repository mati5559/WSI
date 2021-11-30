from board import Board
from game import Game
from players import HumanPlayer, RandomPlayer, MinimaxPlayer
import argparse

# Configure parser and get parsed arguments
def getArguments():
    parser = argparse.ArgumentParser(description='Simple isolation game')

    parser.add_argument('height', type=int, help='Height of the board')
    parser.add_argument('width', type=int, help='Width of the board')

    parser.add_argument('player1', metavar="PLAYER1", type=str, choices=["human", "random", "minimax"], help='Player 1 type. You can choose from: "human", "random", "minimax"')
    parser.add_argument('player2', metavar="PLAYER2", type=str, choices=["human", "random", "minimax"], help='Player 2 type. You can choose from: "human", "random", "minimax"')

    parser.add_argument('X1', type=int, help='X coordinate of player 1 start position')
    parser.add_argument('Y1', type=int, help='Y coordinate of player 1 start position')
    parser.add_argument('X2', type=int, help='X coordinate of player 2 start position')
    parser.add_argument('Y2', type=int, help='Y coordinate of player 2 start position')


    parser.add_argument('--depth1', type=int, default=10, help="Maximum depth of game tree for player 1. Used with minimax algorithm. Default: 10")
    parser.add_argument('--depth2', type=int, default=15, help="Maximum depth of game tree for player 2. Used with minimax algorithm. Default: 15")

    return parser.parse_args()

def main():
    arguments = getArguments()
    board = Board(arguments.width, arguments.height, (arguments.X1, arguments.Y1), (arguments.X2, arguments.Y2))
    
    firstPlayer = None
    secondPlayer = None

    if(arguments.player1 == "human"): firstPlayer = HumanPlayer()
    elif(arguments.player1 == "random"): firstPlayer = RandomPlayer()
    elif(arguments.player1 == "minimax"): firstPlayer = MinimaxPlayer(arguments.depth1)

    if(arguments.player2 == "human"): secondPlayer = HumanPlayer()
    elif(arguments.player2 == "random"): secondPlayer = RandomPlayer()
    elif(arguments.player2 == "minimax"): secondPlayer = MinimaxPlayer(arguments.depth2)
    
    game = Game(board, firstPlayer, secondPlayer)
    game.start()


if __name__ == "__main__":
    main()