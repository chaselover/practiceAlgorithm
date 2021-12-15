import sys
input = sys.stdin.readline

for test in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    answer = 0
    even = float('inf')
    odd = float('inf')
    for idx, num in enumerate(arr):
        if idx & 1:
            odd = min(odd, num)
        else:
            even = min(even, num)
    for idx, num in enumerate(arr):
        if idx & 1:
            if not num % even:
                break
        else:
            if num % even:
                break
    else:
        answer = even

    if answer:
        print(answer)
        continue

    for idx, num in enumerate(arr):
        if idx & 1:
            if num % odd:
                break
        else:
            if not num % odd:
                break
    else:
        answer = odd
    print(answer)