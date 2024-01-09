N, K = map(int,input().split())
num_list = [i for i in range(1,N + 1)] 
visited = [0 for i in range(N)]
credit = 0 # K번째의 수를 판별할 변수
exit_count = 0 # 요세푸스 순열을 전부 만들었을때 반복문을 탈출하기위한 변수
n = 0 # 누적순서
answer = []

while exit_count<N:
    current_order = n%N # 원순열이라서 현재 몇번째 순서인지 판별
    if not visited[current_order]: # 해당 원순열을 방문하지 않았다면
        credit += 1 
        n += 1 # 누적순서를 올린다
        if credit == K: #만일 K번째의 수라면
            # print(num_list[current_order])
            exit_count += 1 #요세푸스 순열에 숫자를 넣었다는 판정
            visited[current_order] = 1 #해당 숫자는 사용되었다는 방문표시
            answer.append(num_list[current_order]) #요세푸스 순열에 넣기
            credit = 0 #K번째 수 판독 초기화
    else: #만일 해당 원순열을 방문했다면
        n += 1 #누적순서만 늘린다
print(str(answer).replace('[', '<').replace(']', '>')) # 어쩐지 반례다 맞는데 틀리다고 하더라 ㅡㅡ