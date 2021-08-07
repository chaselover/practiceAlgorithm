import sys
input = sys.stdin.readline

N,M,K = map(int,input().split())
arr = [[1]*(M+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,M+1):
        # a를 하나 뺀 단어와 z를 하나 뺀 단어의 갯수의 합.
        arr[i][j] = arr[i-1][j] + arr[i][j-1]
        # a와z의 갯수에 따라 단어의 갯수를 저장하는 배열 arr.

if arr[N][M] < K:
    print(-1)
else:
    result=""
    while True:
        if not N or not M:
            result += "z"*M
            result += "a"*N
            break
# arr[N-1][M]은 a를 하나 앞으로 빼뒀을때 뒤에 배열 할 수 있는 가짓수.즉 K가 이거보다 작으면 앞이 a고 크면 z임.
# 이걸 기준으로 하나씩 앞자릿수를 확정시켜주며 z가 앞으로 가면 flag만큼 K를 줄여줌(그래야 다시 앞자리를 a로 유지시키면서 반복가능.)
        flag = arr[N-1][M]
        if K <= flag:
            result += "a"
            N -= 1
        else:
            result += "z"
            M -= 1
            K -= flag
    print(result)