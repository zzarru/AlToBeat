'''
로프는 각자 자신의 최대하중만큼만 견딜 수 있다.
그러니 로프들을 내림차순 정리해서 해당 갯수만큼 곱한게 답들이 될 수 있다.
'''

N = int(input())
rope_list = []
answer_list = []
for _ in range(N):
    rope = int(input())
    rope_list.append(rope)
rope_list.sort(reverse=True)

for i in range(N):
    answer_list.append(rope_list[i] * (i+1))
answer = max(answer_list)

print(answer)