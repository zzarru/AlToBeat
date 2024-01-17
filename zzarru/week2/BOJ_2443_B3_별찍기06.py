N = int(input())

for i in range(N):
    stars = 2*N - (i*2+1)

    if stars != 1:
        print(' '*i + stars*'*'+ ' ')
    else:
        print(' '*i + stars*'*')