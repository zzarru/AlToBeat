'''
마지막까지 다 확인했는지 확실히 확인하고자 입력받은 문자열에 .을 추가해주었다. 어차피 저 .을 통해
계속 갱신하는거라 나중엔 저 점이 안들어가도록 덜 출력하면된다.
'''

word = list(input())
word.append('.')
answer = []
cnt = 0
length = len(word)

for i in range(length):
    if word[i] == '.' or i == length - 1 :
        if cnt % 2:
            answer = -1
            break
        else:
            answer.append('AAAA' * (cnt // 4) )
            if cnt % 4:
                answer.append('BB')
        answer.append('.')
        cnt = 0
    else:
        cnt += 1

if answer != -1:
    print(*answer[:-1], sep='')
else:
    print(answer)

