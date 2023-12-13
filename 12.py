"""
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""

res = {}

with open("input2") as f:
    for l in f:
        row, nums = l.strip().split()
        nums = list(map(int, nums))
        lennums = len(nums)
        lenrow = len(row)
        dp = [[1 for i in range(lenrow)]]
        for i in range(lennums):
            dp.append([0 for j in range(lenrow)])

        for i in range(lenrow):
            j = lenrow-i-1







# def getcombos(row, nums):
#     # print(row, nums)
#     if len(nums) == 0:
#         if all([x!="#" for x in row]):
#             return 1, [row]
#         return 0, []
#     if nums[0] > len(row):
#         return 0, []
#     currnum = nums[0]
#     count = 0
#     ways = []
#     for i in range(len(row)-currnum+1):
#         last = i+currnum
#         if "." in row[i:last]:
#             continue
#         if (i-1 < 0 or row[i-1] != "#") and (last >= len(row) or row[last] != "#"):
#             # if currnum == 2:
#             #     print("found", row[:last+1], "checking", row[last+1:])
#             currcount, newways = getcombos(row[last+1:], nums[1:])
#             count += currcount
#             for nw in newways:
#                 newstr = ''.join(["#" for _ in range(currnum)])
#                 if last < len(row):
#                     newstr += row[last]
#                 ways.append(f"{row[:i]}{newstr}{nw}")
#         if row[i] == "#":
#             break
    # return count, ways

# def getcombos(row, nums):
#     if len(nums) == 0:
#         if all([x!="#" for x in row]):
#             return 1
#         return 0
#     if nums[0] > len(row):
#         return 0
#     currnum = nums[0]
#     count = 0
#     for i in range(len(row)):
#         last = i+currnum
#         if last > len(row):
#             break
#         if "." in row[i:last]:
#             continue
#         if (i-1 < 0 or row[i-1] != "#") and (last >= len(row) or row[last] != "#"):
#             count += getcombos(row[last+1:], nums[1:])
#         if row[i] == "#":
#             break
#     return count

# expectedAnswers = [1,4,1,1,4,10,3,2,3,4]
# actualAnswers = []
# with open("input2") as f:
#     total = 0
#     for l in f:
#         row, nums = l.strip().split()
#         nums = list(map(int, nums.split(",")))
        
#         currtotal = getcombos(row, nums)
#         # currtotal, ways = getcombos(row, nums)
#         # for w in ways:
#         #     print(w)
#         print(currtotal, end=",")
#         actualAnswers.append(currtotal)
#         total += currtotal
#         # print()

# print(actualAnswers == expectedAnswers)
# print(actualAnswers)
# print(total)


# # too high:
# # 9789
# # 8295