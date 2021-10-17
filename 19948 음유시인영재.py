import sys
input = sys.stdin.readline

poem = input().rstrip()
title = ''.join([a[0].upper() for a in poem.split()])
poem += title + '.'
left_space = int(input())
left_push_alphabet = {idx: cnt for idx, cnt in enumerate(map(int, input().split()))}
for i in range(len(poem) - 1):
    if poem[i] == poem[i + 1]:
        continue
    if poem[i] == ' ':
        if left_space:
            left_space -= 1
        else:
            print(-1)
            exit()
    else:
        if left_push_alphabet[ord(poem[i].lower()) - 97]:
            left_push_alphabet[ord(poem[i].lower()) - 97] -= 1
        else:
            print(-1)
            exit()
else:
    print(title)