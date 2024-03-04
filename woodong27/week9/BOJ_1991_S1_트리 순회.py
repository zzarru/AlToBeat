# BOJ 1991 S1 트리 순회

"""
그냥 전위/중위/후위 순회 구현하면 됨
재귀적으로 가장 마지막 노드를 찾아갈 수 있도록 재귀 함수로 구현
"""


# 전위 순회(루트 - 왼쪽 - 오른쪽)
def preorder(start):
    print(flipped_alphabet_dict[start], end='')
    if nodes[start][0] != '.':
        preorder(nodes[start][0])
    if nodes[start][1] != '.':
        preorder(nodes[start][1])


# 중위 순회(왼쪽 - 루트 - 오른쪽)
def inorder(start):
    if nodes[start][0] != '.':
        inorder(nodes[start][0])
    print(flipped_alphabet_dict[start], end='')
    if nodes[start][1] != '.':
        inorder(nodes[start][1])


# 후위 순회(왼쪽 - 오른쪽 - 루트)
def postorder(start):
    if nodes[start][0] != '.':
        postorder(nodes[start][0])
    if nodes[start][1] != '.':
        postorder(nodes[start][1])
    print(flipped_alphabet_dict[start], end='')


n = int(input())

alphabet_dict = {chr(i): i - ord('A') for i in range(ord('A'), ord('Z') + 1)}
flipped_alphabet_dict = {value: key for key, value in alphabet_dict.items()}

nodes = [[] for _ in range(n)]

for _ in range(n):
    parent_node, left_node, right_node = map(str, input().split())
    parent = alphabet_dict[parent_node]
    left = alphabet_dict[left_node] if left_node != '.' else left_node
    right = alphabet_dict[right_node] if right_node != '.' else right_node
    nodes[parent].append(left)
    nodes[parent].append(right)

preorder(0)
print()
inorder(0)
print()
postorder(0)
