A = int(input())
B = input() #각 자릿수를 순회하기 위해서 str으로 입력 받는다.

for b in B[::-1]: # [::-1] 인덱스를 사용하면 문자열을 뒤에서부터 조회 가능하다.
    num = int(b)
    print(num*A)

print(A*int(B))