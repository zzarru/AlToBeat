# BOJ 16472 G4 고냥이

"""
이전에 풀었던 투포인터 문제들이랑 비슷하지만 약간 더 까다로웠다.
alphabet_dict의 key의 종류가 n보다 커질 경우를 고려해서
while문이 종료되는 조건을 두가지로 설정하였다.
"""

n = int(input())
string = input()
length = len(string)

end, answer = 0, 0
alphabet_dict = {}
for start in range(length):
    while end < length:
        if len(alphabet_dict.keys()) > n:
            break

        if string[end] not in alphabet_dict.keys():
            if len(alphabet_dict.keys()) == n:
                break
            else:
                alphabet_dict[string[end]] = 1
        else:
            alphabet_dict[string[end]] += 1
        end += 1
        answer = max(answer, end - start)

    alphabet_dict[string[start]] -= 1
    if not alphabet_dict[string[start]]:
        alphabet_dict.pop(string[start])

print(answer)
