import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

N = int(input())
A = list(map(int,input().split()))

# 앞에서 오는 포인터.

# 뒤에서 오는 포인터.
# 땡겻을 때 더 작은걸 반환.

def palindrome(begin,end):
    if begin>end:
        return 0
    if A[begin] ==A[end]:
        result = palindrome(begin +1,end-1)
    else:
        result = min(1+palindrome(begin+1, end),1+palindrome(begin,end-1))
    return result;

print(palindrome(0,N-1))