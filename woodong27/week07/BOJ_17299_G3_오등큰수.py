# BOJ 17299 G3 오등큰수

"""
어제 제출한 오큰수와 비슷한 문제
오큰수와 다르게
오른쪽에 있으면서 더 큰수가 아니라
오른쪽에 있으면서 수열에 등장하는 횟수가 더 많을 경우에
오등큰수에 해당한다.

처음에 list comprehension을 사용해서
f_list = [numbers.count(number) for number in numbers]
로 하니까 시간초과 발생

-> counts배열을 만들어서 사용
"""

n = int(input())
numbers = list(map(int, input().split()))

counts = [0] * (max(numbers) + 1)
for number in numbers:
    counts[number] += 1


def NGF(idx):
    global answer, stack
    while stack and counts[numbers[stack[-1]]] < counts[numbers[idx]]:
        answer[stack.pop()] = numbers[idx]
    stack.append(idx)


stack = [0]
answer = [-1] * n
for i in range(1, n):
    NGF(i)

print(*answer, sep=" ")
