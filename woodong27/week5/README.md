# week5(DP)

## Dynamic Programming(DP)

반복되는 계산이 필요한 경우 이전에 진행했던 연산의 결과를 기록해두고 다시 사용함으로써 메모리와 시간을 절약할 수 있다.

```markdown
1. 최적 부분 구조
   큰 문제를 작은 문제로 나눌 수 있고, 작은 문제의 답을 모아서 큰 문제를 해결할 수 있다.

2. 중복 부분 문제
   동일한 작은 문제를 반복적으로 해결하는 경우에 사용한다.
```

DP의 대표적인 예시로 피보나치 수열의 구현이 있다.

```python
# 재귀함수로 구현
def fibo(n):
    if n >= 2:
        return fibo(n-1) + fibo(n-2)
    else:
        return fibo(n)
```

n이 5일 경우 총 15번의 연산을 하게되고, n이 커질수록 더 많은 연산이 필요하게 된다.

-> 필요한 시간과 메모리가 급격하게 증가한다.

DP의 기법 중 하나인 Memoization을 사용해서 해결하면 많은 자원을 아낄 수 있다.

" Memoization : 한 번 구한 결과를 기록해두고, 같은 연산이 필요한 경우 기록된 결과를 사용한다.

```python
# Dynamic Programming(DP로 구현)
fibo = [0] * (n + 1)

fibo[1] = 1
fibo[2] = 1

for i in range(1, n + 1):
    fibo[i] = fibo[i-1] + fibo[i-2]
```
