import math

spath = 'day8/sample.txt'
ipath = 'day8/input.txt'
path = ipath

def pairwise_dist_python(points):
    n = len(points)
    dist = []
    for i in range(n):
        for j in range(i+1,n):
            x1, y1, z1 = points[i]
            x2, y2, z2 = points[j]
            d = round(math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2),2)
            dist.append((i,j,d))

    return dist


with open(path) as f:
    points = ([list(map(int,i.strip().split(','))) for i in f])

dist = pairwise_dist_python(points)
# print(dist)

sections = []
main_section = [i for i in range(len(points))]
sections.append(main_section)
dist.sort(key=lambda x : x[2])


for i in dist:
    a,b,d = i
    change = True

    if a in main_section.copy() and b in main_section.copy():
        main_section.remove(a)
        main_section.remove(b)
        sections.pop(0)
        sections.insert(0,main_section)
        sections.append([a,b])
    elif a in main_section.copy():
        main_section.remove(a)
        sections.pop(0)
        sections.insert(0,main_section)
        for j in sections[1:].copy():
            if b in j :
                j.append(a)
                break
    elif b in main_section.copy():
        main_section.remove(b)
        sections.pop(0)
        sections.insert(0,main_section)
        for j in sections[1:].copy():
            if a in j :
                j.append(b)
                break
    else:
        for q in sections.copy():
            if a in q :
                a_sec = q
            if b in q :
                b_sec = q
        if not(a_sec == b_sec) :
            merge = a_sec+b_sec
            sections.remove(a_sec)
            sections.remove(b_sec)
            sections.append(merge)
        else:
            change = False
    
    if change:
        x = a
        y = b
            

    

print(points[x][0]*points[y][0])

# print(points[sections[1][-1][0]]*points[sections[1][-2][0]])