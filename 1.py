import aoc

with open("input") as f:
    input = f.read()

numlist = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
total = 0
# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen
for l in input.split():
    print(l)
    nums = []
    for i in range(len(l)):
        x = l[i]
        if x.isdigit():
            nums.append(x)
        for j in range(len(numlist)):
            numStr = numlist[j]
            currstr = l[i:i+len(numStr)]
            print(currstr)
            if currstr == numStr:
                nums.append(str(j))
                break
    # break
    print(nums)
    newnum = int(nums[0]+nums[-1])
    total += newnum

print(total)



# total = 0
# for l in input.split():
# #     1abc2
# # pqr3stu8vwx
# # a1b2c3d4e5f
# # treb7uchet
#     nums = []
#     # print(l)
#     # for x in l.strip():
#     #     print(x)
#     #     if x.isdigit():
#     #         nums.append(x)
#     #     else:
#     #         print(x, "is not a digit")
#     # print(nums)
#     # break
#     nums = [x for x in l.strip() if x.isdigit()]
#     print(nums)
#     total += int(nums[0]+nums[-1])
# print(total)
