import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
stack = [int(input())]
max_num = stack[-1]
for _ in range(n - 1):
    num = int(input())
    if stack[-1] < num:
        cnt += num - stack[-1]
        max_num = max(max_num, num)
    stack.pop()
    stack.append(num)
cnt += max_num * len(stack) - sum(stack)
print(cnt)


# 2
import sys
input = sys.stdin.readline

def count_add(nums, prev_max):
    if not nums:
        return 0

    max_val = 0
    min_val = float('inf')
    for i in range(len(nums)):
        if max_val < nums[i]:
            max_val = nums[i]
            max_idx = i
        min_val = min(min_val, nums[i])
        
    if max_val == min_val:
        return prev_max - max_val
    
    result = count_add(nums[:max_idx], max_val) + prev_max - max_val + count_add(nums[max_idx+1:], max_val)
    return result


n = int(input())
nums = [int(input()) for _ in range(n)]
print(count_add(nums, max(nums)))


# 3
import sys

if __name__ == "__main__":

    n = int(sys.stdin.readline().rstrip())
    nums = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
    cleared_nums = [nums[0]]
    cnt = 0

    for i in nums:
        if cleared_nums[-1] != i:
            cleared_nums.append(i)

    while True:
        if len(cleared_nums) == 1:
            break

        target = cleared_nums.index(min(cleared_nums))
        two_even = False

        if target == 0:
            even = target+1
        elif target == len(cleared_nums)-1:
            even = target-1
        else:
            if cleared_nums[target-1] > cleared_nums[target+1]:
                even = target+1
            elif cleared_nums[target-1] < cleared_nums[target+1]:
                even = target-1
            else:
                even = target-1
                two_even = True

        cnt += cleared_nums[even] - cleared_nums[target]
        del cleared_nums[target]
        if two_even:
            del cleared_nums[even]

    print(cnt)