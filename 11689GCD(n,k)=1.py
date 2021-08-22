# n의 소인수를 p1,p2..라 할때
# 서로소의 갯수는 = n*(1-1/p1)*(1-1/p2)*...*(1-1/pk)

n = int(input())
result = n
# n 으로 소인수 분해 하기.
for i in range(2, round(n ** 0.5) + 1):
    if n % i == 0:
        while n % i == 0:
            n //= i
        # 소인수 하나당 공식 곱해주기
        result *= 1 - (1 / i)
# 남은게 1이상이면 그 수만큼 곱해주기
if n > 1:
    result *= 1 - (1 / n)
print(round(result))