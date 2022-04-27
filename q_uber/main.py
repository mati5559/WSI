import argparse
import board
import random
import drivers

# Configure parser and get parsed arguments
def getArguments():
    parser = argparse.ArgumentParser(description='Finding best route from start to end with O-Learning algorithm - \"Q-Uber\"')

    parser.add_argument('N', type=int, help='Board size')

    parser.add_argument('--start', nargs=2, type=int, help='Coordinates of start position')
    parser.add_argument('--end', nargs=2, type=int, help='Coordinates of end position')

    parser.add_argument('--seed', type=int, help='Seed for random generator')

    rqGroup = parser.add_mutually_exclusive_group(required=True)
    rqGroup.add_argument('--random', action="store_true", help='Use random driver')
    rqGroup.add_argument('--quber', action="store_true", help='Use driver, that uses Q-learning algorithm')

    parser.add_argument('--print', action="store_true", help='Print board with example run in console')

    parser.add_argument('--epoch', type=int, default=500, help="Number of epochs for QUber (default 500)")
    parser.add_argument('--beta', type=float, default=1, help="Beta parameter for QUber (default 1)")
    parser.add_argument('--df', type=float, default=1, help="Discount factor for QUber (default 1)")


    parser.add_argument('--test', type=int, metavar="X", help='Test driver X times')

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
    driver = None
    if(args.random):
        driver = drivers.RandomDriver(brd)
    else:
        driver = drivers.QUber(brd)
        driver.train(args.beta, args.df, args.epoch)

    brd = driver.start()
    driver.clearBoard()

    if(args.print):
        brd.print()

    if args.test is not None:
        successes = 0
        for _ in range(args.test):
            result = driver.start()
            driver.clearBoard()
            if(result.status == "win"):
                successes += 1
        print("Driver reached goal in " + str(successes) + " per " + str(args.test) + " times.")
        

if __name__ == "__main__":
    main()