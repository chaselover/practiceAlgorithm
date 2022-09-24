import sys
input = sys.stdin.readline

N = int(input())
k = int(input())

start = 1
end = k
# k번째의 '값'을 찾기위한 탐색. start와 end가 만나는 지점에 mid값이 k번째로 정렬된 수 이다.
while start <= end:
    mid = (start+end)//2

    cnt = 0
    # 우리가 찾으려는 값 mid를 i로 나눴을 때 i번째 행에서 나보다 작은 갯수가 나온다.
    # 여기서 N*N이므로 행의 최대갯수인N은 넘을 수 없다.
    # 계산 끝나면 mid가 N*N에서 몇번째로 큰 숫자인지 알 수 있다.
    for i in range(1,N+1):
        cnt += min(mid//i,N)
    # cnt가 k이상이라면 cnt값을 줄이기위해 앞쪽 라인을 검사하러 간다.
    # cnt값을 k에 수렴시키다보면 mid는 결국 앞에서 k번째 값에 수렴하게 된다.
    if cnt >= k:
        answer = mid
        end = mid-1
    else:
        start = mid+1

print(answer)