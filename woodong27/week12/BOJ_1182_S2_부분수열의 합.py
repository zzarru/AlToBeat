# BOJ 1182 S2 부분수열의 합

"""
dfs로 순열을 만들어서
각 순열의 합이 s인지 확인하면 된다.
"""

n, s = map(int, input().split())
numbers = list(map(int, input().split()))


def dfs(current, idx):
    global answer
    if sum(current) == s:
        answer += 1

    for j in range(idx + 1, n):
        if not visited[j]:
            visited[j] = 1
            dfs(current + [numbers[j]], j)
            visited[j] = 0


visited = [0] * n
answer = 0
for i in range(n):
    visited[i] = 1
    dfs([numbers[i]], i)
    visited[i] = 0

print(answer)
