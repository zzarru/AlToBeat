'''
이렇게 보면 그저 조합이나 다름없는 알고리즘이다 다음 두포인터는
더 스마트하게 풀어야겠다.
'''

N = int(input())
goal = int(input())
materials = list(map(int,input().split()))

start = 0
end = 1
last = len(materials)-1
answer = 0

while start != last: 

    if materials[start] + materials[end] == goal :
        answer += 1
        end += 1

    if end < last:
        end += 1

    else:
        start += 1
        end = start + 1

print(answer)
