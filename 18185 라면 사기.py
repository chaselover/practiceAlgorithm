import sys
input = sys.stdin.readline

def buy_triple(idx):
    global cost
    k = min(arr[idx: idx + 3])
    arr[idx] -= k
    arr[idx + 1] -= k
    arr[idx + 2] -= k
    cost += 7 * k


def buy_double(idx):
    global cost
    k = min(arr[idx: idx + 2])
    arr[idx] -= k
    arr[idx + 1] -= k
    cost += 5 * k


def buy_each(idx):
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

        buy_triple(i)
    else:
        buy_triple(i)
        buy_double(i)
    buy_each(i)
print(cost)
