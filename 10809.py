T = int(input())
for test in range(T):
    N, W = input().split()
    W = list(W)
    ans = []
    for i in range(len(W)):
        for _ in range(int(N)):
            ans.append(W[i])

    print("".join(ans))