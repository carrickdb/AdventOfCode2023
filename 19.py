import aoc, re

input = aoc.getInput("input2")

inst = True
mapping = {}
for l in input:
    if l == "":
        inst = False
        continue
    if inst:
        # px{a<2006:qkq,m>2090:A,rfg}
        name, rest = inst.split("{")
        rest = rest[:-1].split(",")
        assessment = []
        for comp in rest[:-1]:
            pattern = re.compile("([xmas])([<>])([0-9]+):(.+)")
            m = re.findall(pattern, comp)
            if m[1] == ">":
                assessment.append(lambda x: m[3] if x[m[0]]>m[2] else None)
        
        assessment.append(lambda x: rest[-1])
            
    else:


total = 0
