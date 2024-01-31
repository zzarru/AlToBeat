# 1159_농구 경기
'''
- 선수들의 성의 첫 글자가 같은 선수 5명을 선발
- 5명보다 적으면 기권 "PREDAJA" 출력
- 선발할 수 있는 경우 성의 첫 글자를 사전순으로 공백 없이 출력
'''

alphabet = ['a', 'b', 'c', 'd', 'e',
            'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']

lst = [0 for _ in range(26)]
N = int(input())

for i in range(N):
    name = input()
    for j in range(26):
        if name[0] == alphabet[j]:
            lst[j] += 1

ans = []
for x in range(26):
    if lst[x] >= 5:
        ans.append(alphabet[x])

if len(ans) > 0:
    print(*ans, sep='')
else:
    print("PREDAJA")
