N = int(input())
str_list = []
for i in range(N):
    str = input()
    str_list.append(str)

str_list = list(set(str_list)) # 중복제거
str_list.sort() # 단어길이에 상관없이 단순히 알파벳 순으로 정렬
# print(str_list)
str_list.sort(key=lambda x:len(x)) # 알파벳순으로 정렬된 순서를 그대로 이어서 단어의 길이순으로 정렬하면 두 조건다 만족된다.
# print(str_list)
for i in range(len(str_list)):
    print(str_list[i])