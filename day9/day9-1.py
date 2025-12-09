import math

spath = 'day9/sample.txt'
ipath = 'day9/input.txt'
path = ipath


def area_vector(points):
    n = len(points)
    dist = []
    for i in range(n):
        for j in range(i+1,n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            a = math.fabs(x1-x2+1)*math.fabs(y1-y2+1)
            dist.append((i,j,int(a)))

    return dist


with open(path) as f:
    points = ([list(map(int,i.strip().split(','))) for i in f])


area = area_vector(points)
area.sort(key=lambda x: x[2])
print(area[-1][2])