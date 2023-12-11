import numpy, queue, aoc, copy

def printGrid(g):
    for l in g:
        print(l)

u = []
with open("input") as f:
    i = 0
    for l in f:
        l = l.strip()
        u.append(list(l))
        if all([x=="." for x in l]):
            u.append(list(l))

u = numpy.transpose(u)

u2 = []
for row in u:
    u2.append(row)
    if all([x=="." for x in row]):
        u2.append(row.copy())

u = numpy.transpose(u2)
printGrid(u)

umap = {}
for i in range(len(u)):
    umap[i] = {}
    for j in range(len(u[0])):
        umap[i][j] = u[i][j]

total = 0

paths = set()

def getPaths(g, i, j):
    q = queue.Queue()
    q.put((i,j))
    currtotal = 0
    steps = 0
    while not q.empty():
        # aoc.printMapGrid(g)
        # print(list(q.queue))
        lenq = q.qsize()
        for _ in range(lenq):
            ci, cj = q.get()
            if g[ci][cj] == "#":
                path = ((ci, cj), (i, j))
                if path not in paths:
                    currtotal += steps
                    paths.add(path)
                    paths.add(((i,j), (ci, cj)))
            if g[ci][cj] == "X":
                continue
            g[ci][cj] = "X"
            for di, dj in aoc.dirs:
                ni, nj = di+ci, dj+cj
                if ni in g and nj in g[ni]:
                    if g[ni][nj] != "X":
                        q.put((ni, nj))
        steps += 1
    return currtotal

for i in range(len(umap)):
    for j in range(len(umap[0])):
        curr = umap[i][j]
        if curr == '#':
            total += getPaths(copy.deepcopy(umap), i, j)
            print(total)

print(total)