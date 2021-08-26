for test in range(1,int(input())+1):
    X,Y = map(int,input().split())
    answer = ((X+Y)/6)*(X-(X+Y)/3)*(Y-(X+Y)/3)
    print(answer)