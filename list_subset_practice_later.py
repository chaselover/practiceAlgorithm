#coding: utf-8


arr =list(map(int,input().split())
n = bin(len(arr))

for i in range(1<<n):
    for j in range(n):
        if i&(1<<j):
            print(arr[j],end=",")
    print()