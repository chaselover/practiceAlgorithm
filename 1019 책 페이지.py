import sys
input = sys.stdin.readline


# calc : a,b가 9또는 0으로 끝나지 않을 때 
# 각 자리수를 ans에 카운트 시키는 함수
def count_page(x,point):
    while x:
        ans[x % 10] += point
        x //= 10
        
end = int(input())
ans = [0] * 10
# 위 글에서 k의 역할을 하는 point
point = 1
# 문제의 조건에 따라 1부터 시작
start = 1

while start <= end:
    # 끝 숫자 9 맞춰주기
    while end % 10 != 9:
        count_page(end, point)
        end -= 1

    if end < start:
        break
    # 시작점 10의 배수 맞춰주기
    while start % 10 != 0:
        count_page(start, point)
        start += 1

    start //= 10
    end //= 10

    for i in range(10):
        ans[i] += (end - start + 1) * point
    point *= 10

print(*ans)


"""
1. a가 9로 끝나는가

1- 1. 그렇지 않다면 각 자릿수를 세준다 + a를 1씩 빼준다

2. b가 0으로 끝나는가

2- 1. 그렇지 않다면 각 자릿수를 세준다 + b를 1씩 더해준다

3. a,b 모두 10으로 나눠준다

4. 위 식을 계산한다

5. 다시 1로 돌아가 반복
"""