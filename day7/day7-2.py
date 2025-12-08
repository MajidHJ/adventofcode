ipath = 'day7/input.txt'
spath = 'day7/sample.txt'
with open(spath) as f:
    emiter_idx = f.readline().find('S')
    spliter_idx = []
    all_spliter_idx = []
    all_beam_idx = []
    beam_idx = set()
    beam_idx.add(emiter_idx)
    total_routes = 0
    colision = 0
    routes = [f'-{emiter_idx}']
    for i in f:
        # print(beam_idx)
        if not('^' in i) : continue
        bi = list(beam_idx)
        bi.sort()
        all_beam_idx.append(bi)
        spliter_idx = (([idx for idx,ch in enumerate(i) if ch == '^']))
        for s in spliter_idx:
            if s in beam_idx:
                beam_idx.remove(s)
                beam_idx.add(s-1)
                beam_idx.add(s+1)
                colision +=1
                for r in routes.copy() :
                    if r.endswith(f'-{s}'):
                        routes.append(f'-{r}-{s-1}')
                        routes.append(f'-{r}-{s+1}')
                        routes.remove(r)
        print(('-----',len(routes)))
        all_spliter_idx.append(spliter_idx)


print(all_beam_idx)
print(all_spliter_idx)
print(len(routes))

for i in all_beam_idx:
    ...

print(total_routes)
print(colision)