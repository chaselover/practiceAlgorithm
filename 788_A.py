import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    flag = False
    left, right = 0, n - 1
    while left < right:
        if arr[left] > 0:
            while arr[right] > 0 and left < right:
                right -= 1
            if left < right:
                arr[left] *= -1
                arr[right] *= -1
            else:
                break
        left += 1
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            print("NO")
            break
    else:
        print("YES")

