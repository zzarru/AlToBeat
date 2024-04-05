'''
어떤 숫자가 몇개나 이용되는지 num_list 리스트에 입력해주고, 6과 9는 서로 바꿔쓸 수 있기때문에 평균을 내서 마지막에 정정해준다.
'''

N = input()
num_list = [0 for i in range(10)]
for num in N:
    num_list[int(num)] += 1
num_list[6] = (num_list[6] + num_list[9] + 1) // 2
num_list[9] = num_list[6]

answer = max(num_list)
print(answer)