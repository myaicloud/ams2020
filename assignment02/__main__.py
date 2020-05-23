import numpy as np
import matplotlib.pyplot

def main():
    print('I am assignment 2.')

    # 2. a)
    coords = np.genfromtxt('assignment02/coordinates.csv', delimiter=',', names=True, usecols=('x', 'y'), dtype=int)
    print(coords)
    # 2. b)
    dists = np.genfromtxt('assignment02/distances.csv', delimiter=',', names=True, usecols=('distance'), dtype=float)

    # 2. c) Visualize coordinates
    #matplotlib.pyplot.imshow(coords)

    # 2. d) walks through every map position
    #matplotlib.pyplot.imshow(dists)

    # 2. e) compute distances
    
    # 2. f) estimate the residuals

    # 2. g) evaluate every position in the map according to its associated probabilities

    # 2. f) find the most probable drone position
if __name__ == '__main__':
    main()
