s1 = ['123','456','678','348']
for i in range(len(s1[0])):
    s = ''
    for j in range(len(s1)):       
        s += s1[j][i]
    print(s)

