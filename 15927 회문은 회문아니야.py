import sys
input = sys.stdin.readline

s = input().rstrip()
n = len(s)
start = 0
end = n-1
s_dic = {i:0 for i in range(26)}
while True:
    
