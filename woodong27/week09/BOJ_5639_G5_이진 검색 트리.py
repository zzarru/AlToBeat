# BOJ 5639 G5 이진 검색 트리

"""
전위순회 결과 중 첫번째 노드는 루트이고
루트보다 작은 노드들은 왼쪽 자식, 큰 노드들은 오른쪽 자식이다.
왼쪽/오른쪽 자식을 계속 분할해가며 재귀를 반복하다가
길이가 1이 되면 리프노드에 도착한 것이기 때문에 출력해주면 된다.
"""


preorder = []
while True:
    try:
        preorder.append(int(input()))
    except:
        break


def postorder(nodes):
    if not nodes:
        return
    if len(nodes) == 1:
        print(nodes[0])
        return

    left, right = [], []
    root = nodes[0]
    for node in nodes[1:]:
        if node < root:
            left.append(node)
        else:
            right.append(node)

    postorder(left)
    postorder(right)
    print(root)


postorder(preorder)
