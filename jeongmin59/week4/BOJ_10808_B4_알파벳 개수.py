# 10808_알파벳 개수
'''
- 단어가 주어졌을 때, 단어에 포함되어 있는 a의 개수, b의 개수, ..., z의 개수를 공백으로 출력
- 단어의 길이는 100을 넘지 않으며, 소문자로 이루어짐
'''

alphabet = ['a', 'b', 'c', 'd', 'e',
            'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']

lst = [0 for _ in range(26)]

word = input()

for i in range(26):
    for j in range(len(word)):
        if word[j] == alphabet[i]:
            lst[i] += 1

print(*lst)