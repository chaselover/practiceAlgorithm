import sys
input = sys.stdin.readline

n = int(input())
liquid = sorted(list(map(int, input().split())))

close_zero = float('inf')
selected = [0]*3

for start in range(n - 2):
    left, right = start + 1, n - 1

    while left < right:
        sum_value = abs(liquid[start] + liquid[left] + liquid[right])

        if sum_value < close_zero:
            selected = [liquid[start], liquid[left], liquid[right]]
            close_zero = sum_value

        if sum_value < 0:
            left += 1
        elif sum_value > 0:
            right -= 1
        else:
            print(*selected)
            exit()
            
print(*selected)