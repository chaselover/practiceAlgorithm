import sys
input = sys.stdin.readline

minkyum = input().rstrip()

n = len(minkyum)
max_v = ''
left = 0
for i in range(n):
    if minkyum[i]=='K':
        max_v += '5' + '0'*(i - left)
        left = i+1
if minkyum[n-1] =='M':
    max_v += '1'*(n - left)

min_v = ''
left = 0
for i in range(n):
    if minkyum[i]=='K':
        if i>0 and minkyum[i-1]=='M':
            min_v += str(10**(i-left-1))
        min_v += '5'
        left = i+1
if minkyum[n-1] =='M':
    min_v += '1' + '0'*(n-1 - left)
print(max_v)
print(min_v)