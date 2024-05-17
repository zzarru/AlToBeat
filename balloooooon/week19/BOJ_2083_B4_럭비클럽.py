while 1:
    info = list(input().split())
    if int(info[2]):
        if int(info[1]) > 17 or int(info[2]) >= 80:

            print(info[0],'Senior')
        else:
            print(info[0],'Junior')
    else:
        break
