import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    s = list(input())
    answer = 0
    section = 1
    tmp = 1
    for i in range(len(s) - 1):
        if s[i + 1] == s[i]:
            tmp += 1
        else:
            if i == 0:
                s[i], s[i + 1] = s[i + 2], s[i + 2]
                answer += 1
                tmp += 1
            elif tmp & 1:
                s[i] = str(int(s[i]) ^ 1)
                answer += 1
                tmp = 2
            else:
                tmp = 1
                section += 1

    print(answer, section)
