# BOJ 20922 S1 겹치는 건 싫어

"""
start와 end를 증가시키면서 counts배열에 numbers[end]번째 인덱스를 1씩 증가시킨다.
만약 counts배열에서 해당 인덱스의 원소가 k이상이 되면
조건을 만족하지 못하기 때문에 while문을 탈출하면 된다.

if counts[numbers[end]] >= k:
    answer = max(answer, end - start)
    counts[numbers[start]] -= 1
    break
이렇게 헀을 때 42퍼센트에서 계속 실패했다.

while end < n:
    if counts[numbers[end]] >= k:
        break
    counts[numbers[end]] += 1
    end += 1
answer = max(answer, end - start)
counts[numbers[start]] -= 1
이렇게 수정하고 통과할 수 있었다.

아래의 방법으로 하면 break후에 start가 1 증가하기 전에
answer를 비교하고 for 반복문이 실행된다.
"""

n, k = map(int, input().split())
numbers = list(map(int, input().split()))

counts = [0] * (max(numbers) + 1)

answer, end = 0, 0
for start in range(n - k + 1):
    while end < n:
        if counts[numbers[end]] >= k:
            break
        counts[numbers[end]] += 1
        end += 1
    answer = max(answer, end - start)
    counts[numbers[start]] -= 1

print(answer)
