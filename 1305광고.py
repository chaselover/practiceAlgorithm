import sys
input = sys.stdin.readline

L = int(input()) # 광고판 길이
s = input().rstrip() # 광고판 문자열
s_len = len(s)

# 실패함수 ( KMP 패턴 부분 일치 테이블 만들기)
p_table = [0 for _ in range(s_len)]
j = 0
for i in range(1, s_len):
    while j > 0 and s[i]!=s[j]:
        j = p_table[j-1]
    if s[i]==s[j]:
        j+=1
        p_table[i] = j

p_len = s_len - p_table[s_len-1] # 가장짧은 광고길이
print(p_len)