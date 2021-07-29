import sys
input = sys.stdin.readline

# 이름에 너무 직관성이 없어서 멋대로 고치겠다.
N, num1, price1, num2, price2 = map(int, input().split())

# 최대 루프 수
max_num = 1e5

# 초기치 : 1번 풀매수
answer2 = ((N - 1) // num1 + 1) * price1

# 첫번째 제품 cnt개 강제 구매
cnt = 0
while(cnt <= max_num):    
    num = N - cnt * num1
    if num < 0:
        break
    answer3 = cnt * price1
    if num % num2 == 0:
        answer2 = min(answer2, answer3 + ((num//num2) * price2))
        break
    # 남은 물건 첫번째 제품으로 도배
    cnt = cnt + 1
    num = ((num - 1)//num2) + 1
    answer2 = min(answer2, answer3 + num * price2)

# 두번째 제품 cnt개 강제 구매
cnt = 0
while(cnt <= max_num):    
    num = N - cnt * num2
    if num < 0:
        break
    answer3 = cnt * price2
    if num % num1 == 0:
        answer2 = min(answer2, answer3 + ((num//num1) * price1))
        break
    # 남은 물건 첫번째 제품으로 도배
    cnt = cnt + 1
    num = ((num - 1)//num1) + 1
    answer2 = min(answer2, answer3 + num * price1)

print(answer2)
