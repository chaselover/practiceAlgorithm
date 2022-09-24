




i=0
while 1:
    i +=1
    ans = 0
    L,P,V = map(int,input().split())
    
    if L ==0 and P ==0 and V ==0:
        break

    ans = (V//P)*L + (V%P)%L
    
    print(f"Case {i}: {ans}")
