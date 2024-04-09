# BOJ 1339 G4 단어 수학

"""
각 단어의 알파벳들을 자리수에 맞게 계산해서 모두 더한다.
더한 결과를 크기 순으로 내림차순 정렬하고,
가장 큰 수부터 9 ~ 1 까지 곱해주면 된다.
"""

n = int(input())
words = [input() for _ in range(n)]

alphabets = {}
for word in words:
    power = len(word) - 1
    for letter in word:
        if letter in alphabets.keys():
            alphabets[letter] += 10 ** power
        else:
            alphabets[letter] = 10 ** power
        power -= 1

results = list(alphabets.values())
results.sort(reverse=True)
start = 9
answer = 0
for result in results:
    answer += result * start
    start -= 1

print(answer)
