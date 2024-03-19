# BOJ 1966 S3 프린터 큐

from collections import deque

"""
반복문으로 현재 중요도보다 더 중요도가 큰 문서가 하나라도 있으면
큐에서 뺀 값을 다시 넣어준다.
이전의 큐의 길이와 pop한 후의 길이를 비교해서
길이가 달라졌다면, 인쇄를 했기 때문에 count를 1 늘려준다.
"""

tc = int(input())

for _ in range(tc):
    n, m = map(int, input().split())
    papers = list(map(int, input().split()))
    papers = deque([[i, papers[i]] for i in range(n)])

    current_length = len(papers)
    answer = 0
    while papers:
        number, current = papers.popleft()
        for idx, paper in papers:
            if paper > current:
                papers.append([number, current])
                break

        if len(papers) != current_length:
            current_length = len(papers)
            answer += 1
            if number == m:
                break

    print(answer)
