N = int(input())
if N>1:
    list = ['1' for i in range(N * 2)]
    k=0
    num = 2 * N
    for j in range(N):
        k += 1
        for i in range(num):
            if 0<=i<k:
                print('*', end = '')
            elif k <= i < num-k:
                print(' ', end = '')
            else:
                print('*', end ='')
        print()
    k=N
    for j in range(N,1,-1):
        k -= 1
        for i in range(num):
            if 0<=i<k:
                print('*', end = '')
            elif k <= i < num-k:
                print(' ', end = '')
            else:
                print('*', end ='')
        if j == 2:
            print(end='')
        else:
            print()
else:
    print("**")