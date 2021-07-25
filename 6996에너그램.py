import sys
input = sys.stdin.readline


# chr count해서 charset의 숫자가 전부 0이어야 통과.
for test in range(int(input())):
    A,B = input().split()
    chrSet = [0]*26
    for chr in A:
        chrSet[ord(chr) - 97] +=1
    for chr in B:
        chrSet[ord(chr) - 97] -=1
    
    print(f'{A} & {B} are anagrams.' if not any(chrSet) else f'{A} & {B} are NOT anagrams.')
