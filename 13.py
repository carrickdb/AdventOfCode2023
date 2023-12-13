def getCount(grid):
    w = len(grid[0])
    # print(w)
    for l in range(1,w):
        found = True
        r = min(l, w-l)
        for row in grid:
            mirror = list(reversed(row[l:r+l]))
            if row[l-r:l] != mirror:
                found = False
                break
        if found:
            return l
    return None

total = 0
with open("input") as f:
    currmap = []
    for l in f:
        if l == "\n":
            count = getCount(currmap)
            if not count:
                newmap = []
                for j in range(len(currmap[0])):
                    newmap.append([currmap[i][j] for i in range(len(currmap))])
                count = getCount(newmap)
                if not count:
                    print("something went wrong")
                    exit()
                count *= 100
            total += count
            currmap = []
        else:
            currmap.append(list(l.strip()))

print(total)


# def getCount(grid):
#     w = len(grid[0])
#     # print(w)
#     for l in range(1,w):
#         found = True
#         r = min(l, w-l)
#         for row in grid:
#             mirror = ''.join(reversed(row[l:r+l]))
#             if row[l-r:l] != mirror:
#                 # if l == 5:
#                 #     print("row[l-r:l] != mirror:" + row[l-r:l] + "!=" + mirror + "]")
#                 found = False
#                 break
#         if found:
#             return l
#     return None

# total = 0
# with open("input") as f:
#     currmap = []
#     for l in f:
#         if l == "\n":
#             count = getCount(currmap)
#             # print("count", count)
#             if not count:
#                 newmap = []
#                 for j in range(len(currmap[0])):
#                     newmap.append(''.join([currmap[i][j] for i in range(len(currmap))]))
#                 count = getCount(newmap)
#                 if not count:
#                     print("something went wrong")
#                     exit()
#                 # print("col count:", count)
#                 count *= 100
#             total += count
#             currmap = []
#         else:
#             currmap.append(l.strip())
#             # print(currmap)

# print(total)