import sys
input = sys.stdin.readline
from math import gcd

N,A,B,C,D = map(int,input().split())
gcd_AC =gcd(A,C)
lcm_AC = gcd_AC*(A//gcd_AC)*(C//gcd_AC)
pre_pass_flowers = (N//lcm_AC)
R_cnt = N%lcm_AC

if B/A < D/C:
    pre_calculated_cost=pre_pass_flowers*B
else:
    pre_calculated_cost=pre_pass_flowers*D
    
# R_cnt
min_cost = float('inf')
# i는 A세트를 사는 번들의 갯수. R_cnt-A*i는 C에서 메꿔야 하는 갯수.
for i in range(R_cnt//A+1):
    if not (R_cnt-A*i)%C:
        cost_to_R = B*i+(D*((R_cnt-A*i)//C))
        if cost_to_R < min_cost:
            min_cost = cost_to_R
    else:
        cost_to_R = B*i+(D*((R_cnt-A*i)//C+1))
        if cost_to_R < min_cost:
            min_cost = cost_to_R

print(pre_calculated_cost+cost_to_R)