# BOJ 13144 G4 List of Unique Numbers

"""
어제 푼 문제랑 동일한 원리
"""

n = int(input())
numbers = list(map(int, input().split()))

counts = [0] * 100001
end, answer = 0, 0
for start in range(n):
    while end < n:
        if counts[numbers[end]] >= 1:
            break
        counts[numbers[end]] += 1
        end += 1
    counts[numbers[start]] -= 1
    answer += end - start

print(answer)
