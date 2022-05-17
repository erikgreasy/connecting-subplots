from inc.Graph import Graph
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])


def load_file(path):
    g = Graph()
    with open(path) as f:
        for i, line in enumerate(f):
            line = line.split(' ')
            p1 = list(map(int, line[0][1:-1].split(',')))
            p2 = list(map(int, line[1][1:-1].split(',')))
            g.addEdge(Point(x= p1[0],y= p1[1]), Point(x= p2[0],y= p2[1]))
    return g