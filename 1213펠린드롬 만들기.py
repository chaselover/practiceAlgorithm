import sys
input = sys.stdin.readline
from collections import defaultdict

name = input().rstrip()
count = defaultdict(int)
for char in name:
    count[char] += 1
char_set = []
flag = 0
mid = ''
for char in count:
    if count[char] % 2:
        if flag:
            print("I'm Sorry Hansoo")
            exit()
        else:
            mid = char
            flag = 1
            for _ in range(count[char] // 2):
                char_set.append(char)
    else:
        for _ in range(count[char] // 2):
            char_set.append(char)
char_set.sort()
answer = ''.join(char_set)
print(answer + mid + answer[::-1])