# 10988_팰린드롬인지 확인하기
'''
- 팰린드롬 : 앞으로 읽을 때와 거꾸로 읽을 때 똑같은 단어
- 팰린드롬이면 1, 아니면 0 출력
'''

word = list(input())

if word == list(reversed(word)):
    print(1)
else:
    print(0)
