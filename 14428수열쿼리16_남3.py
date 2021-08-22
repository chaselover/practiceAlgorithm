import sys

# limit for array size
N = 1000000

# Max size of tree
tree = [0] * (2 * N)
idxTree = [-1] * (2*N)

def build(arr):
    # insert leaf nodes in tree
    for i in range(n):
        tree[n + i] = arr[i]
        idxTree[n + i] = i

    # build the tree by calculating parents
    for i in range(n - 1, 0, -1):
        tree[i] = min(tree[i << 1], tree[i << 1 | 1])
        # print(f'tree[{i}] {tree[i]} =  i << 1-> {i << 1} * i << 1 | 1 ->{i << 1 | 1}')
        if tree[i << 1] < tree[i << 1 | 1]:
            idxTree[i] = idxTree[i << 1]
        elif tree[i << 1] == tree[i << 1 | 1]:
            idxTree[i] = min(idxTree[i << 1],idxTree[i << 1 | 1])
        else:
            idxTree[i] = idxTree[i << 1 | 1]
        # idxTree[i] = idxTree[i << 1] if tree[i << 1] < tree[i << 1 | 1] else idxTree[i << 1 | 1]

def updateTreeNode(p, value):
    # set value at position p
    tree[p + n] = value
    p = p + n
    # move upward and update parents
    i = p
    while i > 1:
        tree[i >> 1] = min(tree[i],tree[i ^ 1])
        if tree[i] < tree[i ^ 1]:
            idxTree[i >> 1] = idxTree[i]
        elif tree[i] == tree[i ^ 1]:
            idxTree[i >> 1] = min(idxTree[i],idxTree[i ^ 1])
        else:
            idxTree[i >> 1] = idxTree[i ^ 1]
        # idxTree[i >> 1] = idxTree[i] if tree[i] < tree[i ^ 1] else idxTree[i ^ 1]
        # print(f'idxtree {i >> 1} updated to {idxTree[i >> 1]}')
        i >>= 1

# function to get sum on interval [l, r)

def query(l, r):
    res = int(1e13)
    idx = -1
    # loop to find the sum in the range
    l += n
    r += n
    while l < r:
        if l & 1:
            if tree[l] < res:
                idx = idxTree[l]
                # print(f'idx set to {idx} cause tree[l] == res')
            elif tree[l] == res:
                # idx = min(idx,l)
                idx = min(idx, idxTree[l])
                # print(f'idx set to {idx} cause tree[l] == res')
            res = min(res, tree[l])
            l += 1
        if r & 1:
            r -= 1
            if tree[r] < res:
                idx = idxTree[r]
                # print(f'idx set to {idx}')
            elif tree[r] == res:
                # idx = min(idx,r)
                idx = min(idx, idxTree[r])
                # print(f'idx set to {idx}')
            res = min(res, tree[r])
        l >>= 1
        r >>= 1

    return idx,res


N = int(sys.stdin.readline().rstrip())
lt = [int(x) for x in sys.stdin.readline().rstrip().split()]
Q = int(sys.stdin.readline().rstrip())
n = len(lt)
build(lt)
for i in range(Q):
    c,a,b = [int(x) for x in sys.stdin.readline().rstrip().split()]
    if c == 1:
        updateTreeNode(a - 1, b)
    elif c == 2:
        idx,val = query(a-1, b)
        print(f'{idx+1}')