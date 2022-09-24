T = int(input())

def sumOdd():
    number = list(map(int,input().split()))
    S = 0
    for i in range(10):
        if number[i] % 2 ==1:
            S += number[i]
    return S

for j in range(T):
    print("#{0} {1}".format(j+1,sumOdd()))