import sys
input = sys.stdin.readline

# 브루트포스.
# ord()로 가장 낮은 idx찾으려 했는데 맨앞이랑 맨끝때매 경우의수 너무 갈림.
s = input().rstrip()
l = len(s)
answer = []
for i in range(l-2):
    for j in range(i+1, l-1):
        for k in range(j+1, l):
            new_s = s[:j][::-1] + s[j:k][::-1] + s[k:][::-1]
            answer.append(new_s)

answer.sort()
print(answer[0])