#내가 생각한 방법이 아니므로.. 다시 생각해서 풀어보는 걸로..

def solution(numbers, target) :
    tree = [0] # 초기 값
    for i in range(len(numbers)) :
        value = []
        for j in range(len(tree)) :
            value.append(tree[j] - numbers[i]) # 빼기
            value.append(tree[j] + numbers[i]) # 더하기

        tree = value

    answer = tree.count(target)

    return answer