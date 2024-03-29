def testPerformance(A):
    for c in range(W):
        cnt = 1
        for r in range(1, D):
            if A[r][c] == A[r-1][c]:
                cnt += 1
            else:
                cnt = 1
            if cnt >= K:
                break
        if cnt < K:
            return False
    return True
 
def comb(depth, k, pick):
    global result
    if depth > result:
        return
    for i in range(k, D):
        select.append(i)
        for d in range(2):
            select.append(i)
            film[i] = drugs[d]
            if testPerformance(film):
                result = min(result, depth+1)
                select.pop()
                film[i] = raw[i]
            else:
                comb(depth+1, i+1, pick)
                film[i] = raw[i]
                select.pop()
 
# main
T = int(input())
for tc in range(T):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]
    raw = [f[:] for f in film]
    if testPerformance(film):
        result = 0
    else:
        result = float('inf')
        select = []
        drugs = [[0] * W, [1] * W]
        for pick in range(1, D+1):
            comb(0, 0, pick)
            if result < float('inf'):
                break
    print("#{} {}".format(tc+1, result))