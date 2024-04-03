'''
해당 행의 바로 전 행의 최댓값 (열이 같지 않은)을 더해서 내려온 뒤,
맨 마지막 행의 최댓값을 출력한다.
'''

def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            land[i][j] += max(land[i-1][k] for k in range(4) if k != j)
    
    return max(land[-1])