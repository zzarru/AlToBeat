# 10798_세로읽기
'''
- 5줄의 입력이 주어질 때 세로로 읽은 순서 대로 빈 칸 없이 출력
- 각 줄에 최대 15개의 글자들이 주어짐
'''

lst = [input() for _ in range(5)]

for i in range(15):
    for j in range(5):
        # 문자열의 길이(최대 15글자)보다 열의 index가 작을 때
        if i < len(lst[j]):
            print(lst[j][i], end='')