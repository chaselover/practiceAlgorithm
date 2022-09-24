import sys
input = sys.stdin.readline
from math import factorial

N,M,K = map(int,input().split())

# N개중에 M개를 뽑는 전체 경우의 수 중에 M개중에 K개를 뽑는 경우
answer = (factorial(M)*factorial(N-M)*factorial(M)*factorial(N-K))/(factorial(K)*factorial(M-K)*factorial(N)*factorial(N-M)*factorial(M-K))
print(answer)