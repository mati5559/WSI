import argparse
import board
import random

# Configure parser and get parsed arguments
def getArguments():
    parser = argparse.ArgumentParser(description='Q-Uber')

    parser.add_argument('N', type=int, help='Board size')

    parser.add_argument('--start', nargs=2, type=int, help='Coordinates of start position')
    parser.add_argument('--end', nargs=2, type=int, help='Coordinates of end position')

    parser.add_argument('--seed', type=int, help='Seed for random generator')

    parser.add_argument('--print', action="store_true", help='Print board in console')

    return parser.parse_args()

def main():
    args = getArguments()

    if args.seed is not None:
        random.seed(args.seed)
    else:
        seed = int(random.uniform(0, 100000))
        random.seed(seed)
        print("Seed:", seed)

    brd = board.Board(args.N, args.start, args.end)

    if(args.print):
        brd.print()


if __name__ == "__main__":
    main()