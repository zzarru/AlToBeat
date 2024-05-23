N = list(map(int,input()))
if len(N) == 1:
    N = int(N[0])
    if N%3:
        print(0)
        print('NO')
    else:
        print(0)
        print('YES')
else:
    N = sum(N)
    answer = 1
    num_list = [1, 2, 4, 5, 7, 8]
    if N in num_list:
        print(answer)
        print('NO')
    elif N in [3,6,9]:
        print(answer)
        print('YES')
    else:
        while 1:
            N = list(map(int,str(N)))
            N = sum(N)
            answer += 1
            if N in [3,6,9]:
                print(answer)
                print('YES')
                break
            elif N in num_list:
                print(answer)
                print('NO')
                break
            else:
                continue