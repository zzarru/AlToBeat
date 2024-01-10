N = int(input())
num_lst = [0]*N
for i in range(N):
    A,B = map(int,input().split())
    num_lst[i]=[A,B]

num_lst.sort()
for i in range(N):
    print(num_lst[i][0],num_lst[i][1])