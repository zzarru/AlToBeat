n, money = map(int,input().split())

coins = [ int(input()) for _ in range(n)]
coins.sort(reverse=1)

cur = 0
answer = 0
while money:
    temp = money - coins[cur]
    if temp < 0:
        cur += 1
    else:
        money = temp
        answer += 1
print(answer)