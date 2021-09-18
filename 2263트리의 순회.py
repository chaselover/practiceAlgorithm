import sys
input = sys.stdin.readline


n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

# 루트는 post_order[-1]
# in order에서 루트 왼쪽에 있는 애들이 왼쪽 서브트리. 오른쪽이 오른쪽 서브트리. 즉 분할 가능.
