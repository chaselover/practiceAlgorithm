import sys
input = sys.stdin.readline

for test in range(int(input())):
    s = input().rstrip()
    left = 0
    right = len(s) - 1
    start = len(s) + ord('a') - 1
    while left <= right:
        flag = 0
        if s[right] == chr(start):
            right -= 1
            start -= 1
            flag = 1
        elif s[left] == chr(start):
            left += 1
            start -= 1
            flag = 1
        if not flag:
            print('NO')
            break
    else:
        print('YES')

