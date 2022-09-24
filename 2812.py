
N , K= map(int,input().split())
number = list(input())
ans = []

for i in range(N):
    while K != 0 and ans:
        if ans[-1] < number[i]:
            ans.pop()
            K -= 1
        else:
            break
    ans.append(number[i])
# 전꺼보다 작은수는 안넣고 큰수면 전에꺼 빼고 내꺼 넣음. K양수일때까지 돌고 K남으면 남은K만큼 소모시킴.
# 아이디어는 큰수는 넣고 그 다음 숫자들이랑 비교시키는것.
# ans에 어떤 숫자를 넣을것인가?
for _ in range(K):
    ans.pop()

print(''.join(ans))