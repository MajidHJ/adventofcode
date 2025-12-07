ipath = 'day7/input.txt'
spath = 'day7/sample.txt'
with open(spath) as f:
    emiter_idx = f.readline().find('S')
    spliter_idx = []
    beam_idx = set()
    routes = set()
    routes.add(f'-{emiter_idx}')
    beam_idx.add(emiter_idx)
    colision = 0
    routes_count = 1
    for i in f:
        if not('^' in i) : continue
        spliter_idx = ([idx for idx,ch in enumerate(i) if ch == '^'])
        for s in spliter_idx:
            if s in beam_idx:
                beam_idx.remove(s)
                beam_idx.add(s-1)
                beam_idx.add(s+1)
                colision +=1
                routes_count += 2
                for r in routes.copy():
                    if r.endswith(f'-{s}'):
                        routes.add(f'{r}-{s-1}')
                        routes.add(f'{r}-{s+1}')
                        routes.remove(r)



print(((colision)))
print(((len(routes))))
print(((routes_count)))