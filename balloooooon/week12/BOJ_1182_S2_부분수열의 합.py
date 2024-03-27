'''
모든 경우의 수를 체크하는 부분수열의 합으로
단순히 첫번쨰 원소부터 넣을까 말까?를 마지막 원소까지 모두해보는
친절한 완전탐색문제였다. 나중에는 비트연산자를 써보는것도 괜찮을 듯 하다.
여기서 문제는 만일 원소가 하나라면 내가 만든 조건문에서 오류가 날 수 있으므로
해당 조건만 N>1 이라는 조건으로 수정해주었다.
'''

N, S = map(int,input().split())
num_list = list(map(int,input().split()))
answer_list = [0,num_list[0]]
start = 1

while N>1:
    temp = []
    for num in answer_list:
        temp.append(num)
        temp.append(num + num_list[start])
    start += 1
    answer_list = temp
    if start == N:
        break

answer_list.pop(0)

answer = answer_list.count(S)
print(answer)