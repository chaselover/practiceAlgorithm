import sys
input = sys.stdin.readline


for _ in range(int(input())):
    d, n = map(int, input().split())
    arr = list(map(lambda x: int(x)%d, input().split()))
    visited = [1] + [0] * 1000000
    sum_n = 0
    for num in arr:
        sum_n = (sum_n + num) % d
        visited[sum_n] += 1
    
    # i가 나온 것들중 2개를 뽑는 조합의 수.
    result = 0
    for i in range(d):
        result += visited[i]*(visited[i]-1)//2
    print(result)
