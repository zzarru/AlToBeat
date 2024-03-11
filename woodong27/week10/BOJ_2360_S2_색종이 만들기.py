# BOJ 2630 S2 색종이 만들기

"""
정사각형을 네조각으로 쪼개가며 재귀하면 된다.
첫번째 칸과 나머지 칸의 색깔이 다르면
다시 칸을 네 부분으로 나누어서 재귀하고
아니라면 흰색, 파란색에 따라서 결과를 더해준다.
"""

n = int(input())

paper = [list(map(int, input().split())) for _ in range(n)]


def separation(si, sj, number):
    global white, blue
    color = paper[si][sj]
    for i in range(si, si + number):
        for j in range(sj, sj + number):
            if color != paper[i][j]:
                separation(si, sj, number//2)
                separation(si, sj + number//2, number//2)
                separation(si + number//2, sj, number//2)
                separation(si + number//2, sj + number//2, number//2)
                return
    if color:
        blue += 1
    else:
        white += 1


white, blue = 0, 0
separation(0, 0, n)
print(white)
print(blue)
