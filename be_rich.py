#N일 매매가 알고있음
# 하루 1개만큼 구입
# 판매는 얼마든지 가능#=>쌀때사서 비쌀때 판매.

#T
#일 수N
#N개의 자연수(매매가)

T = int(input())




def MakeMoney():
    N = int(input())
    P = list(map(int,input().split()))
    maxProfit = 0
    for i in range(N):
        for j in range(i+1):
            if max(P)==P[i] and j<=i and P[j] !=0:
                maxProfit += P[i]-P[j]
                P[j]=0
    return maxProfit


for testcase in range(T):
    print("#{} {}".format(testcase+1,MakeMoney()))