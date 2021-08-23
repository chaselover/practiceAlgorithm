import decimal
# 천자리까지 정확도 주기
decimal.getcontext().prec = 1000


N = int(input())
for _ in range(N):
    # Decimal  객체를 만듬.(float, int같은)
    # 자릿수 10자리까지 정확하게 입력해줌.
    d = decimal.Decimal(input().rstrip() + '.0000000000') 
    pow = decimal.Decimal('1') / decimal.Decimal('3')
    d = decimal.Decimal(d ** pow)
    # decimal 파이썬 자체 내장 함수에 대응, 500자리에서 대충 올렸다.
    d = round(d, 500)
    # quantize(a,b) -> b의 지수를 가지는 자리 올림됨 x와 같은 값을 반환.
    # d에 대해 a와 같은 자릿수에서 0을 향해 올림해서 값을 가져감
    d = decimal.Decimal(d).quantize(decimal.Decimal('.0000000001'), rounding=decimal.ROUND_DOWN)
    print(d)