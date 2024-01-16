# 3052_나머지
'''
- 수 10개를 입력 받은 위 42로 나눈 나머지 구하기
- 서로 다른 값이 몇 개 있는지 출력
'''

lst = []

for _ in range(10):
    x = int(input())
    lst.append(x % 42)

ans = []
for i in lst:
    if i not in ans:
        ans.append(i)

print(len(ans))
