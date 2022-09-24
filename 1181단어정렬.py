import sys
input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    a = input().rstrip()
    arr.append((len(a),a))
arr = list(set(arr))
arr.sort(key=lambda arr: (arr[0],arr[1]))

for i in range(len(arr)):
    print(arr[i][1])