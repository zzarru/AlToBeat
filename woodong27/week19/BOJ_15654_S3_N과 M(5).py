# BOJ 15654 S3 N과 M(5)

"""
간단한 백트래킹 문제
길이가 m인 수열이 되면 출력하면 된다.
사전 순으로 출력해야하기 때문에 numbers를 정렬하고 시작하면 된다.
"""


def backtracking(list_):
    if len(list_) == m:
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
    visited = [0] * n
    for i in range(n):
        visited[i] = 1
        backtracking([numbers[i]])
        visited[i] = 0
