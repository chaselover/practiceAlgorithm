
def check(nums:list) -> int:
    sum_minus = 0
    check_zero = {i:0 for i in range(16)}
    for num in nums:
        for i in range(16):
            if num & (1<<i):
                check_zero[i] += 1
    for zero_idx in check_zero:
        if check_zero[zero_idx] == len(nums):
            for i in range(zero_idx,-1,-1):
                if check_zero[i] < len(nums)-1:
                    check_zero[zero_idx] -= 1
                    check_zero[i] += 1
                    sum_minus += 2**zero_idx - 2**i
                    break
            else:
                sum_minus += 2**zero_idx

    return sum_minus


def solution(m, b):
    new_arr = [[] for _ in range(len(m))]
    num_idx = 0
    idx = 0
    answer = []
    for num in m:
        for _ in range(num):
            new_arr[idx].append(b[num_idx])
            num_idx += 1
        else:
            idx += 1
    for arr in new_arr:
        answer.append(check(arr))
    return answer


print(solution([2,2],[6,2,1,2]))