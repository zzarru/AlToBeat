order=[]
length=[]
fruit=int(input())
for i in range(6):
    a,b=map(int,input().split())
    order.append(a)
    length.append((a,b))

while 1:
    if (order[0],order[3])==(order[4],order[5]): #예시의 순서가 북동남서북서 다른 모양의 형태도 이런꼴이 된다
                                                 #어떠한 꼭지점에서 이런 포멧을 만족시키기때문에 그렇게 되도록 리스트를 조정
        break
    else:
        order = [order.pop()] + order
        length = [length.pop()] + length

S=max(length[0][1]*length[1][1],length[1][1]*length[2][1],length[2][1]*length[3][1])-length[5][1]*length[4][1]
#넓이구하는 건 앞의 북동남서에서 북동 동남 남서를 골라 가장 큰게 전체 넓이
print(S*fruit)