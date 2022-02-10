import sys
input = sys.stdin.readline

N,A,B,C,D = map(int,input().split())
min_cost = float('inf')
if B/A > D/C:
    for i in range(C+1):
        if N > A*i:
            if (N-A*i)%C==0:
                cost = B*i + D*((N-A*i)//C)
                if cost<min_cost:
                    min_cost = cost
            else:
                cost = B*i + D*(((N-A*i)//C)+1)
                if cost<min_cost:
                    min_cost = cost
        else:
            if B*i<min_cost:
                min_cost = B*i
            break
else:
    for i in range(A+1):
        if N > C*i:
            if (N-C*i)%A==0:
                cost = D*i + B*((N-C*i)//A)
                if cost<min_cost:
                    min_cost = cost
            else:
                cost = D*i + B*(((N-C*i)//A)+1)
                if cost<min_cost:
                    min_cost = cost
        else:
            if D*i<min_cost:
                min_cost = D*i
            break
print(min_cost)