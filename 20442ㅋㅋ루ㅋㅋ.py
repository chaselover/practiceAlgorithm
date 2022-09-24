import sys
input = sys.stdin. readline

s = input().strip()
left_K_cnt = []
rignt_K_count = []
# 정방향에서 K갯수 세면서 R나올때마다 cnt를 lk에 저장
cnt = 0
for i in s:
    if i == 'K':
        cnt += 1
    else:
        left_K_cnt.append(cnt)
# 역방향에서 K세면서 R나올때마다 cnt를 rk에 저장.
cnt = 0
for i in s[::-1]:
    if i == 'K':
        cnt += 1
    else:
        rignt_K_count.append(cnt)
rignt_K_count.reverse()
# rk뒤집음.
# l,r 양끝에서 부터 한칸씩 땡기면서 검사.
l, r = 0, len(left_K_cnt) - 1
ans = 0
# l 과 r이 만나면 조사 끝. 
while l <= r:
    # 답은 r-l+1즉 R의 총 갯수 + 왼쪽 또는 오른족에 있는 K의 갯수중 작은 값.
    ans = max(ans, r - l + 1 + 2 * min(left_K_cnt[l], rignt_K_count[r]))
    # l의 왼쪽에 있는 K의 갯수가 r의 오른쪽에 있는 K의 갯수보다 적으면 맞춰주기 위해 l을 오른쪽으로 땡김
    if left_K_cnt[l] < rignt_K_count[r]:
        l += 1
    else:
        r -= 1
print(ans)
