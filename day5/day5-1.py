import os
import io
base = os.path.dirname(os.path.abspath(__file__))
ipath = os.path.join(base, 'input.txt')
spath = os.path.join(base, 'sample.txt')
opath = os.path.join(base, 'output.txt')


ranges = []
numbers = []
fresh = []

with open(ipath) as f:
    for i in f:
        if i.strip() == '': continue
        if '-' in i :
            ranges.append(list(map(int,i.split('-'))))
        else:
            numbers.append(int(i))


    for num in numbers:
        for j in ranges:
            if j[0] <= num <= j[1]:
                fresh.append(num)
                break

print(ranges)
print(numbers)
print(fresh)
print(len(set(fresh)))