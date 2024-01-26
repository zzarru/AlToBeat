def solution(num_list, n):
    answer = []
    maxLange = len(num_list)
    for i in range(maxLange):
        if not i%n: ## 해당 간격의 특정값은 나머지정리로 찾는다. 조건만족을 위해서 not을 이용해 truthy하게 만든다.
            answer.append(num_list[i])
        
    return answer