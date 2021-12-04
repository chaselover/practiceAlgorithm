import sys
input = sys.stdin.readline


for test in range(int(input())):
    n = int(input())
    if n & 1:
        print("YES")
        continue
    answer = "NO"
    while n > 2:
        n //= 2
        if n & 1:
            answer = "YES"
            break
    print(answer)