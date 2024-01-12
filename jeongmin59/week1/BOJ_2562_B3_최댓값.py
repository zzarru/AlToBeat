# 2562 최댓값
'''
- 9개 서로 다른 자연수가 주어질 때, 최댓값을 찾고 몇 번째 수인지 출력
'''

N = 9
lst = []

for _ in range(N):
    n = int(input())
    lst.append(n)

maxV = 0
idx = 0

for i in range(N):
    if lst[i] >= maxV:
        maxV = lst[i]
        idx = i + 1

print(maxV)
print(idx)

'''
# 예전에 풀었던 다른 방법 - for문에서
for i in range(9):
    num = int(input())

    if maxV < num:
        maxV = num
        idx = i
'''
