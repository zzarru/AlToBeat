# BOJ 9935 G4 문자열 폭발

"""
처음에 문자열의 replace메서드와 not in을 사용해서
while 반복문을 돌렸지만, 시간초과가 발생했다.

해결
알고리즘 분류에 스택이 있는 것을 보고 스택을 활용했다.
"""

import sys

letters = sys.stdin.readline().strip()
bomb = sys.stdin.readline().strip()

# 문자들을 하나씩 넣어줄 스택
result = []
len_bomb = len(bomb)
# 한 글자씩 스택에 넣으면서, 들어온 글자들이 bomb과 동일한지 검사한다.
# bomb과 동일할 경우 pop을 통해서 해당 글자들을 제거해준다.
for letter in letters:
    result.append(letter)
    if ''.join(result[-len_bomb:]) == bomb:
        for _ in range(len_bomb):
            result.pop()

answer = ''.join(result) if result else 'FRULA'
print(answer)
