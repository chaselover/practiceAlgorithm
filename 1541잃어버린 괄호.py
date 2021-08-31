import sys
input = sys.stdin.readline


expression = input().split('-')
new_expression = []
for ex in expression:
    nums = ex.split('+')
    sum_n = 0
    for num in nums:
        sum_n += int(num)
    new_expression.append(sum_n)
print(2*new_expression[0] - sum(new_expression))
