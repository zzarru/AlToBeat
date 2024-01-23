# Week3 (정렬)

## 버블정렬(Bubble Sort)

첫번째 원소부터 인접한 두개의 원소를 비교하며 자리를 교환하는 방식(시간 복잡도 : O(N^2))

```python
# peeudo code

# 55 7 78 12 42
# for i : N-1 -> 1      각 구간의 끝
#    for j : 0 -> i-1   비교할 왼쪽 원소
#        if arr[i]>arr[j+1]
#            arr[j]<->arr[j+1]  더 큰 원소 오른쪽으로 이동

#N=int(input())
#arr=list(map(int,input().split()))


arr=[55,7,78,12,42]
N=len(arr)

for i in range(N-1,0,-1):
	for j in range(i):
		if arr[j]>arr[j+1]:
			arr[j],arr[j+1]=arr[j+1],arr[j]

print(arr) # [7, 12, 42, 55, 78] -> 오름차순으로 정렬되었음
```

---
