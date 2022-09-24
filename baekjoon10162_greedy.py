import sys
###인풋
N = int(input())
strings = []

for _ in range(N):
    string = list(sys.stdin.readline())
    del string[-1]
    strings.append([len(string)]+string)

strings = sorted(strings,reverse=True)
del strings[0]


print(strings)