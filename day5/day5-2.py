import os
import io
base = os.path.dirname(os.path.abspath(__file__))
ipath = os.path.join(base, 'input.txt')
spath = os.path.join(base, 'sample.txt')
opath = os.path.join(base, 'output.txt')


ranges = []
merged = []

with open(ipath) as f:
    for i in f:
        if i.strip() == '': continue
        if '-' in i :
            ranges.append(list(map(int,i.split('-'))))

    
    ranges.sort(key= lambda x : x[0])
    merged.append(ranges[0])
    idx = 0
    for i in ranges[1:]:
        x = merged[idx][0]
        y = merged[idx][1]
        a = i[0]
        b = i[1]
        if a > y : 
            merged.append(i)
            idx+=1
        elif b<= y :
            continue
        else:
            merged.append([y+1,b])
            idx+=1
    fresh = 0    
    for i in merged:
        fresh += i[1]-i[0]+1

# print(ranges)
# print(numbers)
# print(fresh)
print(fresh)