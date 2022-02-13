import sys
sys.stdin = open('input.txt')


def inorder_tree(cur_node):
    if not tree[cur_node]:
        return int(values[cur_node])
    left = inorder_tree(tree[cur_node][0])
    right = inorder_tree(tree[cur_node][1])
    if values[cur_node] == '-':
        return left - right
    elif values[cur_node] == '+':
        return left + right
    elif values[cur_node] == '*':
        return left * right
    else:
        return left / right


for test in range(1, 11):
    N = int(input())
    tree = {i: [] for i in range(1, N+1)}
    values = {i: '' for i in range(1, N+1)}
    for _ in range(N):
        data = input().split()
        values[int(data[0])] = data[1]
        if len(data) == 3:
            tree[int(data[0])] += [int(data[2])]
        elif len(data) == 4:
            tree[int(data[0])] += [int(data[2])]
            tree[int(data[0])] += [int(data[3])]

    answer = int(inorder_tree(1))
    print(f'#{test} {answer}')