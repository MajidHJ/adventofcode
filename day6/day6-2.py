import os
base = os.path.dirname(os.path.abspath(__file__))
ipath = os.path.join(base, 'input.txt')

with open(ipath) as f:
    content = f.read()
    lines = []
    grand_total = 0
    operands = content.splitlines()[-1]
    col_idx = [i-1 for i,ch in enumerate(operands) if ch in '+*']

    for line in content.splitlines()[:-1]:
        new_line = ''
        for idx,ch in enumerate(line):
            if ch==' ' :
                if idx in col_idx :
                    new_line +=ch
                else:
                    new_line +='X'
            else:
                new_line +=ch
        
        lines.append(new_line)


    worksheet = [line.split() for line in lines]
    new_worksheet = list(zip(*worksheet))

    operands = operands.split()
    
    for x in range(len(new_worksheet)):
        p = new_worksheet[x]
        result = 0
        col = len(p[0])
        numbers = []
        for i in range(col):
            s = ''.join([p[j][i].replace('X',' ') for j in range(len(p))])           
            numbers.append(int(s))

        if operands[x] == '+':
            result = sum(numbers)
        else:
            result =1 
            for i in numbers : result *=i

        grand_total += result
                
    print(grand_total)



        
