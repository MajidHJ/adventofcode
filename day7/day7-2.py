ipath = 'day7/input.txt'
spath = 'day7/sample.txt'
with open(spath) as f:
    emiter_idx = f.readline().find('S')
    spliter_idx = []
    all_spliter_idx = []
    all_beam_idx = []
    beam_idx = set()
    beam_idx.add(emiter_idx)
    routes_count = 1
    for i in f:
        # print(beam_idx)
        if not('^' in i) : continue
        all_beam_idx.append(beam_idx)
        spliter_idx = (([idx for idx,ch in enumerate(i) if ch == '^']))
        for s in spliter_idx:
            if s in beam_idx:
                beam_idx.remove(s)
                beam_idx.add(s-1)
                beam_idx.add(s+1)
        all_spliter_idx.append(spliter_idx)


print(len(all_beam_idx))
# print(len(all_spliter_idx))
print(all_beam_idx)
# print(all_spliter_idx[0])

for i in range (len(all_beam_idx)):
    ...