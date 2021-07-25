import sys
input = sys.stdin.readline


# 중위순회는 왼쪽 탐색, 본인 출력, 오른쪽 탐색(왼쪽에 더이상 갈 일이 없는 노드부터 same_level트리에 들어가게 됨(num은 가로 index))
def inorder(root, level):
    global num
    if tree[root][0] != -1:
        inorder(tree[root][0], level + 1)
    same_level[level].append(num)
    num += 1
    if tree[root][1] != -1:
        inorder(tree[root][1], level + 1)



n = int(input())
tree = [[0] * 2 for _ in range(n + 1)]
node = [0 for _ in range(n + 1)]
same_level = [[] for _ in range(n + 1)]
num = 1

# 삽입하고 존재하는 노드는 1표시.
for i in range(n):
    root, left, right = map(int, input().split())
    tree[root][0] = left
    tree[root][1] = right
    node[root] += 1
    if left != -1:
        node[left] += 1
    if right != -1:
        node[right] += 1
for i in range(1, n + 1):
    if node[i] == 1:
        root = i

# 입력한 tree에 대해 중위순회 실시(루트, 레벨 1부터.)
inorder(root, 1)

# result에 1열부터 끝 level까지 모든 가로값에 대해 비교 후 최종결정.(가로길이와 레벨 저장.)
result = max(same_level[1]) - min(same_level[1]) + 1
level = 1
for i in range(2, n + 1):
    if same_level[i]:
        if result < max(same_level[i]) - min(same_level[i]) + 1:
            result = max(same_level[i]) - min(same_level[i]) + 1
            level = i
print(level, result)