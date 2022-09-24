import sys
input = sys.stdin.readline

for test in range(1,int(input())+1):
    N = input()


    i=0
    ans = 0
    while str(ans)[:len(N)] != N:
        i+=1
        ans = int(1/(5**(1/2))*(((1+(5**(1/2)))/2)**i-((1-(5**(1/2)))/2)**i))

        

    print(f"Case #{test}: {i}")