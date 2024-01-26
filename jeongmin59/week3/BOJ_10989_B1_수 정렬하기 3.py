# 10989_수 정렬하기 3
'''
- N개의 수가 주어졌을 때 오름차순으로 정렬
- 주어지는 수는 10,000보다 작거나 같은 자연수
- 메모리 제한 8mb
'''
import sys

N = int(sys.stdin.readline())
lst = [0] * 10001

for _ in range(N):
    num = int(sys.stdin.readline())
    lst[num] += 1

for i in range(10001):
    if lst[i] != 0:
        for j in range(lst[i]):
            print(i)

'''
* Counting Sort
- 배열의 인덱스를 특정한 데이터의 값으로 여김
- 배열의 크기는 데이터의 범위를 포함할 수 있도록 설정
- 데이터가 등장한 횟수를 셈
- 유의사항: 데이터의 개수가 많을 때 파이썬에서 `sys.stdin.readline()`을 씀

---
* 메모리 초과 났었던 내 코드 

N = int(input())
lst = []

for _ in range(N):
    num = int(input())
    lst.append(num)

lst.sort()

for i in lst:
    print(i)

- 반복문 안에 append를 썼기 때문에 메모리 재할당이 일어남
- 속도 저하와 비효율적인 메모리 사용이 발생
- 모든 입력을 배열에 저장하면 메모리 초과가 됨
'''
