from math import log2
from collections import defaultdict

def get_prime_factor(num): 
    dic=defaultdict(int) 
    d=2 
    while d<=num: 
        if num%d==0: 
            dic[d]+=1 
            num=num/d 
        else: 
            d+=1

    primes=[] 
    for i in dic.keys(): 
        for j in range(dic[i]): 
            primes.append(str(i))
    return primes

def print_fibo(n):
    fibo_num = dp_fibo[i]
    if not n:
        print(f"Fib(0) = 0, lg does not exist")
    else:
        print(f"Fib({n}) = {fibo_num}, lg is {log2(fibo_num):.6f}")
    primes = get_prime_factor(fibo_num)
    if primes:
        print("Prime factors: ", end="")
        print(*primes)
    else:
        print("No prime factors")

def make_fibo_dp(n):
    i=0
    while dp_fibo[i] < n:
        i+=1
        dp_fibo[i]=int(1/(5**(1/2))*(((1+(5**(1/2)))/2)**i-((1-(5**(1/2)))/2)**i))
    return 

while 1:
    start,end = input().split()
    start = int(start,16)
    end = int(end,16)
    dp_fibo = [0]*(10000)
    if start>=end:
        exit()

    print(f"Range {start} to {end}:")

    make_fibo_dp(end**2)
    cnt=0
    for i in range(end+1):
        if start<=dp_fibo[i]<=end:
            print_fibo(i)
            cnt+=1

    if not cnt:
        print("No Fibonacci numbers in the range")
    print()
    

