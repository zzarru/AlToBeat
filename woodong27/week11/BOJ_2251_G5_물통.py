# BOJ 2251 G5 물통

"""
bfs로 하면 더 간단할 것 같지만..
dfs를 사용해서 모든 경우에 대해 완전탐색으로 물을 이동시켰다.
"""


def dfs(b1, b2, b3):
    global results
    if not b1:
        results.add(b3)

    # 이동 가능한 모든 경우에 대해서 진행
    for from_bucket, to_bucket in ((0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)):
        current = [b1, b2, b3]
        move_amount = min(current[from_bucket], volumes[to_bucket] - current[to_bucket])
        moved = current[:]
        moved[from_bucket] -= move_amount
        moved[to_bucket] += move_amount
        moved = tuple(moved)

        if moved not in visited:
            visited[moved] = 1
            dfs(*moved)


# 바구니의 부피(volume)
volumes = list(map(int, input().split()))
visited = {}
results = set()
# 바구니(basket) 현재 상태
third = volumes[2]
dfs(0, 0, third)
print(*sorted(results))
