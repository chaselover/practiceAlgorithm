#coding: utf-8


T = int(input())

def LISDP():
    a = list(map(int,input().split()))
    LIS = [0]*(a[0]+1)
    for i in range(1,a[0]+1):
        LIS[i] = 1
        for j in range(1,i):
            if a[j]<a[i] and 1+LIS[j] > LIS[i]:
                LIS[i] = 1+LIS[j]
    return max(LIS)


for k in range(T):
    print("#{0} {1}".format(k+1, LISDP()))