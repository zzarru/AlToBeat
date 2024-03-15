# BOJ 17829 S2 222-풀링

"""
이전에 풀었던 문제들과 유사하게
재귀를 통해 가장 작은 사이즈의 결과를 구하고
해당 결과과들을 취합해서 반환하면 된다.
"""

N = int(input())
matrix = [list(map(int, input().split()))for _ in range(N)]


def pooling222(si, sj, n):
    if n == 2:
        temp = []
        for i in range(si, si + n):
            for j in range(sj, sj + n):
                temp.append(matrix[i][j])
        temp.sort()
        return temp[-2]

    mid = n // 2
    a = pooling222(si, sj, mid)
    b = pooling222(si, sj + mid, mid)
    c = pooling222(si + mid, sj, mid)
    d = pooling222(si + mid, sj + mid, mid)

    result = [a, b, c, d]
    result.sort()
    return result[-2]


answer = pooling222(0, 0, N)
print(answer)
