import os
import time

start = time.time()

base = os.path.dirname(os.path.abspath(__file__))
ipath = os.path.join(base, "input.txt")
opath = os.path.join(base, "output.txt")


def find_invalids(a, b):
    invalids = []
    ssum = 0

    for n in range(a, b + 1):
        s = str(n)
        l = len(s)

        if l < 2:
            continue

        # size: length of repeating block
        # blocks must divide length and be different from full length
        for size in range(1, min(6, l)):
            if l % size != 0:
                continue

            block = s[:size]
            if block * (l // size) == s:
                invalids.append(s + "\n")
                ssum += n
                break

    return invalids, ssum


all_invalids = []
total_sum = 0

with open(ipath) as f:
    ranges = f.read().split(",")

    for r in ranges:
        if r.startswith("0"):
            print(r)

        a, b = map(int, r.split("-"))
        inv, ssum = find_invalids(a, b)
        all_invalids.extend(inv)
        total_sum += ssum


with open(opath, "w") as f:
    f.writelines(all_invalids)

print(total_sum)

end = time.time()

print(end - start,'Seconds')