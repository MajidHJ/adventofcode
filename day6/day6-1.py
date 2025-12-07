import os
import io
base = os.path.dirname(os.path.abspath(__file__))
ipath = os.path.join(base, 'input.txt')
spath = os.path.join(base, 'sample.txt')
opath = os.path.join(base, 'output.txt')



with open(spath) as f:
    content = f.read()
    grand_total = 0
    worksheet = [list(map(int,line.split()))  for line in content.splitlines()[:-1]]
    operands = content.splitlines()[-1].split()
    print(worksheet)
    print(operands)
    for i in range (len(worksheet[0])):
        result = 0
        if operands[i] == '+':
            for j in range(len(worksheet)):
                result += worksheet[j][i]
        elif operands[i] == '*':
            if result ==0 : result =1
            for j in range(len(worksheet)):
                result = worksheet[j][i] * result

        grand_total += result
    

print(grand_total)


        
