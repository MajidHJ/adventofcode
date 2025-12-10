import math

spath = 'day9/sample.txt'
ipath = 'day9/input.txt'
path = spath


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

boundries = []
green_red_tiles = []

with open(path) as f:
    min_x = math.inf
    max_x = -math.inf
    min_y = math.inf
    max_y = -math.inf


    points = ([tuple(map(int,i.strip().split(','))) for i in f])
    x0,y0 = points[0]
    for point in points[1:] :
        step = 1
        x1,y1 = point
        if x1 == x0:
            if y1-y0 < 0 : step = -1
            for y in range(y0+step,y1,step):
                boundries.append((x0,y))
        elif y0 ==y1 :
            if x1-x0 < 0 : step = -1
            for x in range(x0+step,x1,step):
                boundries.append((x,y0))
        else:
            print('Something Wrong!!')
            break
        if x0 < min_x : min_x = x0
        if y0 < min_y : min_y = y0
        if x0 > max_x : max_x = x0
        if y0 > max_y : max_y = y0


        x0 = x1
        y0 = y1
    
    boundries.extend(points)
    
    for y in range(min_y,max_y+1):
        for x in range(min_x,max_x+1):
            if (x,y) in boundries:
                for k in range(x+1,)








    # points.sort(key = lambda x: (x[0],x[1]))
    
    # print(boundries)

# area = area_vector(points)
# area.sort(key=lambda x: x[2])
# print(area[-1][2])