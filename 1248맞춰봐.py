import sys
input = sys.stdin.readline

#부호와 합이 일치하는지 확인하는 함수 일치하면 true 합과 일치하지 않으면False
def ck(idx):
    hap = 0
    for i in range(idx, -1, -1):
        hap += result[i]
        if hap == 0 and S[i][idx] != 0:
            return False
        elif hap < 0 and S[i][idx] >= 0:
            return False
        elif hap > 0 and S[i][idx] <= 0:
            return False
    return True

def solve(idx):
    # 인덱스가 N에 도달할때까지 모든 idx check가 true인 상태면 모든 선택지에 대해 true를 반환하고 그 당시의 result배열을 반환. 
    if idx == N:
        return True
        # 0일때는 0기록하고 다음순서로 넘어간다.(0일때는 result도 무조건 0)
    if S[idx][idx] == 0:
        result[idx] = 0
        return solve(idx+1)
    # 수를 1부터 10까지만 쓸 수있다. 모든경우의 수를 S값 즉 양 음에 따라 곱해서 기록한다.
    for i in range(1, 11):
        result[idx] = S[idx][idx] * i
        # 인덱스까지의 모든 합이 부호와 일치하면 true.그리고 뒤의 모든 idx도 다 일치하면 true
        if ck(idx) and solve(idx+1):
            return True
    # 1~10 돌았는데 부호일치안하면 잘못된 선택지이므로 False반환.
    return False

#s는 array의 부호에 따라 result에 저장할 숫자들의 계수(음수,양수여부를 저장하는 배열)
N = int(input())
arr = list(input())
S = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(i, N):
        temp = arr.pop(0)
        if temp == '+':
            S[i][j] = 1
        elif temp == '-':
            S[i][j] = -1

# result배열에 각 부호에 맞는 숫자를 경우의수에 따라. 저장해주면서 백트래킹한다.
result = [0] * N
solve(0)
# checking이끝난 배열에 대해 출력한다.
print(' '.join(map(str, result)))