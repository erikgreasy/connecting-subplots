from operator import itemgetter
from collections import namedtuple

Node = namedtuple("Node", ["value", "left", "right"])

def build(points, depth):
    if len(points) == 0:
        return None
        
    points.sort(key=itemgetter(depth % 2))
    middle = len(points) // 2
    
    return Node(
        value = points[middle],
        left = build(
            points=points[:middle],
            depth=depth+1,
        ),
        right = build(
            points=points[middle+1:],
            depth=depth+1,
        ),
    )