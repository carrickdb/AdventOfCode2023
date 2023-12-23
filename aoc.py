import requests

dirs = [[0,1], [0,-1], [-1, 0], [1,0]]
diagDirs = [[0,1], [0,-1], [-1, 0], [1,0], [-1, -1], [1, 1], [-1, 1], [1, -1]]

def printMapGrid(g):
    for i in sorted(g.keys(), reverse=True):
    # for i in sorted(g.keys()):
        for j in sorted(g[i].keys()):
            print(g[i][j], end="")
        print()

def printGridList(g):
    for row in g:
        print(''.join(row))
    print()

def getInput(filename):
    input = []
    with open(filename) as f:
        for l in f:
            input.append(l.strip())
    return input
