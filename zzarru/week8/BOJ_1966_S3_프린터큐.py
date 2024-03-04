T = int(input())
for _ in range(T):
    n, idx = map(int, input().split())
    queue = []
    index = 0
    for num in list(map(int, input().split())):
        queue.append((index, num))
        index += 1

    cnt = 0
    mx = max(queue, key=lambda x: x[1])  # 큐에서 가장 큰 값을 찾는다
    while len(queue) != 0:
        front = queue[0] # 큐에서 가장 앞에 있는 거
        if front[1] == mx[1]:
            if front[0] == idx:
                cnt += 1
                print(cnt)
                break
            else:
                queue.pop(0)
                mx = max(queue, key=lambda x: x[1])
                cnt += 1
        else:
            queue.append(front)
            queue.pop(0)
