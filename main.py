from time import perf_counter
from collections import namedtuple
from sys import maxsize

from inc.Graph2 import Graph2
from inc.read_file import load_file
from inc.find_nearest_neighbor import find_nearest_neighbor
from inc.build import build


def build_trees(cc):
    start = perf_counter()
    trees = [build(x, 0) for x in cc]
    print(f"Building trees time: {perf_counter()-start}s")

    return trees


def find_components(g):
    start = perf_counter()
    cc = g.connectedComponents()
    print(f"Components find time: {perf_counter()-start}s")

    return cc


def main():
    # load input data
    g = load_file(input("Enter input file name: "))

    # find components
    cc = find_components(g)
    len_cc = len(cc)
    print(f"Num of components: {len_cc}")

    # build trees
    trees = build_trees(cc)

    Line = namedtuple("Line", ["X", "Y", "distance"])
    arr = [[Line(None, None, maxsize) for i in range(len_cc)]
           for j in range(len_cc)]

    start = perf_counter()
    for i, group in enumerate(cc):
        print(f"\rCount distances between groups {i}/{len_cc}", end='')
        for j, tree in enumerate(trees[i+1:], start=i+1):
            p1 = None
            p2 = None
            v = maxsize
            for point in group:
                best = find_nearest_neighbor(tree=tree, point=point)
                if best.distance < v:
                    p1 = point
                    p2 = best.point
                    v = best.distance

            arr[i][j] = Line(p1, p2, v)
            #arr[j][i] = Line(p1, p2, v)

    print(
        f"\nDistance between groups time: {perf_counter()-start}s")

    start = perf_counter()
    print(f"Build final graph")
    s = 0
    g = Graph2(len_cc)
    with open('out.txt', 'w') as f:
        edges = 0
        while(edges != len_cc-1):
            point = arr[0][0]
            mi = 0
            mj = 0
            for i, line in enumerate(arr):
                for j, x in enumerate(line[i+1:], start=i+1):
                    if x[2] < point[2]:
                        point = x
                        mi, mj = i, j
            g.addEdge(mi, mj)
            if g.isCyclic():
                g.removeEdge(mi, mj)
            else:
                s += point[2]
                edges += 1
                f.write(
                    f"[{point[1].x},{point[1].y}] [{point[0].x},{point[0].y}] \n")
            arr[mi][mj] = arr[0][0]

    print(f"Sum of added edge: {s}")


if __name__ == '__main__':
    main()
