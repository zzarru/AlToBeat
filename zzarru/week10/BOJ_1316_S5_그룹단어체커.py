N = int(input())
cnt = N
for _ in range(N):
    letter = input()
    alphabets = []
    checker = ''
    for l in letter:
        if l not in alphabets:
            alphabets.append(l)
            checker = l
        else: # 배열 안에 알파벳이 들어있다면
            if checker == l:
                continue
            else:
                cnt -= 1
                break

print(cnt)