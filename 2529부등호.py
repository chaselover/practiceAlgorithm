n = int(input())
inequality = input().split()
check = [False] * 10
max, min = "", ""

def possible(i, j, k):
    if k == '<':
        return i < j
    if k == '>':
        return i > j
    return True

def DFS(depth, seqs):
    global max, min
    if depth == n + 1:
        if not len(min):
            min = seqs
        else:
            max = seqs
        return
    for i in range(10):
        if not check[i]:
            if depth == 0 or possible(seqs[-1], str(i), inequality[depth - 1]):
                check[i] = True
                DFS(depth + 1, seqs + str(i))
                check[i] = False
DFS(0, "")
print(max)
print(min)