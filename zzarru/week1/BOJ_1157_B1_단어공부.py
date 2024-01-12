'''
1) 각 문자열에 쓰인 알파벳을 담은 배열을 만든다. ex) ['m', 'i', 's', 'i']
2) 각 알파벳의 개수를 셀 배열을 만든다. ex) [0, 0, 0, 0]
3) cnt 함수를 통해서 각 알파벳과 해당하는 인덱스의 배열에 개수를 입력해준다.
4) max 값의 인덱스를 통해 가장 많은 알파벳을 출력한다.
'''

letter = input().upper()
alphs = []
cnts = []

for alph in letter:
    if alph not in alphs:
        alphs.append(alph)
        cnt = letter.count(alph)
        cnts.append(cnt)

# 가장 개수가 많은 알파벳 찾기
max_cnt = max(cnts)
if cnts.count(max_cnt) > 1:
    print('?')
else:
    idx = cnts.index(max_cnt)
    print(alphs[idx])