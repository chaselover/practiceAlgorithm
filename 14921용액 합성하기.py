import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))

min_num = float('inf')
for i in range(N):
    for j in range(N-1,0,-1):
        sum_s = arr[i] + arr[j]
        if abs(min_num) > abs(sum_s):
            min_num = sum_s
        if i == j-1:
            print(min_num)
            exit()
        if sum_s < 0:
            break
        elif sum_s > 0:
            continue
        else:
            print(0)
            exit()


