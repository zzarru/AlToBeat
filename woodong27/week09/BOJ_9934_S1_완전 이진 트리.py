# BOJ 9934 S1 완전 이진 트리

"""
들어오는 입력은 완전 이진 트리의 중위 손회 결과이기 때문에
쉽게 완전 이진트리를 만들 수 있다.

문제는 출력인데...
어떻게 출력할 지 생각하는게 오래걸렸다.
"""

k = int(input())
inorder = list(map(int, input().split()))
tree = [0] * (2 ** k)


def make_tree(arr, idx):
    mid = (len(arr) // 2)
    tree[idx] = arr[mid]
    if len(arr) == 1:
        return
    make_tree(arr[:mid], idx * 2)
    make_tree(arr[mid+1:], idx * 2 + 1)


make_tree(inorder, 1)

i = 1
while True:
    if i >= 2 ** k:
        break
    for j in range(i, i * 2):
        print(tree[j], end=' ')
    print()
    i *= 2
