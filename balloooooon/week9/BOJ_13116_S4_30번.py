graph = [ [] for i in range(1024)]
n = 1023
for i in range(1,511+1):
    graph[i].append(2*i)
    graph[i].append(2*i + 1)

parent = [0] * (n+1) #해당 인덱스에 대한 value값으로 부모를 저장한다.
d = [0] * (n+1)
visited = [0] * (n+1)

'''
dfs에서는 재귀할때 인자로 다음노드와 깊이를 넘겨준다.
방문처리는 재귀한 함수 시작할때 처리해준다.
'''
def dfs(cur, depth):
    visited[cur] = True
    d[cur] = depth
    for nxt in graph[cur]:
        if not visited[nxt]:
            parent[nxt] = cur
            dfs(nxt, depth + 1)


'''
최소 공통 조상 찾기 알고리즘이 좀 흥미로웠다.
두개의 while문을 통해서 검증한다.
첫번쨰 while문을 통해 깊이를 통일하고, 통일되면
두번째 while문에서 공통 조상인지 확인해본다. 여기서 공통조상이 아니라면
첫번째 while에서 깊이가 통일 되서 내려왔기때문에 '둘 다 동시에 깊이를 높인다.'
그리고 다시 두번째 while에서 동일하게 조상찾기를 반복한다.
'''
def lca(a,b):
    while d[a] != d[b]:
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]
    while a != b:
        a = parent[a] # 둘 다 동시에
        b = parent[b] # 깊이를 올리는 대목
    return a

dfs(1,0)

for _ in range(int(input())):
    a, b = map(int,input().split())
    print(lca(a,b) * 10)
