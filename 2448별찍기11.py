import sys
input = sys.stdin.readline


# 정복
def Conquer(shift):
    c = len(tri)                                                #최초 3 (즉 세로줄 수)
    for i in range(c):                                          #triangle 한줄씩 꺼냄.
        tri.append(tri[i] + tri[i])                             #tri.append(tri[i] + tri[i]) 3일때그림아래쪽에 바로 2개를 그림.
        tri[i] = ("   " * shift + tri[i] + "   " * shift)       #tri[i] = ("   "*shift + tri[i] + "   " * shift)
                                                                #아래쪽에 트리 두개 더한 그림을 그렸다면 원래 있던 그림에도 한줄씩 꺼내 " "공백을
                                                                #삐져나온만큼 더해준다.
                                                                #그럼 세로 3줄 -> 6줄 -> 12줄 -> 24줄 각 줄당 두줄씩 K번 더 그려지게된다.
#  입력
tri = ["  *   "," * *  ","***** "]                              # 삼각형 밑변끼리 붙지 않도록 오른쪽 한칸 띄어야함.
N = int(input())


# 분할

k=0
N = N//3
while N != 1 :
    N = N//2
    k +=1
# 조합
for i in range(k):
    Conquer(int(pow(2,i)))                                      #pow는 i승을 의미. 스페이스를 매k마다 2배씩 더 그려야 하기 때문.
for stars in tri:
    print(stars)


        

