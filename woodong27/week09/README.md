# Week9(Tree, 트리)

일반 배열은 데이터의 삽입, 삭제에 O(n)의 시간이 소요되지만, 트리에선 편향 트리가 아닌 이상 O(log N) 정도의 시간이 소요된다.

비선형 자료구조로 계층적인 관계를 가진다.

## Binary Tree(이진 트리)

모든 노드들이 최대 2개의 자식 노드를 가질 수 있는 트리

포화 이진 트리 : 모든 레벨의 노드가 가득 차 있는 트리

완전 이진 트리 : 마지막 노드 번호가 n일 때 n번 노드까지 비어있는 노드가 없는 트리

편향 이진 트리 : 한 쪽 방향으로만 자식을 가지는 트리(왼쪽 자식만 있거나 오른쪽 자식만 있거나)

이진트리의 문제점을 개선하여 활용하는 B Tree/B+ Tree 등도 존재한다.

### 이진 트리 순회

전위 순회(preorder) : 부모노드 방문 후 왼쪽 자식 노드, 오른쪽 자식 노드 순으로 방문

중위 순회(inorder) : 왼쪽 자식, 부모, 오른쪽 자식 순으로 방문

후위 순회(postorder) : 왼쪽 자식, 오른쪽 자식, 부모 노드 순으로 방문

```python
# 각 노드의 첫 번째 원소는 왼쪽 자식, 두 번째 원소는 오른쪽 자식
# 'x'는 해당 위치의 자식이 없음을 표시
tree = [[], [2, 'x'], ...]

# 전위 순회
def preorder(node):
    print(node)
    if tree[node][0] != 'x':
        preorder(tree[node][0])
    if tree[node][1] != 'x':
        preorder(tree[node][1])

# 중위 손회
def inorder(node):
    if tree[node][0] != 'x':
        inorder(tree[node][0])
    print(node)
    if tree[node][1] != 'x':
        inorder(tree[node][1])

# 후위 순회
def postorder(node):
    if tree[node][0] != 'x':
        postorder(tree[node][0])
    if tree[node][1] != 'x':
        postorder(tree[node][1])
    print(node)
```