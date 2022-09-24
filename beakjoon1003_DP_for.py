import sys

#입력부
n = int(sys.stdin.readline())
scores =[]
sum_score=[]
check = [0]*n
   
for _ in range(n):
    score = int(sys.stdin.readline())
    scores.append(score)



sum_score.append(scores[0])
sum_score.append(scores[0]+scores[1])
check[0] = 1
check[1] = 1

for i in range(2,n):
    if sum_score[i-2]<sum_score[i-1] and (check[i-2]!=1 or check[i-1] !=1):  
        sum_score.append(sum_score[i-1]+scores[i])
        check[i] = 1
    elif scores[i-1]>scores[i-2] and (check[i-2]==1 and check[i-1] ==1):
        sum_score.append(sum_score[i-1]-scores[i-2]+scores[i])
        check[i] = 1
        check[i-1]=2
    else:
        sum_score.append(sum_score[i-2]+scores[i])
        check[i] = 2


print(check)

"""
case1: i-1이 i-2보다 커서 i-1에서 이동.(i-1), i-2가 동시에 1이동이면 안됨.
case2: i-2가 i-1보다 커서 i-2에서 이동.(조건 없음)
case3: i-1이랑 i-2가 동시에 1인데 i-1score보다 i-2스코어 가 더 큼.그럼 i-1배제보다 i-2배제가 더 좋음.
->


"""