import sys
input = sys.stdin.readline

arr = [0] * 10001

N = int(input())
for _ in range(N):
    n = int(input())
    arr[n] += 1

for i in range(1, 10001):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)