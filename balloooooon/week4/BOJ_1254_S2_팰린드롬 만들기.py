str = input()
answer = 0
for i in range(len(str) + 1): # 최악의 경우의 수(단어전체)까지 확인해야하므로 마지막 인덱스를 위한 +1
    # 앞으로 읽어도 거꾸로 읽어도 우영우
    # 거꾸로 해도 원본과 같아야하므로 이를 만족시키는 최소한의 길이가 되려면
    # 첫번째 문자까지 거꾸로 해서 맨뒤에 붙여서 확인
    # 두번째 문자까지 거꾸로 해서 맨뒤에 붙여서 확인
    # 그렇게 최악의 경우까지 확인하는 도중 확인하면 바로 break

    new_str = str + str[:i][::-1] # i번째 문자까지 거꾸로 해서 맨뒤에 붙이기
    if new_str == new_str[::-1]: # 펠린드롬이 되는지 확인
        answer = len(new_str)
        break
print(answer)