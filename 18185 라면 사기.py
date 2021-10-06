import sys
input = sys.stdin.readline

def three(idx):
    global cost
    k = min(arr[idx: idx + 3])
    arr[idx] -= k
    arr[idx + 1] -= k
    arr[idx + 2] -= k
    cost += 7 * k


def two(idx):
    global cost
    k = min(arr[idx: idx + 2])
    arr[idx] -= k
    arr[idx + 1] -= k
    cost += 5 * k


def one(idx):
    global cost
    cost += 3 * arr[idx]


N = int(input())
arr = list(map(int, input().split())) + [0, 0]
cost = 0
for i in range(N):
    if arr[i + 1] > arr[i + 2]:
        k = min(arr[i], arr[i + 1] - arr[i + 2])
        arr[i] -= k
        arr[i + 1] -= k
        cost += 5 * k

        three(i)
    else:
        three(i)
        two(i)
    one(i)
print(cost)
