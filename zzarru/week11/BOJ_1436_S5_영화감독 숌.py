N = int(input())
cnt = 0
dystopia = 666

while True:
    if '666' in str(dystopia):
        cnt += 1

    if N == cnt: # while문의 반복을 결정하는 조건
        break

    else:
        dystopia += 1

print(dystopia)