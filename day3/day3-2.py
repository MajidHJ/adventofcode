import os
base = os.path.dirname(os.path.abspath(__file__))
ipath = os.path.join(base, 'input.txt')
spath = os.path.join(base, 'sample.txt')
opath = os.path.join(base, 'output.txt')


def max_jolt(bank:str):
    digits = []
    header = 0
    idx=0

    for i in range (12,0,-1):
        max_digit = 0
        a,b = (header,len(bank)-i+1)
        block = bank[a:b]

        for j,d in enumerate(block) :
            d_int = int(d)
            if d_int > max_digit: 
                max_digit = d_int
                idx = j
        
        header += idx+1
        digits.append(str(max_digit))
        

    return int(''.join(digits))


total_jolts = 0
with open(ipath) as f:

    for line in f: 
         total_jolts += max_jolt(line.strip())
         

print(total_jolts)
        

    


