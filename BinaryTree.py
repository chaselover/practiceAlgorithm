#이진트리

def search():
    a,b = map(int,input().split())
    i=0
    j=0

    while 1:
        if (1+i*b)/(1+j*a)>a/b:
            j+=1
        elif (1+i*b)/(1+j*a)<a/b:
            i+=1
        else:
            break
    return i+j


T = int(input())

for test in range(T):
    print("#{0} {1}".format(test+1,search()))


