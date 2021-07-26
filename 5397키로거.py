import sys
input = sys.stdin.readline

T = int(input())
for test in range(T):
    L = input().rstrip()
    left,right = [],[]
    for chr in L:
        if chr=="<":
            if left:
                right.append(left.pop())
        elif chr==">":
            if right:
                left.append(right.pop())
        elif chr=="-":
            if left:
                left.pop()
        else:
            left.append(chr)
    answer = left + right[::-1]
    print("".join(answer))