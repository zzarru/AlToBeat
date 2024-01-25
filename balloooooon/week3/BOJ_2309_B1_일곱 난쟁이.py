from itertools import combinations
dwarf=[]
for i in range(9):
    dwarf.append(int(input()))
total=sum(dwarf)

for orc in combinations(dwarf,2):
    if total-sum(orc)==100:
        break
dwarf.remove(orc[0])
dwarf.remove(orc[1])
dwarf.sort()
for i in dwarf:
    print(i)