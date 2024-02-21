import sys
n = int(sys.stdin.readline().rstrip())

stack = []
out = []
ans = []
current = 1 # 시간초과를 해결하기 위해서

for _ in range(n):
    number = int(sys.stdin.readline().rstrip())

    while current <= number:
        stack.append(current)
        ans.append('+')
        current += 1

    if stack[-1] == number:
        stack.pop()
        ans.append('-')
    else:
        print('NO')
        sys.exit(0)

for a in ans:
    print(a)


# import sys
#
# n = int(sys.stdin.readline().rstrip())
#
# stack = []
# out = []
# ans = []
# for _ in range(n):
#     number = int(sys.stdin.readline().rstrip())
#     for i in range(1, number+1):
#         if i not in stack and i not in out:
#             stack.append(i)
#             ans.append('+')
#
#     lotto = stack.pop()
#     if lotto == number:
#         out.append(lotto)
#         ans.append('-')
#     else:
#         stack.append(lotto)
#
# if not stack:
#     for a in ans:
#         print(a)
# else:
#     print('NO')