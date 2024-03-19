# BOJ 17298 G4 오큰수

"""
처음에는 2중 반복문을 사용했지만 시간초과 발생
-> stack을 사용해서 현재 현재 검사하는 index를 stack에 저장하며 진행

9 5 4 8을 예로 들면
stack에는 가장 처음에 0이 들어가있음(첫번째 인덱스)
stack[-1] = 0이므로 idx가 1일때 numbers[0]과 numbers[1]을 비교하게 됨
answer 의 진행 상태
i = 1 : -1, -1, -1, -1
i = 2 : -1, -1, -1, -1
i = 3 : -1, 8, 8, -1
-> 오른쪽에서 더 큰 수를 만나면, 기존에 stack에 들어있던 모든 index에 대해서
오큰수 계산을 해준다.
"""

n = int(input())
numbers = list(map(int, input().split()))


def NGE(idx):
    global stack, answer
    while stack and numbers[stack[-1]] < numbers[idx]:
        answer[stack.pop()] = numbers[idx]
    stack.append(idx)


stack = [0]
answer = [-1] * n
for i in range(1, n):
    NGE(i)

print(*answer, sep=" ")
