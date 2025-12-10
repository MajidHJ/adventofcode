from shapely.geometry import Polygon, box, Point
import math
import matplotlib.pyplot as plt


from shapely.geometry import Polygon, box



spath = 'day9/sample.txt'
ipath = 'day9/input.txt'
path = ipath
# تابع کمکی برای رسم
def plot_shape(shape, color='blue', alpha=0.5):
    if shape.is_empty:
        return
    if hasattr(shape, 'geoms'):  # MultiPolygon یا GeometryCollection
        for geom in shape.geoms:
            plot_shape(geom, color, alpha)
    else:
        x, y = shape.exterior.xy
        plt.fill(x, y, alpha=alpha, fc=color, ec='black')

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
    shape_points = ([list(map(int,i.strip().split(','))) for i in f])
poly = Polygon(shape_points)


area = area_vector(shape_points)
area.sort(key=lambda x: x[2],reverse=True)

diffs = []

for i in area:
    a,b,c = i
    p1 = shape_points[a]
    p2 = shape_points[b]
    
    x1, y1 = p1
    x2, y2 = p2

    rect = box(min(x1, x2), min(y1, y2),
            max(x1, x2), max(y1, y2))
    
    p1 = Point((x1, y1))
    p2 = Point((x1, y2))
    p3 = Point((x2, y1))
    p4 = Point((x2, y2))

    valid = poly.covers(p1) and poly.covers(p2) and poly.covers(p3) and poly.covers(p4)

    if not valid : continue

    if rect.difference(poly).area==0 :
        diffs.append(f'{a}  {b} Area: {c}  Diff:  {rect.difference(poly).area}\n')

    is_inside = poly.covers(rect)

    if is_inside : 
        print(poly.difference(rect).area)
        print(rect.difference(poly).area)
        print(rect.difference(poly).is_empty)
        print(a,b,f'Area: {c}')
        # رسم
        plt.figure(figsize=(6,6))
        plot_shape(poly, color='lightgreen', alpha=0.4)
        plot_shape(rect, color='lightblue', alpha=0.6)

        plt.axis('equal')
        plt.show()
        break

with open('Day9/x.txt','w') as f:
    f.writelines(diffs)

