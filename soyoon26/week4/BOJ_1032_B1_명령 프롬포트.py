N=int(input())
name=[input() for _ in range(N)]
answer=''

for i in range(len(name[0])):
    for j in range(N):
        letter=name[0][i]
        if letter==name[j][i]:
            if j == N-1:
                answer+=name[0][i]
        else:
            answer+='?'
            break
print(answer)
