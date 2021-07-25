n = (int(input()) // 2 * 2) + 1

A = [[1, 0], [0, 1]]
B = [[1, 1], [1, 0]]

def matrix_mul(a, b):
    result = [[0] * 2 for _ in range(2)]
    
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += a[i][k] * b[k][j]
                
    for i in range(2):
        for j in range(2):
            result[i][j] %= 1000000007
            
    return result

while n:
    if n & 1:
        A = matrix_mul(A, B)
    B = matrix_mul(B, B)
    
    n //= 2
    
print(A[1][0] - 1)