import sys
while True:
    n,m = map(int,sys.stdin.readline().split())
    if n==0 and m==0:
        break
    sg = list(int(sys.stdin.readline().rstrip()) for _ in range(n))
    sy = list(int(sys.stdin.readline().rstrip()) for _ in range(m))
    gs, ys = 0,0
    cnt = 0

    while gs < n and gs < m:
        if sg[gs] == sy[ys]: # 값이 같으면 다음 값을 비교
            cnt+=1
            ys += 1
            gs += 1
        elif sg[gs] > sy[ys]:
            ys+=1
        elif sy[ys] > sg[gs]:
            gs+=1
    print(cnt)