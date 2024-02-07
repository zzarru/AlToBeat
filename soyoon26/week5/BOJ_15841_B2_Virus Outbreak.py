cnt=[0,1]+[0]*489
for i in range(2,491):
    cnt[i]=cnt[i-1]+cnt[i-2]
while True:
    num=int(input())
    if num == -1:
        break
    else:
        print(f'Hour {num}: {cnt[num]} cow(s) affected')


