import os
base = os.path.dirname(os.path.abspath(__file__))
ipath = os.path.join(base, 'input.txt')
spath = os.path.join(base, 'sample.txt')
opath = os.path.join(base, 'output.txt')


def max_jolt(bank:str):
    tens_max_digit = 1
    ones_max_digit = 1
    decimal_max_digit_index = 0

    for i in bank[:-1]:
        if int(i)> tens_max_digit: 
            tens_max_digit = int(i)
            decimal_max_digit_index = bank.find(i)
    
    for j in bank[decimal_max_digit_index+1:]:
        if int(j)>ones_max_digit : ones_max_digit = int(j)


    return 10*tens_max_digit + ones_max_digit



total_jolts = 0
with open(ipath) as f:

    for line in f:
         x = max_jolt(line.strip())
         total_jolts += x
         

print(total_jolts)
        

    


