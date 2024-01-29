letter = input()
alphabets = 'abcdefghijklmnopqrstuvwxyz'
cnt_list = []

cnt = 0
for alphabet in alphabets:
    cnt = letter.count(alphabet)
    cnt_list.append(cnt)
    cnt = 0

print(*cnt_list)