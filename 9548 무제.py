import sys

class Item():
    def __init__(self):
        self.p = -1
        self.l = -1
        self.r = -1
        self.it = 0
        self.cnt = 1

def update(x):
    global nodes
    global root
    nodes[x].cnt = 1
    if nodes[x].l != -1:
        nodes[x].cnt += nodes[nodes[x].l].cnt
    if nodes[x].r != -1:
        nodes[x].cnt += nodes[nodes[x].r].cnt

def rotate(x):
    global nodes
    global root
    p = nodes[x].p
    b = -1
    if nodes[p].l == x:
        b = nodes[x].r
        nodes[p].l = b
        nodes[x].r = p
    else:
        b = nodes[x].l
        nodes[p].r = b
        nodes[x].l = p
    if b != -1:
        nodes[b].p = p
    nodes[x].p = nodes[p].p
    nodes[p].p = x
    if nodes[x].p == -1:
        root = x
    elif nodes[nodes[x].p].l == p:
        nodes[nodes[x].p].l = x
    else:
        nodes[nodes[x].p].r = x
    update(p)
    update(x)

def splay(x):
    global nodes
    global root
    while nodes[x].p != -1:
        p = nodes[x].p
        g = nodes[p].p
        if g != -1:
            if (nodes[p].l == x) == (nodes[g].l == p):
                rotate(p)
            else:
                rotate(x)
        rotate(x)

def find_k(k):
    global nodes
    global root
    k += 1
    x = root
    while 1:
        while nodes[x].l != -1 and nodes[nodes[x].l].cnt > k:
            x = nodes[x].l
        if nodes[x].l != -1:
            k -= nodes[nodes[x].l].cnt
        if k == 0:
            break
        k -= 1
        x = nodes[x].r
    splay(x)

def interval(l, r):
    global nodes
    global root
    find_k(l - 1)
    x = root
    root = nodes[x].r
    nodes[root].p = -1
    find_k(r - l)
    nodes[root].p = x
    nodes[x].r = root
    root = x

def init():
    global nodes
    global root
    del nodes
    nodes = []
    nodes.append(Item())
    nodes.append(Item())
    l = len(nodes)
    nodes[l - 2].r = l - 1
    nodes[l - 1].p = l - 2
    nodes[l - 2].cnt = 2
    root = l - 2

nodes = []
init()
t = int(sys.stdin.readline())
if t > 1:
    exit(0)
i = 0
while i < t:
    s = sys.stdin.readline().rstrip()
    l = len(s)
    init()
    find_k(0)
    x = nodes[root].l
    nodes.append(Item())
    y = len(nodes) - 1
    nodes[root].l = y
    nodes[x].p = y
    nodes[y].p = root
    nodes[y].l = x
    nodes[y].it = s[0]
    nodes[y].cnt = l + nodes[x].cnt
    j = 1
    while j < l:
        nodes.append(Item())
        x = len(nodes) - 1
        nodes[x].p = y
        nodes[y].r = x
        nodes[x].it = s[j]
        nodes[x].cnt = l - j;
        y = x
        j += 1
    update(root)
    while 1:
        q = sys.stdin.readline()
        if q[0] == 'E':
            break
        if q[0] == 'I':
            a, b, c = q.split()
            c = int(c)
            l = len(b)
            find_k(c);
            x = nodes[root].l
            nodes.append(Item())
            y = len(nodes) - 1
            nodes[root].l = y
            nodes[x].p = y
            nodes[y].p = root
            nodes[y].l = x
            nodes[y].it = b[0]
            nodes[y].cnt = l + nodes[x].cnt
            j = 1
            while j < l:
                nodes.append(Item())
                x = len(nodes) - 1
                nodes[x].p = y
                nodes[y].r = x
                nodes[x].it = b[j]
                nodes[x].cnt = l - j;
                y = x
                j += 1
            update(root)
        else:
            a, b, c = q.split()
            b = int(b)
            c = int(c)
            j = b
            while j <= c:
                find_k(j)
                print(nodes[root].it, end = '')
                j += 1
            print('');
    i += 1