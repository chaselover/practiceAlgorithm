#검사해서 좌우 두칸에 나보다 작은 숫자만 있으면 됨.


TC = int(input())


def speed():
    D, N = list(map(int,input().split()))
    if N ==1:
        K, S = list(map(int,input().split()))
        v = (D*S)/(D-K)
    else:
        KL = []
        SL = []
        for i in range(N):
            K, S = list(map(int,input().split()))
            KL.append(K)
            SL.append(S)
        if (((D-KL[0])/SL[0]) >=((D-KL[1])/SL[1])):
            v = (D*SL[0])/(D-KL[0])
        else:
            v = (D*SL[1])/(D-KL[1])
    return v



for j in range(TC):
    print("#{0} {1}".format(j+1,speed()))