# BOJ 13164 G5 행복 유치원

"""
원생들이 오름차순으로 정렬되어서 들어오기 때문에
옆자리와의 키 차이를 구한 뒤, 키 차이가 가장 큰 결과를 제외하면 된다.
제외하는 수는 입력받는 K(부분 리스트의 갯수)에 따라서 달라진다.
"""

N, K = map(int, input().split())
children = list(map(int, input().split()))

difference = [children[i] - children[i-1] for i in range(1, N)]
difference.sort()

answer = sum(difference[:N-K])
print(answer)
