N = int(input())

for i in range(2*N-1):
    if i < N:
        stars = 2*i + 1

        print(' '*(N-i-1)+stars*'*'+ ' ')

    else:
        stars = 2*(2*N-i-1) - 1

        if stars != 1:
            print(' '*(i-N+1) + stars*'*' + ' ')
        else:
            print(' '*(i-N+1) + stars*'*')

