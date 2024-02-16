N, X = map(int,input().split())
visited = [False for i in range(100000+1)]

'''
각 경우를 탐색하여 탐색한 기록이 있다면 그것이 가장 빠른 도달 방법이므로
해당 분기는 더이상 탐색할 필요가 없으므로 쳐낸다.
이를 위해 100,000까지의 배열을 준비해놓고 거기서 지지고 볶고 할 수 있도록 해주자
'''


queue = [N]
visited[N] = 1
while queue:
    cur = queue.pop(0)
    if cur == X:
        print(visited[cur]-1)
        break

    if 0<=cur-1 and not visited[cur-1]:
        visited[cur-1] = visited[cur]+1
        queue.append(cur-1)

    if cur+1<100001 and not visited[cur + 1]:
        visited[cur+1] = visited[cur]+1
        queue.append(cur+1)

    if cur*2 < 100001 and not visited[2*cur]:
        visited[2*cur] = visited[cur]+1
        queue.append(2*cur)
