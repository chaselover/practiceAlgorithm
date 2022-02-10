def solution(numbers):
    check = {i: False for i in range(10)}
    for number in numbers:
        if not check[number]:
            check[number] = True
    answer = 0
    for nums in check:
        if not check[nums]:
            answer += nums

    return answer