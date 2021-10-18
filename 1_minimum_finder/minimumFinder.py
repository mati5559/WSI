import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np
import matplotlib.patches as mpatches
from mpl_toolkits.mplot3d import *
import argparse


# Booth's function
def f(x, y):
    return 5*x*x +8*x*y -34*x +5*y*y -38*y +74


def gradF(x, y):
    return [10*x +8*y -34, 8*x +10*y -38]


def invHessGradF(x, y):
    grad = gradF(x, y)
    return [(15/18)*grad[0] - (2/9)*grad[1], (15/18)*grad[1] - (2/9)*grad[0]]


# Finding function's minimum methods
# and drawing all iterations on plot
def gradientDescent(startPoint, axes, b, maxIterations):
    currentPoint = startPoint
    axes.scatter(currentPoint[0], currentPoint[1], f(currentPoint[0], currentPoint[1]),
                 marker='o', c='red', label='Gradient descent method')


    for iteration in range(0, maxIterations):
        d = gradF(currentPoint[0], currentPoint[1])
        currentPoint = [-b * d[0] + currentPoint[0], -b * d[1] + currentPoint[1]]
        axes.scatter(currentPoint[0], currentPoint[1], f(currentPoint[0], currentPoint[1]),
                     marker='o', c='red')


def newtonMethod(startPoint, axes, b, maxIterations):
    currentPoint = startPoint
    axes.scatter(currentPoint[0], currentPoint[1], f(currentPoint[0], currentPoint[1]),
                 marker='o', c='green', label='Newton method')

    for iteration in range(0, maxIterations):
        d = invHessGradF(currentPoint[0], currentPoint[1])
        currentPoint = [-b * d[0] + currentPoint[0], -b * d[1] + currentPoint[1]]
        axes.scatter(currentPoint[0], currentPoint[1], f(currentPoint[0], currentPoint[1]),
                     marker='o', c='green')


def preparePlot():
    # Creating plot
    figure, axes = plt.subplots(subplot_kw={"projection": "3d"})

    # Load function to pyplot
    X = np.arange(-6, 6, 0.25)
    Y = np.arange(-6, 6, 0.25)
    X, Y = np.meshgrid(X, Y)
    Z = f(X, Y)

    # Configure axes
    axes.set_zlim(-10, 1000)
    axes.zaxis.set_major_locator(LinearLocator(10))
    axes.set_ylabel("Y")
    axes.set_xlabel("X")
    axes.set_zlabel("Z")

    # Plot the surface
    surface = axes.plot_surface(X, Y, Z, cmap='terrain', linewidths=0, antialiased=True, alpha=0.8, zorder=10)
    
    figure.colorbar(surface, shrink=0.5, aspect=5)

    return axes


def getArguments():
    parser = argparse.ArgumentParser(description='Show plot of Booth\'s function and working of Newton method and gradient descent method.')
    parser.add_argument('X', metavar='X', type=float, help='X coordinate of starting point')
    parser.add_argument('Y', metavar='Y', type=float, help='Y coordinate of starting point')
    parser.add_argument('B', metavar='B', type=float, help='B parameter for algorithm')
    parser.add_argument('iter', metavar='iter', type=int, help='Number of iterations')

    parser.add_argument('--nm', metavar='n', action='store_const', const=True, 
                        help='Show Newton method')
    parser.add_argument('--gdm', metavar='gdm', action='store_const', const=True, 
                        help='Show gradient descent method')

    return parser.parse_args()

if __name__ == "__main__":
    axes = preparePlot()
    args = getArguments()

    if args.gdm:
        gradientDescent([args.X, args.Y], axes, args.B, args.iter)

    if args.nm:
        newtonMethod([args.X, args.Y], axes, args.B, args.iter)
        

    # Show plot    
    plt.legend()
    plt.show()
