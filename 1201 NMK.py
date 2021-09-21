import sys
n,m,k = map(int, sys.stdin.readline().split())
# n이 범위를 만족하는지 (자세한 것은 비둘기의 정리 참조)
if m + k - 1 <= n and n <= m * k:
    # 첫번째 조건 반영 (1 ~ n)까지의 수
    num = [i + 1 for i in range(n)]
    g = []
    # k를 담는다 (= 첫 그룹의 끝나는 점)
    g.append(0)
    g.append(k)
    # 이미 k를 넣었으니 전체에서 k개는 빼고 봐도 되니까 n에서 k를 빼준다
    n -= k
    # 그룹도 한개를 만들었으니 m에서 1을 빼준다
    m -= 1
    # 남은 n - k에서 균일하게 그룹 수(m - 1)로 나누어주면 각각의 그룹의 갯수가 나온다
    gs = 1 if m == 0 else n // m
    # 나누어 떨어지지 않는다면 나머지를 변수에 할당해준다
    r = 0 if m == 0 else n % m
    for i in range(m):
        # 항상 g의 마지막 원소는 그 그룹이 끝나는 지점이므로 거기서 부터 갱신해줘야 한다
        # 각 그룹의 원소의 갯수 만큼 더해주고 나머지의 원소들을 하나하나 씩 다음 그룹에 더해준다
        g.append(g[-1] + gs + (1 if r > 0 else 0))
        if r > 0:
            # 나머지에서 각 그룹한테 한개씩 줬으니까 빼준다
            r -= 1
    # 각 그룹을 뒤집어주는 작업
    for i in range(len(g) - 1):
        begin = g[i]
        end = g[i + 1] - 1
        while begin < end:
            temp = num[begin]
            num[begin] = num[end]
            num[end] = temp
            begin += 1
            end -= 1
    for i in num:
        print(i, end=' ')
# 애초에 n이 범위를 벗어나면 불가능하므로 -1 출력
else:
    print(-1)



################
N,M,K=map(int,input().split())
if M+K-1<=N<=M*K:
    Ln=list(range(N+1))
    Cn=[1]*M
    N-=M
    i=0
    while N>0:
        Cn[i]+=min(K-1,N)
        N-=min(K-1,N)
        i+=1
    i=0
    for j in Cn:
        print(' '.join(map(str,Ln[i+j:i:-1])),end=" ")
        i+=j
else:
    print(-1)