'''
1) 재귀를 사용하니 n=50 이상이 되었을 때 런타임에러가 발생하였다.
2) for문을 통해서 문제를 다시 풀었다.
3) 리스트의 idx를 통해 피보나치 수열을 저장하고 값을 구했다.
'''
def solution(n):
    fibo = [0, 1]
    for i in range(n+1):
        if i == 0 or i ==1:
            pass
        else:
            fibo.append(fibo[i-1]+fibo[i-2])
    answer = fibo[n] % 1234567
    return answer