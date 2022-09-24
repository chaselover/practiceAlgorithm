"""
리스트 크기5
교환2(무조건)
MAX값.(내림차순 정렬)
"""
T = int(input())

def maxPrize():
    numbers = list(map(int, input().split()))
    N1 = list(str(numbers[0]))
    digits = list(map(int, N1))
    t=0

    for j in range(len(digits)):
        for k in range(j+1,len(digits)):
            if digits[j]<digits[k]:
                digits[j],digits[k] = digits[k],digits[j]
                t+=1
            
            if t==numbers[1]:
                break
    N2 = list(map(str,digits))
    result = ''.join(N2)
    return result


for i in range(T):
    print("#{0} {1}".format(i+1,maxPrize()))