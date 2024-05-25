m, n = map(int,input().split())
graph = [ list(map(int,input().split())) for _ in range(m)]
T = int(input())
di = [0,1,1,1,0,-1,-1,-1]
dj = [-1,-1,0,1,1,1,0,-1]
answer = 0
num_list = []
for i in range(1,m-1):
    for j in range(1,n-1):
        temp = [graph[i][j]]
        for k in range(8):
            ni = i + di[k]
            nj = j + dj[k]
            temp.append(graph[ni][nj])
        temp.sort()
        num_list.append(temp[4])
for num in num_list:
    if T <= num:
        answer += 1
print(answer)