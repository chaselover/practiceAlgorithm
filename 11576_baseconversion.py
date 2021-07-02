x, y = map(int, input().split())
z = int(input())
a = list(map(int, input().split()))
ten = 0
answer =[]
for i in range(z):
    ten += a[-1] * (x**i)
    a.pop(-1)
while ten !=0:
    answer.append(str(ten % y))
    ten = ten // y

print(' '.join(answer[::-1]))