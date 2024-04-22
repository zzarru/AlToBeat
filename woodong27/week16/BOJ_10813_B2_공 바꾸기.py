# BOJ 10813 B2 공 바꾸기

"""
야근한 날
문제가 도저히 머리에 안들어와서 그냥 브론즈
"""

n, m = map(int, input().split())
baskets = [i for i in range(n + 1)]

for _ in range(m):
    from_, to = map(int, input().split())
    baskets[from_], baskets[to] = baskets[to], baskets[from_]

print(*baskets[1:])
