import os
base = os.path.dirname(os.path.abspath(__file__))
ipath = os.path.join(base, 'input.txt')
opath = os.path.join(base, 'output.txt')


all_invalids =  []
sum = 0
def find_invalids(a,b):
    global sum
    for i in range(a,b+1):
        s = str(i)
        l = len(str(i))
        if l%2==0:
            if s[:l//2]==s[l//2:] :
                all_invalids.append(s+'\n')
                sum += i


with open(ipath) as f:
    content = f.read().split(',')
    for i in content:
        if i.startswith('0'): print(i)
        a,b = i.split('-')
        find_invalids(int(a),int(b))


with open(opath,'w') as f:
    f.writelines(all_invalids)



print(sum)