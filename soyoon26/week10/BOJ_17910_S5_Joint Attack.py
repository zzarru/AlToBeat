import sys
from fractions import Fraction
N=int(sys.stdin.readline().rstrip())
nums=list(map(int,sys.stdin.readline().split()))
a=0
def fraction(lst,y,z,n):
    ans=Fraction(lst[n]*y+z,y)
    one = ans.numerator #분자
    two = ans.denominator
    n-=1
    if n== -1:
        print(ans)
        return ans
    fraction(lst,one,two,n)
if N == 1:
    print(*nums)
else:
    fraction(nums,nums[N-1],1,N-2)


#시간 줄이는 방법
def recursion(idx, N, D):
    N = pos[idx] * D + N
    D = D
    if idx < 1:
        print(f"{N}/{D}")
        return
    else:
        recursion(idx-1, D, N)

n = int(input())
pos = list(map(int, sys.stdin.readline().strip().split()))

if len(pos) == 1:
    print(pos[0])
else:
    recursion(n-2, 1, pos[-1])