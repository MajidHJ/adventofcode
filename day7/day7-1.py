path = 'day7/input.txt'
with open(path) as f:
    emiter_idx = f.readline().find('S')
    spliter_idx = []
    beam_idx = set()
    beam_idx.add(emiter_idx)
    print(emiter_idx)
    colision = 0
    for i in f:
        spliter_idx = ([idx for idx,ch in enumerate(i) if ch == '^'])
        for s in spliter_idx:
            if s in beam_idx:
                beam_idx.remove(s)
                beam_idx.add(s-1)
                beam_idx.add(s+1)
                colision +=1


print(spliter_idx)
print(colision)
print(beam_idx)

