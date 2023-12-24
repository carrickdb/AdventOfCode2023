import aoc
import numpy as np

input = aoc.getInput("input")

hail = []
for l in input:
    # 19, 13, 30 @ -2,  1, -2
    pos, vel = l.split(" @ ")
    pos = list(map(int, pos.split(", ")))
    vel = list(map(int, vel.split(", ")))
    hail.append((pos, vel))





# import aoc
# import numpy as np

# input = aoc.getInput("input")
# bl,bh = 7,27
# bl,bh = 200000000000000, 400000000000000

# hail = []
# for l in input:
#     # 19, 13, 30 @ -2,  1, -2
#     pos, vel = l.split(" @ ")
#     pos = list(map(int, pos.split(", ")))
#     vel = list(map(int, vel.split(", ")))
#     hail.append((pos, vel))


# inbounds = 0
# for i in range(len(hail)-1):
#     # https://problemsolvingwithpython.com/05-NumPy-and-Arrays/05.08-Systems-of-Linear-Equations/
#     p1, v1 = hail[i]
#     # print(f"p1: {p1}, v1: {v1}")
#     p1x, p1y, _ = p1
#     v1x,v1y,_ = v1
#     for j in range(i+1, len(hail)):
#         p2, v2 = hail[j]
#         # print(f"\tp2: {p2}, v2: {v2}")
#         p2x,p2y,_ = p2
#         v2x,v2y,_ = v2
#         A = np.array([[v1x, -v2x], [v1y, -v2y]])
#         b = np.array([p2x-p1x, p2y-p1y])
#         try:
#             t,v = np.linalg.solve(A, b)
#         except:
#             continue
#         if t < 0 or v < 0:
#             continue
#         x = t*v1x + p1x
#         y = t*v1y + p1y
#         if x >= bl and x <= bh and y >=bl and y <=bh:
#             # print(f"\tInside bounds at {x}, {y}")
#             inbounds += 1
#         # else:
#         #     print(f"\tOutside bounds at {x}, {y}")

# print(inbounds)