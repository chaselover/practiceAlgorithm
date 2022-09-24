import sys
inmput = sys.stdin.readline


def check(a,left,right):
    while left < right:
        if a[left] != a[right]:
            return 0
        left += 1
        right -= 1
    return 1


s = input().rstrip()
n = len(s)
# 최대 길이가 회문 아니면 n
if not check(s,0,n-1):
    print(n)
# 최대길이에서 하나뺀게 회문 아니면 n-1
elif not check(s,0,n-2):
    print(n-1)
else:
    print(-1)