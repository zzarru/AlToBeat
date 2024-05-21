import sys
input = sys.stdin.readline

#0 입력 받기
N = int(input())
n_list = list(map(int, input().split()))
M = int(input())
m_list = list(map(int, input().split()))


#1 이진탐색은 정렬된 상태에서 진행한다.
n_list.sort()

#2 각 원소에 대한 이진탐색
for m in m_list:
    # 시작과 끝 idx 지정
    start = 0
    end = N-1
    answer = 0 # 값을 찾았는가 여부 판단

    # 시작과 끝 idx가 같아질 때까지 반복한다.
    while start <= end:
        middle = (start + end) // 2 # 중간값

        # 1) 중간 값이 찾는 값일 경우
        if n_list[middle] == m:
            answer = 1
            break

        elif n_list[middle] < m:
            start = middle + 1

        else:
            end = middle - 1

    print(answer)