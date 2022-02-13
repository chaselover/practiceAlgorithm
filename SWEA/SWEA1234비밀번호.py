import sys
sys.stdin = open('input.txt')


for test in range(1,11):
    s, nums = input().split()
    nums = list(nums)       # 비밀번호 list
    stack = []              # 옮겨담을 stack

    while nums:
        stack.append(nums.pop())        # 일단 pop
        while nums and stack and stack[-1] == nums[-1]:  # 같은 문자가 나오면 양쪽 다 제거. 틀린게 나올때까지 혹은 빌때까지
            stack.pop()
            nums.pop()
    print(f"#{test} {''.join(stack)[::-1]}")            # stack 에 역순으로 담긴 password 뒤집어 출력

