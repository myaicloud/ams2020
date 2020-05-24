import numpy as np
import matplotlib.pyplot as plt

def takeSecond(elem):
    return elem[1]

def main():
    print('I am assignment 2.')

    # 2. a)
    coords = np.genfromtxt('assignment02/coordinates.csv', delimiter=',', names=True, dtype=int)
    x_list = []
    y_list = []
    dist_dict = {}
    dist_list = []
    for (id, x, y) in coords:
        x_list.append(x)
        y_list.append(y)

    # 2. b)
    dists = np.genfromtxt('assignment02/distances.csv', delimiter=',', names=True, dtype=float)
    for (id, dist) in dists:
        dist_dict[id] = (dist, dist**2 * 64)
        dist_list.append(dist**2 * 64)

    # 2. d) walks through every map position
    map_dist = []
    for x in range(64):
        for y in range(64):
            a = np.array((x, y))
            for (id, map_x, map_y) in coords:
                if(map_x == x and map_y == y):
                    continue # wall positions dist=0

                # 2. e) compute distances to each wall point
                b = np.array((map_x, map_y))
                dist = np.linalg.norm(a - b)
                (d, d2) = dist_dict[id]
                # 2. f) estimate the residuals
                map_dist.append(((x,y), abs(dist - d), dist))

    map_dist.sort(key=takeSecond)
    for i in range(0, 10):
        # top10 nearest matching points to meatured and calculated distances
        print(map_dist[i])

    # 2. g) evaluate every position in the map according to its associated probabilities
    # TODO missing

    # 2. f) find the most probable drone position
    """ debug output
    python3.6 assignment02
    I am assignment 2.
    ((16, 8), 9.781210901138593e-05)
    ((28, 32), 9.781210901138593e-05)
    ((30, 34), 9.781210901138593e-05)
    ((54, 46), 9.781210901138593e-05)
    ((42, 43), 0.000174092775999668)
    ((63, 22), 0.000174092775999668)
    ((16, 58), 0.0002948858150979561)
    ((32, 42), 0.0002948858150979561)
    ((42, 42), 0.0002948858150979561)
    ((58, 58), 0.0002948858150979561)
    """

    # 2. c) Visualize coordinates/map
    plt.axis([0, 63, 0, 63])
    plt.plot(x_list, y_list, 'ro')
    plt.gca().invert_yaxis()
    plt.ylabel('y')
    plt.xlabel('x')

    data = {'x': np.array(x_list),
            'y': np.array(y_list),
            'd': np.array(dist_list)} # measured distances
    print(data)
    plt.scatter('x', 'y', s='d', data=data)
    plt.show()

if __name__ == '__main__':
    main()
