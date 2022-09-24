import sys
input = sys.stdin.readline

L = int(input()) # 광고판 길이
string = input().rstrip() # 광고판 문자열
string_length = len(string)

# 실패함수 ( KMP 패턴 부분 일치 테이블 만들기)
pattern_table = [0 for _ in range(string_length)]
count = 0
for idx in range(1, string_length):
    while count > 0 and string[idx]!=string[count]:
        count = pattern_table[count-1]
    if string[idx]==string[count]:
        count+=1
        pattern_table[idx] = count

pattern_length = string_length - pattern_table[string_length-1] # 가장짧은 광고길이
print(pattern_length)