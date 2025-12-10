import math

spath = 'day9/sample.txt'
ipath = 'day9/input.txt'
path = ipath




def compress_points(points):
    # points: list of (x, y)

    xs = sorted(set(p[0] for p in points))
    ys = sorted(set(p[1] for p in points))

    # map original -> compressed
    cx = {v: i for i, v in enumerate(xs)}
    cy = {v: i for i, v in enumerate(ys)}

    compressed = [(cx[x], cy[y]) for (x, y) in points]
    return compressed, cx, cy

with open(path) as f:
    points = ([list(map(int,i.strip().split(','))) for i in f])


print(compress_points(points))