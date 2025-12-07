import os
import time

start = time.time()

base = os.path.dirname(os.path.abspath(__file__))
ipath = os.path.join(base, 'input.txt')
opath = os.path.join(base, 'output.txt')


all_invalids = []
total_sum = 0

def find_invalids(a,b):
    ssum = 0
    invalids = []

    for i in range(a,b+1):
        s = str(i)
        l = len(s)
        if l<2 : continue
        for size in range(1,min(l,6)):
            if l%size!=0 : continue
            block = s[:size]
            if s == block*(l//size) :
                invalids.append(s +'\n')
                ssum+= i
                break
    return ssum,invalids

with open(ipath) as f:
    content = f.read().split(',')
    for i in content:
        if i.startswith('0'): print(i)
        a,b = map(int,i.split('-'))
        sum,invalids = find_invalids(a,b)
        total_sum += sum
        all_invalids.extend(invalids)



with open(opath,'w') as f:
    f.writelines(all_invalids)



print(total_sum)

end = time.time()
print(end - start,'Seconds')
