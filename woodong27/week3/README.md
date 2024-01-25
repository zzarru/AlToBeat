# Week3 (정렬)

## Python의 sort()

Python에서 제공하는 sort()와 sorted()메서드는 기본적으로 병합정렬을 기반으로 만들어져있다.

퀵 정렬보다 일반적으로 느리지만 최악의 경우에도 O(NlogN)의 시간복잡도를 보장한다.

기본적으로 사전순 정렬도 지원하기 때문에, 문자열들을 사전순으로 정렬하려고 할 때 sort를 사용하면 해결된다.

key 속성을 사용해서 자유롭게 정렬 기준을 정할 수 있다.

e.g

```python
words = ['ABC', 'BD', 'C']

# 길이순 정렬
words.sort(key=lambda x: len(x))

# 사전순 정렬
words.sort()

# 길이순 정렬 후, 사전순 정렬
words.sort(key=lambda x: (len(x), x))

```

---

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

## 카운팅 정렬(Counting Sort)

집합에 각 항목이 몇개 있는지 세어서 정렬하는 효율적인 알고리즘

정수나 정수로 표현 가능한(번호를 붙일 수 있는) 자료에 대해서만 적용 가능

시간 복잡도 : O(n+k)(n=리스트 길이, k=정수의 최대값) (버블정렬 대비 짧음)

```python
lst=[0,4,1,3,1,2,4,1]

result=[0 for x in range(len(lst))]
#result=[0]*len(lst)
counts=[0 for x in range(max(lst)+1)] #lst의 가장 큰 원소+1의 길이를 가진 리스트
#counts=[0]*(len(lst)+1)

for i in range(len(lst)):
    counts[lst[i]]+=1 #lst[i]번째 인덱스에 1씩 누적합

#print(counts) [1,3,1,1,2]

for i in range(1,len(counts)): #0번 인덱스는 필요없음
    counts[i]+=counts[i-1] # i번 인덱스의 원소에 그 전 인덱스의 원소를 더해줌

#print(counts) [1,4,5,6,8]

#lst=[0,4,1,3,1,2,4,1]
#counts=[1,4,5,6,8]
#result=[0,0,0,0,0,0,0,0]
for i in range(len(lst)-1,-1,-1): #len(lst)-1 : 7번 인덱스 부터 시작, 0번 인덱스까지
    counts[lst[i]]-=1
    result[counts[lst[i]]]=lst[i]

print(result) # [0,1,1,1,2,3,4,4]
```
