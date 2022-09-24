import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    s = list(input())
    answer = 0
    tmp = 1
    for i in range(len(s) - 1):
        if s[i + 1] == s[i]:
            tmp += 1
        else:
            if tmp & 1:
                s[i] = str(int(s[i]) ^ 1)
                answer += 1
                tmp = 2
            else:
                tmp = 1
    print(answer)
