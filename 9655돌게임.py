import sys
input = sys.stdin.readline

N = int(input())
print('CY' if not N%4 else 'SK')