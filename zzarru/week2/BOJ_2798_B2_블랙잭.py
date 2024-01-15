N, M = map(int, input().split())
nums = list(map(int, input().split()))

sums = []
for a in range(N-2):
    for b in range(a+1, N-1):
        for c in range(b+1, N):
            A = nums[a]
            B = nums[b]
            C = nums[c]

            sums.append(A+B+C)

ans = 0
for i in sums:
    if i <= M:
        if i > ans:
            ans = i

print(ans)
