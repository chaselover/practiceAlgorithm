o=[]
for t in range(10):
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(100)]
    A = [0]*100
    B, C, D = A[:], 0, 0
 
    for i in range(100):
        C += M[i][i]
        D += M[99-i][i]
        for j in range(100):
            A[i] += M[i][j]
            B[i] += M[j][i]
 
    o.append(f"#{N} {max(A+B+[C,D])}\n")
print(''.join(o))