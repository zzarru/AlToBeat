N = int(input())
letters = input()

# 알파벳에 고유한 번호가 있으므로 인덱스를 통해서 매칭해준다.
alphabets = '0abcdefghijklmnopqrstuvwxyz'

ans = 0
location = 0 #인덱스의 번호만큼 제곱한다.
for letter in letters:
    idx = alphabets.index(letter)
    ans += idx * 31**location
    location += 1


print(ans % 1234567891)