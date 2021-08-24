import sys
input = sys.stdin.readline

# 제곱을 재귀로.. 분할정복으로 해도 될듯?
def pow(a,b,c):
    if b==0:
        return 1
    if b==1 :
        return a%c
    if b%2==0:
        return pow(a**2%c,b//2,c)
    else:
        return a*pow(a**2%c,b//2,c)%c

N = int(input())
menus = sorted(map(int,input().split()))
MOD = 1000000007
minus = 0
plus = 0
for i in range(N):
    minus += (menus[i]%MOD)*pow(2,N-i-1,MOD)
    plus += (menus[i]%MOD)*pow(2,i,MOD)
    plus %= MOD
print((plus-minus)%MOD)



# 50점
# import sys
# input = sys.stdin.readline

# N = int(input())
# menus = sorted(map(int,input().split()))
# MOD = 1000000007
# minus = 0
# for i in range(N-1):
#     for j in range(i+1,N):
#         minus += ((menus[j] - menus[i])*(2**(j-i-1)))%MOD
# print(minus%MOD)

# logN의 파워함수.
# def power(a, n):
#     ret = 1
#     while n > 0:
#         if n % 2 != 0:
#             ret *= a
#         a *= a
#         n //= 2        
    
#     return ret

# logN power
# def power(n, p):
#     if p == 0:
#         return 1
#     # Call this only once, instead of two times.
#     power_p_divided_by_2 = power(n, p // 2)
#     if p % 2:
#         return n * power_p_divided_by_2 * power_p_divided_by_2
#     else:
#         return power_p_divided_by_2 * power_p_divided_by_2