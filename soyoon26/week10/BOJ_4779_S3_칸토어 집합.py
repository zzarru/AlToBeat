def ct(start, end, lst, list):
    m = (end - start) // 3
    if m == 1:
        for i in range(start + m, end - m):
            list[i] = ' '
        return m
    for i in range(start + m, end - m):
        list[i] = ' '
    ct(start, start + m, lst[:start + m], list)
    ct(end - m, end, lst[end - m:], list)
while True:
    try:
        n=int(input())
        lst = list('-' * (3 ** n))
        if n == 0:
            print('-')
        else:
            ct(0,len(lst),lst,lst)
            print(*lst,sep='',)
    except:
        break
