import sys
input = sys.stdin.readline



for test in range(int(input())):
    M = int(input())

    # 여러줄 입력을 한 리스트에 -> extend써야 배열 +연산처럼 들어감
    seqs = []
    for i in range(M//10+1):
        seqs.extend(list(map(int,input().split())))

    # 출력하는 갯수 : 홀수의 갯수.
    print(M//2+1)

    # M=1일때  index에러 대비해서 따로 빼줌.
    print(seqs[0], end=" ")

    # count이용 출력 숫자 10개로 조절. 줄바꿈.
    # for else문으로 반복문 끝났을 때 한칸띄어서 다음 입력이 깔끔하게 제어.
    if M !=1:
        cnt=1
        for i in range(2,M,2):
            print(sorted(seqs[:i+1])[(i+1)//2], end=" ")
            cnt+=1
            if cnt==10:
                print()
                cnt=0
        else:
            print()