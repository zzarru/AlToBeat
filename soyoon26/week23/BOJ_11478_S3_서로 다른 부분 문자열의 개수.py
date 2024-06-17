import sys
word=sys.stdin.readline().rstrip()
check=set()
for i in range(len(word),-1,-1):
    for j in range(i):
        check.add(word[j:i])
print(len(check))