# 해당 문제는 홀수번째와 짝수번째에 별을 찍는 걸 표현해줘야하는데
# 난 리스트를 만들어서 각 조건에 충족되는 리스트를 넣어주었다.
# sep을 사용하면 print에서 띄어쓰여진 곳에 원하는 문자를 넣을 수 있고
# end를 사용하면 print는 마지막에 개행을 하는데 문제에서 원하는
# 출력을 내기위해선 개행을 삭제해주어야해서 end에 ''와 같은 빈칸을 사용하면
# 개행을 막을 수 있다.

N = int(input())
if N != 1:
    list1 = ['0' for i in range(N)]
    list2 = ['0' for i in range(N)]

    for i in range(N):
        if i%2:
            list1[i] = '*'
            list2[i] = ' '
        else:
            list1[i] = ' '
            list2[i] = '*'

    for i in range(N):
        if i == N-1:
            print(*list2, sep = '')
            print(*list1, sep = '', end ='')
        else:
            print(*list2, sep='')
            print(*list1, sep='')
else:
    print("*" , end = '')

