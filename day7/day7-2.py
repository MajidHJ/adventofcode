ipath = 'day7/input.txt'
spath = 'day7/sample.txt'
with open(ipath) as f:
    emiter_idx = f.readline().find('S')
    spliter_idx = []
    all_spliter_idx = []
    all_beam_idx = []
    beam_idx = set()
    beam_idx.add(emiter_idx)
    routes_count = 1
    for i in f:
        if not('^' in i) : continue
        spliter_idx = (([idx for idx,ch in enumerate(i) if ch == '^']))
        for s in spliter_idx:
            if s in beam_idx:
                beam_idx.remove(s)
                beam_idx.add(s-1)
                beam_idx.add(s+1)
        all_beam_idx.append(beam_idx)
        all_spliter_idx.append(spliter_idx)

print(len(all_beam_idx))
print(len(all_spliter_idx))


for i in range (len(all_beam_idx)):
    ...