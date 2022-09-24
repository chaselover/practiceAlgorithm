import sys
input = sys.stdin.readline

A, B, C = map(int, input().split(' '))

# 정복
def conq(length):
    # 정복 : length가 1이 되면 A를 반환하겠다.(최소단위 연산의 정복)
    if length == 1:
        return A %C
        # 짝수면 좌우로 찢고
    if length % 2 == 0:
        # 분할 (곱해야하는 length를 반으로 나눠가며 계산하겠다.)
        left = conq(length // 2)
        # 조합(함수 반환시마다 양쪽을 곱해서 올라가겠다.)
        return left * left %C
        # 홀수면 좌우로 찢고 남은A하나 곱해준다.
    else:
        left = conq(length // 2)
        return left * left * A %C


print(conq(B))

