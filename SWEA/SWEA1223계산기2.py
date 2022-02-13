def calculate(post_ex):
    n = len(post_ex)
    stack = []
    for i in range(n):
        # 숫자면 stack
        if post_ex[i].isdigit():
            stack.append(post_ex[i])
        else:
            # 곱하기 나오면 두개빼서 곱하고 다시 넣음
            if post_ex[i] == '*':
                stack.append(int(stack.pop()) * int(stack.pop()))
            # 더하기 나오면 두개 빼서 더하고 다시 넣음
            elif post_ex[i] == '+':
                stack.append(int(stack.pop()) + int(stack.pop()))
            else:
                stack.pop()
    return stack[0]


def make_post(expression):
    isp = {'+': 1, '-': 1, '*': 2, '/': 2, ')': 0, '(': 0}
    icp = {'+': 1, '-': 1, '*': 2, '/': 2, ')': 0, '(': 3}
    stack = []
    ans = ""
    for s in expression:
        if s.isdigit():
            ans += s
        elif s == ')':
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.pop()
        else:
            while stack and icp[s] <= isp[stack[-1]]:
                ans += stack.pop()
            stack.append(s)
    while stack:
        ans += stack.pop()
    return ans


for test in range(1, 11):
    n = int(input())
    print(f'#{test} {calculate(make_post(input()))}')