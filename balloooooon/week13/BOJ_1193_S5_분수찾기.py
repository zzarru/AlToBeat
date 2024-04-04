'''
수학이래서 수학적으로 접근해봤다.
'''

N = int(input())
n = 1
while 1:
    if n * (n+1) / 2 >= N:
        n = n - 1
        break
    n += 1

if n % 2 :
    end = n + 1
    start = 1
    credit = int(N - n * (n + 1) / 2) - 1
    end -= credit
    start += credit
else:
    start = n + 1
    end = 1
    credit =  int(N - n*(n+1) / 2) - 1
    start -= credit
    end += credit

print(start,'/',end, sep='')

