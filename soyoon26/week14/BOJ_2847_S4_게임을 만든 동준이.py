import sys
n = int(sys.stdin.readline().rstrip())
score = list(int(sys.stdin.readline().rstrip()) for _ in range(n))
max = sum(score)
for i in range(n-2,-1,-1):
    if score[i] >= score[i+1]:
        score[i] = score[i]-(score[i] - score[i+1] +1)
print(max - sum(score))