import sys
input = sys.stdin.readline


N = int(input())
switches = list(map(int, input().split()))
M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    # 남학생이면 스위치 번호가 받은 수의 배수이면 그 스위치의 상태를 바꾼다. XOR(3을 받으면 3,6끔)
    # 여학생은 자기가 받은 스위치 번호를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아 상태를 모두 바꾼다. XOR
    if a==1:
        for i in range(N):
            if not (i+1)%b:
                switches[i] ^= 1
    else:
        size=1
        while b-1-size>=0 and b-1+size<N and switches[b-1-size]==switches[b-1+size]:
            size += 1
        for i in range((b-1)-(size-1),(b-1)+(size-1)+1):
            switches[i] ^= 1
for i in range(0,N,20):
    print(*switches[i:i+20])