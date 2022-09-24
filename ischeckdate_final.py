N = int(input())
numbers = list(map(int,input().split()))
numbers = sorted(numbers)
M = int((N-1)/2)
answer = numbers[M]

print(answer)