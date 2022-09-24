import itertools as I,sys
def F(s):
    n=len(s)
    *a,r,p=[0]*(n+2)
    for i in range(n):
        if i<=r:a[i]=min(a[2*p-i],r-i)
        else:a[i]=0
        while i-a[i]-1>=0 and i+a[i]+1<n and s[i-a[i]-1]==s[i+a[i]+1]:a[i]+=1
        if r<i+a[i]:r,p=i+a[i],i
    return a
# 숫자 버림
input()
# 함수 g는 map(int, input().split()).이랑똑같음. 대신 함수 할당해서 빌트인에서 안불러와도 되도록 ㅎ함.
g=lambda:[*map(int,sys.stdin.readline().split())]
# 문자열 l
l=g()
#  v는 itertools.chain으로 chan안에 들어오는 모든 리스트요소들을 연결시킴. 여기서는 문자열 l 안의 모든 요소를 0과 엮어서 합침.
v=[*I.chain(*[[i,0]for i in l])]
# 뒤에 0하나 빼서 버림.
v.pop()
# a는 기존 홀수 펠린드롬 산출
a=F(l)
# b는 짝수 펠린드롬 산출한데서 0값에 해당하는 값 다 버림.
b=F(v)[1::2]
for i in range(int(input())):
    v,e=g()
    l,w=e-v+1,0
    # 홀수면 위 짝수면 아래.
    if l&1:
        x=1+a[(e+v)//2-1]*2
    else:
        x=(b[(e+v)//2-1]+1)//2*2
    # x값이 문자열 길이보다 크거나 같으면 1 or 0프린트.
    print(int(x>=l))



# def manacher(s):
#     A = []
#     R = -1; p = -1
#     for i in range(len(s)):
#         if i <= R: A.append(min(A[2*p-i], R-i))
#         else: A.append(0)
#         while i-A[i]-1 >= 0 and i+A[i]+1 < len(s) and s[i-A[i]-1] == s[i+A[i]+1]: A[i]+= 1
#         if i+A[i] > R: R = i+A[i]; p = i
#     return A

# def maxpalin(M, i):
#     if i%2 == 0: return M[i]//2*2+1
#     return (M[i]+1)//2*2

# from sys import stdin
# input = stdin.readline
# n = int(input())
# L = [0]*(2*n-1)
# for i, c in zip(range(n), map(int,input().split())): L[2*i] = c
# M = manacher(L)
# for TEST in range(int(input())):
#     a, b = map(int,input().split())
#     print(int(maxpalin(M, a+b-2) >= b-a+1))