A, B, C = map(int, input().split())
X, Y, Z = map(int, input().split())
answer = 0

# 각 X, Y, Z 식권 3장은 각 Y, Z, X 1장으로 바꿀 수 있다.
# 결국 현재 식권으로 최대한 음식으로 교환 후, 다음 식권으로 교환
# 이를 총 3번하면 된다.
# 4번째에선 원래 식권으로 돌아오기 때문.

for _ in range(3):
    # 가능한 최대 치킨 수
    chicken = min(A, X)
    answer += chicken
    A -= chicken
    X -= chicken
    # 가능한 최대 피자 수
    pizza = min(B, Y)
    answer += pizza
    B -= pizza
    Y -= pizza
    # 가능한 최대 햄버거 수
    burger = min(C, Z)
    answer += burger
    C -= burger
    Z -= burger
    
    # 각 X, Y, Z 식권 3장은 각 Y, Z, X 1장으로 교환
    Y, Z, X = X // 3, Y // 3, Z // 3

print(answer)