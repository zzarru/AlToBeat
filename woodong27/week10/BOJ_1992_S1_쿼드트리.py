# BOJ 1992 S1 쿼드트리

"""
이전에 풀었던 색종이 문제와 비슷하게
분할된 영역의 전체 값이 같지 않다면,
다시 네 영역으로 쪼개면서 재귀를 반복하면 된다.
"""

N = int(input())
image = [list(input())for _ in range(N)]


def dividing(si, sj, n):
    global answer
    pixel = image[si][sj]
    for i in range(si, si + n):
        for j in range(sj, sj + n):
            if pixel != image[i][j]:
                answer.append('(')
                dividing(si, sj, n//2)
                dividing(si, sj + n//2, n//2)
                dividing(si + n//2, sj, n//2)
                dividing(si + n//2, sj + n//2, n//2)
                answer.append(')')
                return
    answer.append(pixel)


answer = []
dividing(0, 0, N)
print(''.join(answer))
