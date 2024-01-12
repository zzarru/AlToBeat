# 이 문제는 sequence라는 리스트에서 연속된 수열(말 그대로 연속된 숫자의 집합인데, 수열이라고 표기해놓음 ㅡㅡ)중 해당 수열들의 합은 k가 되어야하고
# 그 중 가장 길이가 짧은 수열을 찾아내야한다. 그중에서는 단일로 될 수도 있다. 예전에 설명을 들은 적이 있지만, 나 스스로 구현해본적은 없었기에
# 문제 접근은 수월했지만 구현에 애를 먹었다.
# 연속된 부분 수열은 한마디로 정리하면 '지렁이'라고 쓸 수 있겠다. 리스트의 특정 시작지점과 끝지점을 계속해서 초기화하면서
# 지렁이가 꿈틀거리듯이 리스트를 훑으며 문제를 만족하는 수열을 찾아낸다.
# 구현에 애를 먹은 것은 언제나 그렇듯, 경곗값이 가장 속을 썩였다.
# while 조건문에 이상치를 쳐내려고 조건문을 썼지만 그렇게해선 잡히지 않았다. 왜냐면 로직에서 내가 원하는 정보를 뽑아내려면
# 저렇게 지저분하게 조건문이 주어지게 되는데 while 조건문에 넣어봤자 저 로직이 돌아가기 떄문에
# 여튼 각 if에서 마지막에 엉뚱한 이상치로 다시 while문을 돌리지 못하게 조건문을 걸어둠으로써 해결됐다.
# 지렁이처럼 움직이는걸 구현하는게 나는 너무 어려웠다.
def solution(sequence, k):
    start, end = -1, -1
    temp = [] # 시작위치, 끝위치, 길이, 합
    temp_sum = 0

    while start <= end:
        if temp_sum >= k:
            start += 1
            if temp_sum == k:
                temp.append([start, end, end - start , temp_sum])

            if start <= len(sequence)-1:
                temp_sum -= sequence[start]
            else:
                break

        else:
            end += 1
            if temp_sum == k:
                temp.append([start, end, end-start, temp_sum])
            if end <= len(sequence)-1:
                temp_sum += sequence[end]
            else:
                break
    #     print(temp_sum,start, end)
    # print(temp)
    answer_list  = sorted(temp, key = lambda x : (x[2], x[0])) #문제에서 제시한대로(가장 짧고, 만일 길이가 같다면 시작지점이 앞에인것) 정렬시켜서
    answer = [answer_list[0][0],answer_list[0][1]] #답으로 도출
    return answer