# return 이 하나면 1의 연산이라 보면 됨.
# T(n) = T(n-1) + n = T(0) + n(n+1)/2 => n^2연산
# T(n) = T(n/2) + 1 = log n + 2 => log n 연산
# T(n) = 2 * T(n/2) + n = n^(log(b)a) * log n = n * log n (a=2, b=2)
# T(n) = T(n-1) + 1/n = T(0) + 시그마(1/k)고 시그마(1/k)는 1~n까지 1/x의 적분 보다 같거나 작은데 이는 1+ log n - log 1 보다 작음을 의미.
# = T(0) + log n + 1 = log n
def fibo(n):
    sqrt_5 = 5 ** (0.5)
    ans = (((1 + sqrt_5) / 2) ** n - ((1 - sqrt_5) / 2) ** n) // sqrt_5
    return ans % 1000000


n = int(input())
print(fibo(n))

#2^x 피보나치를 구해주는 함수
def matrix_mul_self(x):
    base = [[1, 1], [1, 0]]
    result = [[1, 1], [1, 0]]
    for _ in range(x):
        result = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    result[i][j] += (base[i][k] * base[k][j]) % 1000000
        base = result
        
    return result

#2*2 두 행렬의 곱을 구해주는 함수
def matrix_mul(a, b):
    result = [[0 ,0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += (a[i][k] * b[k][j]) % 1000000
                
    return result

n = bin(int(input()))[2:] #2진법으로 변환

result = [[1, 0], [0, 1]]
for i in range(len(n)):
    if n[-i-1] == '1': #2^x 피보나치들만 구해준 다음 곱해줌
        result = matrix_mul(result, matrix_mul_self(i))
        
print(result[0][1] % 1000000)



def mul(a, b):
    x1 = (a[0]*b[0] + a[1]*b[2]) % 1000000
    x2 = (a[0]*b[1] + a[1]*b[3]) % 1000000
    x3 = (a[2]*b[0] + a[3]*b[2]) % 1000000
    x4 = (a[2]*b[1] + a[3]*b[3]) % 1000000
    return x1,x2,x3,x4

def fib(n):
    a, b = (1,0,0,1), (1,1,1,0)
    while n > 0:
        if n & 1:
            a = mul(a, b)
        b = mul(b, b)
        n >>= 1
    return a[2]

print(fib(int(input())))