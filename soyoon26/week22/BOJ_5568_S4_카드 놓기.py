import sys
n = int(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline().rstrip())
nums = [sys.stdin.readline().rstrip() for _ in range(n)]
check = [False]*n
answer=set()
ans = []
def back():
    if len(ans) == k:
        answer.add(''.join(ans))
        return
    for i in range(n):
        if check[i] == False:
            ans.append(nums[i])
            check[i] = True
            back()
            ans.pop()
            check[i] = False
back()
print(len(answer))