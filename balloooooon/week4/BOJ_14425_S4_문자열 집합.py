# 어제와 풀이 방식은 아주 동일하다고 할 수 있다
import sys
N, M = map(int,input().rstrip().split())
answer = 0
input = sys.stdin.readline

S = {}
for i in range(N):
    str = input().rstrip()
    S[str] = 1

for i in range(M):
    str = input().rstrip()
    if str in S:
        answer += 1
print(answer)

