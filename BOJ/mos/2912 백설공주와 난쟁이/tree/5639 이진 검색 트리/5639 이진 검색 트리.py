import sys

def dfs(pos, min_v):
    ret = 0
    if pos + 1 < len(orders) and orders[pos] > orders[pos + 1]:
        ret += dfs(pos + 1, min(min_v, orders[pos]))
    if pos + ret + 1 < len(orders) and orders[pos] < orders[pos + ret + 1] \
        and orders[pos + ret + 1] < min_v:
        ret += dfs(pos + ret + 1, min_v)
    print(orders[pos])
    return ret + 1

sys.setrecursionlimit(10009)

orders = []
for v in map(int, sys.stdin.read().split()):
    orders.append(v)
dfs(0, 0x3c3c3c3c)


# 2
from bisect import bisect_left
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def post_order(start, end):
    if start > end:
        return
    
    root = pre_order[start]
    mid = bisect_left(pre_order, root, start+1, end+1)
    post_order(start+1, mid-1)
    post_order(mid, end)
    print(root)

if __name__ == "__main__":
    pre_order = []
    while True:
        try:
            x = int(input())
            pre_order.append(x)
        except:
            break
    
    post_order(0, len(pre_order)-1)


# 3
import sys
sys.setrecursionlimit(1000000)


def pretopost(s, e):
    if s >= e:
        return
    root = prefix[s]
    if prefix[e - 1] <= root:
        pretopost(s + 1, e)
        print(root)
        return
    for i in range(s + 1, e):
        if prefix[i] > root:
            tmp = i
            break
    pretopost(s + 1, tmp)
    pretopost(tmp, e)
    print(root)


prefix = []
while True:
    try:
        prefix.append(int(sys.stdin.readline()))
    except:
        break
pretopost(0, len(prefix))