import sys
input = sys.stdin.readline

def three(idx):
    global cost
    k = min(arr[idx: idx + 3])
    arr[idx] -= k
    arr[idx + 1] -= k
    arr[idx + 2] -= k
    cost += (B + 2 * C) * k


def two(idx):
    global cost
    k = min(arr[idx: idx + 2])
    arr[idx] -= k
    arr[idx + 1] -= k
    cost += (B + C) * k


def one(idx):
    global cost
    cost += B * arr[idx]


N, B, C = map(int, input().split())
if B < C: C = B
arr = list(map(int, input().split())) + [0, 0]
cost = 0
for i in range(N):
    if arr[i + 1] > arr[i + 2]:
        k = min(arr[i], arr[i + 1] - arr[i + 2])
        arr[i] -= k
        arr[i + 1] -= k
        cost += (B + C) * k

        three(i)
    else:
        three(i)
        two(i)
    one(i)
print(cost)
