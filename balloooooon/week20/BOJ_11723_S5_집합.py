import sys
input = sys.stdin.readline
N = int(input().rstrip())
S = set()

def remove(S,num):
    if num in S:
        S.discard(num)
def add(S,num):
    S.add(num)
def check(S,num):
    if num in S:
        print(1)
    else:
        print(0)

def toggle(S,num):
    if num in S:
        S.discard(num)
    else:
        S.add(num)

functions = {'remove' : remove , 'add' : add, 'toggle': toggle, 'check': check}
for _ in range(N):
    str = list(input().rstrip().split())
    order = str[0]
    if order == 'all':
        S = set(i for i in range(1,21))
    elif order == 'empty':
        S = set()
    else:
        num = int(str[1])
        func = functions[order]
        func(S,num)
