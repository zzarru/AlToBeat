import sys
input =  sys.stdin.readline

# 입력 받기
n, k = map(int, input().split())

idx = 0
people = [i for i in range(1, n+1)]
exits= []
while people :
    idx += k - 1  # 제거할 인덱스
    if idx >= len(people ):  # 인덱스가 범위를 넘어갈 경우
        idx %= len(people )  # 나머지 연산을 통해 인덱스 계산
    exits.append(str(people .pop(idx)))  # k번째 수 제거 후 배열에 추가

# 결과 출력
print("<", ", ".join(exits), ">", sep="")