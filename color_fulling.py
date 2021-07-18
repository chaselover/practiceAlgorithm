"""
N킬로그램 배달해야됨.
봉지는 3,5킬로 단위.
가장 적은 봉지
"""

N = int(input())

cnt =0

while N>0:
    if N%5==0:
        cnt += N//5
        break
    else:
        N = N-3
        cnt +=1

if N<0:
    print(-1)

print(cnt)