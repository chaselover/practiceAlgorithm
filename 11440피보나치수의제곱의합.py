#2^x 피보나치를 구해주는 함수(base행렬의 n승을 구하는 함수)
def matrix_mul_self(x):
    base = [[1, 1], [1, 0]]
    result = [[1, 1], [1, 0]]
    for _ in range(x):
        result = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    result[i][j] += (base[i][k] * base[k][j]) % 1000000007
        base = result
        
    return result

#2*2 두 행렬의 곱을 구해주는 함수(인자로 받은 두 행렬을 곱함.)
def matrix_mul(a, b):
    result = [[0 ,0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += (a[i][k] * b[k][j]) % 1000000007
                
    return result

n = bin(int(input())) #2진법으로 변환

result = [[1, 0], [0, 1]]
for i in range(len(n)):
    if n[-i-1] == '1': #2^x 피보나치들만 구해준 다음 곱해줌
        result = matrix_mul(result, matrix_mul_self(i))
        
print(result[0][1] % 1000000007)