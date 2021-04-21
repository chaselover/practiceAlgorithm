t = int(input())
for test in range(t):
    n= int(input())
    numbers = []

    for _ in range(n):
        numbers.append(input())

    numbers.sort()
    ans = 0
    for i in range(n-1):
        if numbers[i+1].find(numbers[i]) == 0:
            ans = 1
            break

    if ans == 1:
        print("NO")
    else:
        print("YES")

