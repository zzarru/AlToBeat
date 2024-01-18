# 마지막 행은 0이다.
while True:
    N = int(input())
    if N == 0:
        break

    else:
        nums = str(N)
        length = len(nums) # int를 str으로 바꾸어 길이를 구한다.

        a = ''
        b = ''
        for i in range(length//2+1):
            j = i + 1
            a += nums[i]
            b += nums[-j] # 인덱스 뒤에서부터 슬라이싱

        if a == b: # 비교해서 같으면 yes
            print('yes')
        else: # 다르면 no 출력
            print('no')

