import sys
input = sys.stdin.readline


for test in range(int(input())):
    N = int(input())
    arr1 = set(input().split())
    M = int(input())
    for num in input().split():
        print(1 if num in arr1 else 0)