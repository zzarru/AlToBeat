from itertools import permutations
a,b=input().split()
a_lst=list(a)
a_lst.sort()
ans=-1
for i in list(permutations(a_lst)):
    if i[0] != '0' and int(b) > int(''.join(i)):
        ans = max(ans,int(''.join(i)))
print(ans)
