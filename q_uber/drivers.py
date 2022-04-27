from board import Board
import random
import copy
from abc import ABC, abstractmethod

class Driver(ABC):
    def __init__(self, brd:Board):
        self.board = copy.deepcopy(brd)
        self.emptyBoard = brd

    def clearBoard(self):
        self.board = copy.deepcopy(self.emptyBoard)

    @abstractmethod
    def start(self) -> Board:
        pass


class RandomDriver(Driver):
    def start(self) -> Board:
        while(self.board.move(random.choice([0, 1, 2, 3]))):
            if(self.board.status != "running"):
                break
        return self.board


class QUber(Driver):
    def __init__(self, brd:Board):
        super().__init__(brd)

        self.Q = [[[0 for _ in range(4)] for _ in range(len(brd.fields))] for _ in range(len(brd.fields))]
    

    # Run through board 
    # Modify politics only when gain and discountFactor is not None
    def start(self, gain=None, discountFactor=None) -> Board:
        while(True):
            position = copy.deepcopy(self.board.playerPosition)
            movesGrades = copy.deepcopy(self.Q[position[1]][position[0]])

            maxGrade = max(movesGrades)
            indexes = []
            for index, grade in enumerate(movesGrades):
                if(grade == maxGrade):
                    indexes.append(index)

            # Choose move randomly when there is more than 1 move with highest grade 
            move = random.choice(indexes) 
            self.board.move(move)

            if (gain is not None) and (discountFactor is not None):
                nextPosition = self.board.playerPosition
                nextMovesGrades = self.Q[nextPosition[1]][nextPosition[0]]
                
                reward = self._getReward()

                self.Q[position[1]][position[0]][move] = (movesGrades[move] + 
                gain * (reward + discountFactor * max(nextMovesGrades) + movesGrades[move]))

            if(self.board.status != "running"):
                break

        return self.board
        
    def _getReward(self) -> int:
        if(self.board.status == "lost"):
            return -1
        if(self.board.status == "win"):
            return 1

        return 0

    def train(self, gain, discountFactor, epoch):
        for _ in range(0, epoch):
            self.start(gain, discountFactor)
            self.board = copy.deepcopy(self.emptyBoard)

