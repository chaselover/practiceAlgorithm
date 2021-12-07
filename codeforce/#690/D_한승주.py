import sys
input = sys.stdin.readline
 
 
for test in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    total = sum(arr)
    candidate = [num for num in range(1, total + 1) if not total % num]
    for target in candidate:
        tmp, answer = 0, 0
        for num in arr:
            tmp += num
            answer += 1
            if tmp == target:
                tmp = 0
                answer -= 1
            elif tmp > target:
                break
        else:
            print(answer)
            break