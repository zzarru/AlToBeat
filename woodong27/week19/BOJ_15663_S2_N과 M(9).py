# BOJ 15663 S2 N과 M(9)

"""
used체크를 할 때 list로 하는것 보다 set으로 하는게 검색 속도가 더 빠르다.
set는 해시테이블이라 O(1)이지만 list는 O(n)의 시간이 걸린다.
set의 원소로는 불변 타입만 넣을 수 있어서 list_를 tuple로 타입변경해서 넣어줘야 한다.
"""


def backtracking(list_):
    if len(list_) == m:
        temp = tuple(list_)
        if temp not in used:
            used.add(temp)
            print(*list_)
        return

    for j in range(n):
        if not visited[j]:
            visited[j] = 1
            backtracking(list_ + [numbers[j]])
            visited[j] = 0


if __name__ == '__main__':
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    numbers.sort()

    used = set()
    visited = [0] * n
    for i in range(n):
        visited[i] = 1
        backtracking([numbers[i]])
        visited[i] = 0
