'''
'큰 가중치에는 큰 수가 따른다.'

각 단어들은 정직하게 일의 자리, 십의 자리, 백의 자리를 지키고 있기때문에
각 알파벳을 해당 자릿수로 곱해서 딕셔너리에 얼마나 쓰였는지 가중치로써 저장해둔다
모든 단어를 확인이후 딕셔너리에 해당 단어의 가중치를 내림차순으로 정리하고
9부터 0까지 가중치들을 곱해준다
'''

from collections import defaultdict

N=int(input())
word_dict = defaultdict(int)

for _ in range(N):
    word = input()
    word_length = len(word)
    for i in range(word_length):
        word_dict[word[i]] += 10 ** (word_length - 1 - i)

weight_list = list(word_dict.values())
weight_list.sort(reverse=True)

value = 9
answer = 0
for weight in weight_list:
    answer += weight * value
    value -= 1

print(answer)