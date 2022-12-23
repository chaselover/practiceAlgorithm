from sys import stdin
from random import randint

input = stdin.readline

n, c = map(int, input().split())
arr = [0] + list(map(int, input().split()))
arr_inv = [[] for _ in range(c + 1)]
for i in range(1, n + 1):
    arr_inv[arr[i]].append(i)
for _ in range(int(input())):
    s, e = map(int, input().split())
    ans = 'no'
    for _ in range(30):
        k = arr[randint(s, e)]
        start = 0
        end = len(arr_inv[k]) - 1
        rs = 0
        while start <= end:
            mid = (start + end) // 2
            if arr_inv[k][mid] < s:
                start = mid + 1
            elif arr_inv[k][mid] > s:
                rs = mid
                end = mid - 1
            else:
                rs = mid
                break
        start = 0
        end = len(arr_inv[k]) - 1
        re = end
        while start <= end:
            mid = (start + end) // 2
            if arr_inv[k][mid] < e:
                re = mid
                start = mid + 1
            elif arr_inv[k][mid] > e:
                end = mid - 1
            else:
                re = mid
                break
        if (re - rs + 1) * 2 > (e - s + 1):
            ans = f'yes {k}'
            break
    print(ans)
