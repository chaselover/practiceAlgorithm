import sys
input = sys.stdin.readline

for test in range(int(input())):
    input()
    k, n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    answer = []
    idx_a = 0
    idx_b = 0
    while idx_a != n or idx_b != m:
        while idx_a < n and not a[idx_a]:
            answer.append(0)
            idx_a += 1
            k += 1
        while idx_b < m and not b[idx_b]:
            answer.append(0)
            idx_b += 1
            k += 1

        if idx_a < n:
            if a[idx_a] <= k:
                answer.append(a[idx_a])
                idx_a += 1
            else:
                answer = [-1]
                break

        while idx_a < n and not a[idx_a]:
            answer.append(0)
            idx_a += 1
            k += 1

        if idx_b < m:
            if b[idx_b] <= k:
                answer.append(b[idx_b])
                idx_b += 1
            else:
                answer = [-1]
                break

    print(*answer)