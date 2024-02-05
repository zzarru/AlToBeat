num_list = [ 99999 for i in range(1000000+1)]
num_list[1] = 0
n = 1000000

N = int(input())

for i in range(1,n):
    num_list[i+1] = min(num_list[i+1], num_list[i]+1) # 1을 더하는 행위
    if 2*i <= n:
        num_list[2*i] = min(num_list[2*i], num_list[i]+1) # 2를 곱하는 행위
    if 3*i <= n: 
        num_list[3*i] = min(num_list[3*i], num_list[i]+1) # 3을 곱하는 행위
# 해당 인덱스를 그 숫자로, 인덱스에 있는 값은 해당 숫자까지 가는 카운트로 넣어두었다.
# 최소횟수는 최소횟수에 기인하므로, 해당 숫자까지 도달하는 3가지방법을 사용함과 동시에 계속해서
# 횟수를 최솟값으로 갱신해준다.
# 문제에서는 2,3 으로 나누기 1빼기로 했지만 나는 반대로 접근했다
print(num_list[N])