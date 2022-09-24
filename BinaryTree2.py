#이진트리

def search():
    a,b = map(int,input().split())
    up = []
    down =[]
    up.append(1)
    down.append(1)
    i=0
    j=0

    while 1:
        if up[i]/down[j]>a/b:
            down.append(down[j]+up[i])
            j+=1
        elif up[i]/down[j]<a/b:
            up.append(up[i]+down[j])
            i+=1
        else:
            break
    return i+j


T = int(input())

for test in range(T):
    print("#{0} {1}".format(test+1,search()))


