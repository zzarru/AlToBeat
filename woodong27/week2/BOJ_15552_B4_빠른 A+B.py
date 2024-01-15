# 백준 15552 B4 빠른 A+B

import sys

# 테스트 케이스의 갯수
T = int(input())

for _ in range(T):
    # 시간초과 방지를 위해 sys.stdin.readline()을 사용해서 입력받음
    A, B = map(int, sys.stdin.readline().strip().split())
    print(A + B)
    
