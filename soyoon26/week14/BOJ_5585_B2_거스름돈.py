price = 1000-int(input())
coins = [500,100,50,10,5,1]
ans=0
for i in coins:
    ans+=price//i
    price = price % i

print(ans)