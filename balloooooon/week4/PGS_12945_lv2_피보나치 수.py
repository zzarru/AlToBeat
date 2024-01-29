
# def solution(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     elif n > 1:
#         return (solution(n - 1) + solution(n - 2)) % 1234567

# 위처럼 풀이를 했다가 100이상의 자연수에 엄청많은 양의 재귀가 걸려
# 런타임에러가 뜬다

def solution(n):
    list = [i for i in range(n+1)]
    if n>2:
        k=1
        while k < n:
            k += 1
            list[k] = (list[k-1] + list[k-2]) % 1234567
            # print('k는',k,list[k],list[k-1],list[k-2])
    return list[n]

# 옛날에 배운 기억이 나서 어설프게 만들어 보았는데, list memorization인가 하는
# 리스트에 값을 넣어두고 재귀하는 것처럼 만드는 것이다
# 이렇게 하니 해결되었다.

# 메모이제이션은 자꾸만 반복되지만 그 결과값은 변하지 않는 작은 문제들의 결과값을 저장하는 것을 의미한다. 
# 메모이제이션을 통해 이미 결과값이 기록되는 특정 문제가 반복할 때, 불필요한 계산은 패스하고 
# 기록되어 있는 값만 불러오면 아주 빠르게 해결할 수 있다. 재귀함수 또한 큰 문제를 해결하기 위해 
# 탈출 조건을 만날 때까지 작은 문제들을 풀어나가야 하고, 그 과정 중에 반복되는 작은 문제들이 있을 수 있다.