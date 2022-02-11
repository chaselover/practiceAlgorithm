

def is_prime(n):
    if n <= 1:
        return False
    m = int(n**0.5)+1
    for i in range(2,m):
        if not n%i:
            return False
    return True


def solution(n, k):
    # 정수 n을 k진수로 바꿨을 때
    # 소수 양쪽에 0, 한쪽에만 0, 양쪽에 아무것도 없는 경우, 단 소수는 0을 포함하지 않는 소수.
    # ex) 437674를 3진수? -> 211020101011여기서 찾을 수 있는 소수 211 2 11 소수의 갯수를 return
    answer = ''
    while n:
        n, b = n//k, n%k
        answer = str(b) + answer
    cnt = 0
    for num in answer.split('0'):
        if num and is_prime(int(num)):
            cnt += 1
    return cnt


print(solution(437674,3))