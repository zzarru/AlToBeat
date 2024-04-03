import sys
n = int(sys.stdin.readline().rstrip())
answer=0
for _ in range(n):
    word=sys.stdin.readline().rstrip()
    cnt=0
    for i in range(1,len(word)):
        if word[i-1] != word[i]:
            cnt+=1
    if cnt+1 == len(set(word)):
        answer+=1
print(answer)