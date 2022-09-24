import sys

N = int(sys.stdin.readline())



num = [int(sys.stdin.readline()) for _ in range(N)]

num.sort(reverse=True)
Sum=0
i=0
while num[i]>1 and num[i+1]>1 and i<N:
    Sum += num[i]*num[i+1]
    i+=2

num.sort()

i=0
while num[i]=<-1 and num[i+1]=<-1 and i<N:
    Sum += num[i]*num[i+1]
    i+=2    

print(Sum)
