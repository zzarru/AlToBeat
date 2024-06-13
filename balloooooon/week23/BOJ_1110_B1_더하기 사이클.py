avc=int(input())
def f(a):
    b=0
    if a<10:
        a=a*10
    count_0=1
    k=a
    while k!=b:
        
        
        b=(a//10+a%10)%10+(a%10)*10
        c=b
        a=c
        if k!=b:
            count_0 +=1
        else:
            break
    return count_0

print(f(avc),end='')