
with open("input") as f:
    for l in f:
        steps = l.strip().split(",")

def HASH(s):
    total = 0
    for c in s:
        total += ord(c)
        total *= 17
        total %= 256
    return total

def printBoxes(b):
    for i, x in enumerate(b):
        if len(x) > 0:
            print(i, ":", end=' ')
            for l, f in x:
                print(f"[{l} {f}]", end="")
            print()
            


boxes = [[] for _ in range(256)]
for s in steps:
    # print(s)
    if s[-1] == '-':
        label = s[:-1]
        box = HASH(label)
        todelete = -1
        for i, lens in enumerate(boxes[box]):
            if lens[0] == label:
                todelete = i
        if todelete > -1:
            del boxes[box][todelete]
    elif '=' in s:
        label, fl = s.split('=')
        focallength = int(fl)
        box = HASH(label)
        found = False
        for i, n in enumerate(boxes[box]):
            if n[0] == label:
                found = True
                boxes[box][i][1] = focallength
                break
        if not found:
            boxes[box].append([label, focallength])
    else:
        print("what is this: ", s)
    # printBoxes(boxes)
    # print()

total = 0
for i in range(len(boxes)):
    b = boxes[i]
    for j in range(len(b)):
        fl = (1+i)*(j+1)*b[j][1]
        # print("fl:", fl)
        total += fl

print(total)



"""
The focusing power of a single lens is the result of multiplying together:

    One plus the box number of the lens in question.
    The slot number of the lens within the box: 1 for the first lens, 2 for the second lens, and so on.
    The focal length of the lens.
"""






# with open("input") as f:
#     for l in f:
#         steps = l.strip().split(",")


# sumtotal = 0
# """
# Determine the ASCII code for the current character of the string.
# Increase the current value by the ASCII code you just determined.
# Set the current value to itself multiplied by 17.
# Set the current value to the remainder of dividing itself by 256.
# """
# for s in steps:
#     total = 0
#     for c in s:
#         total += ord(c)
#         total *= 17
#         total %= 256
#     sumtotal += total

# print(sumtotal)

