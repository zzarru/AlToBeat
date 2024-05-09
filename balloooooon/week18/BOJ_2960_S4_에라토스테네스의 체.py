N, K = map(int,input().split())

num_list = [i for i in range(2,N+1)]
cnt = 0
while num_list:
    start = num_list[0]
    for i in range(1,N//start +1):
        if start * i > N:
            continue
        if start * i in num_list:
            num_list.remove(start*i)
            cnt += 1
            if cnt == K:
                print(start * i)
                break

