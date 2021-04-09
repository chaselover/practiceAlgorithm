import sys
###인풋
T = int(sys.stdin.readline())
for test in range(T):
    N = int(sys.stdin.readline())
    sample = []

    for _ in range(N):
        W, M = map(int,sys.stdin.readline().split())
        sample.append([W,M])
    
    
###비교
    cnt = 0
    sample = sorted(sample,key=lambda x : x[0])
    minN = sample[0][1]
    for i in range(1,N):
        if minN>sample[i][1]:
            minN = sample[i][1]
            cnt += 1

    print(cnt)
###출력