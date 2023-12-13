dirs = [[0,1], [0,-1], [-1, 0], [1,0]]
diagDirs = [[0,1], [0,-1], [-1, 0], [1,0], [-1, -1], [1, 1], [-1, 1], [1, -1]]

def printMapGrid(g):
    for i in range(len(g.keys())):
        for j in range(len(g[i].keys())):
            print(g[i][j], end="\t")
        print()

def printGridList(g):
    for row in g:
        print(''.join(row))
    print()