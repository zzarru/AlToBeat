while 1:
    num_list = list(map(int,input().split()))
    if num_list[0]:
        n = num_list.pop(0)
        temp = []
        num_list.sort()
        visited = [0 for _ in range(n)]
        def lotto(lv,start):
            if lv == 6:
                print(*temp)
                return
            for i in range(start,n):
                if not visited[i] and start-1 < i:
                    temp.append(num_list[i])
                    visited[i] = True
                    lotto(lv+1,i + 1)
                    visited[i] = False
                    temp.pop()

        lotto(0,0)
        print()
    else:
        break
