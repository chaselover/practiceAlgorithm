import sys
input = sys.stdin.readline
N = int(input())
cnt=0
for _ in range(N):
    chr_set = {i:0 for i in range(97,123)}
    word = input().rstrip()
    for i in range(len(word)):
        if chr_set[ord(word[i])]==1:
            break
        if i<len(word)-1 and word[i] != word[i+1]:
            chr_set[ord(word[i])]=1
    else:
        cnt+=1
print(cnt)
    

# 빠른풀이. sort의 key 값을 이용해 정렬 순서를 조작한다. s.find즉 빨리나오는 알파뱃의 인덱스 순서대로 정렬(그룹단어체크를 강제로 만든다.)
# res = 0
# for i in range(int(input())):
#     s = input()
#     if list(s) == sorted(s, key=s.find):
#         res += 1
# print(res)