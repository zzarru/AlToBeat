import sys
n=int(sys.stdin.readline().rstrip())
cnt=0
def isPalindrome(start,end,word):
    global cnt
    if start<end:
        cnt+=1
        if word[start] == word[end]:
            isPalindrome(start+1,end-1,word)
        else:
            print(0,cnt)
            cnt=0
            return 0,cnt
    else:
        print(1,cnt+1)
        cnt=0
        return 1,cnt
for i in range(n):
    word=sys.stdin.readline().rstrip()
    isPalindrome(0,len(word)-1,word)