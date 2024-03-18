# BOJ 12904 G5 A와 B

"""
1. 문자열 뒤에 A를 추가한다.
2. 문자열을 뒤집고 B를 추가한다.
두가지 경우를 수행하는 메서드를 만들어서
bfs를 사용해서 가능한 결과들을 모두 검사했다.
-> 시간초과 발생

해결
굳이 bfs를 쓸 필요가 없었다.
s에서 t로 만들어가는게 아니라
t에서 s로 역순으로 진행하면 더 빠르게 해결할 수 있다.
t가 A로 끝나면 단순이 A를 제거만 하고
B로 끝나면 B를 제거하고 뒤집어 주다가
두개의 길이가 같아졌을 때 두개가 동일한지 확인하면 된다.
"""

s = input()
t = list(input())

answer = 0
while True:
    if t[-1] == 'A':
        t.pop()
    else:
        t.pop()
        t.reverse()

    if len(t) == len(s):
        if s == ''.join(t):
            answer = 1
        break

print(answer)
