import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 포켓몬 사전 만들기
poketmon_name = {}
poketmon_number = {}

for n in range(N):
    poketmon = input().strip()  # 개행 제거
    poketmon_number[n] = poketmon
    poketmon_name[poketmon] = n

# 출력하기
for _ in range(M):
    method = input().strip()
    if method.isdigit(): # 숫자인지 아닌지 판단하여
        print(poketmon_number[int(method) - 1]) # 숫자면 해당 포켓몬의 이름 출력
    else:
        print(poketmon_name[method]+1)

