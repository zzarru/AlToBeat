from fractions import Fraction
N = int(input())
answer = []
num_list = list(map(int,input().split()))
a = num_list[-1]
for i in range(N-2,-1,-1):
    a = num_list[i] + Fraction(1,a)

temp = 1-Fraction(1,a)
answer.append(temp.numerator)
answer.append(temp.denominator)
print(*answer)
