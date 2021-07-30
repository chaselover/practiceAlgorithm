import sys
input = sys.stdin.readline

A = int(input(), 2) 
B = int(input(), 2)
print(bin(A & B)[2:].zfill(100000)) 
print(bin(A | B)[2:].zfill(100000)) 
print(bin(A ^ B)[2:].zfill(100000)) 
print(bin(A ^ (1<<100000)-1)[2:].zfill(100000)) 
print(bin(B ^ (1<<100000)-1)[2:].zfill(100000))

