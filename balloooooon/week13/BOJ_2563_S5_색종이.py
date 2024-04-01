paper=[[0 for _ in range(100)] for _ in range(100)]

total=0
t=int(input())
for i in range(t):
    a,b= map(int,input().split())
    for i in range(10):
        for j in range(10):
            paper[100-a-i][100-b-j] = 1

for i in range(100):
    for j in range(100):
        total += paper[i][j]
print(total)