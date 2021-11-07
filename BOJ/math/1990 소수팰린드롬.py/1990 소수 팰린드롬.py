def check_is_primary_num(num): 
    for i in range(2, int(num**0.5) + 1): 
        if num % i == 0: 
            return False 
    return True 

def check_is_palindrome(num): 
    is_palindrome = False 
    num = str(num) 
    if num == num[::-1]: 
        is_palindrome = True 
    return is_palindrome 

def solution(A, B): 
    if B > 10000000: 
        B = 10000000 
    palindrome_numbers = [num for num in range(A, B + 1) if check_is_palindrome(num)] 
    primary_nums = [num for num in palindrome_numbers if check_is_primary_num(num)] 
    for num in primary_nums: 
        print(num) 
    print("-1") 

if __name__ == "__main__": 
    A, B = map(int, input().split()) 
    solution(A, B)


# 풀이 2
from sys import stdout
print = stdout.write
a,b = map(int, input().split())

if b > 10000000:
    b = 10000000
def solv():
    candidate = set_candidate()
    answer = []
    for num in candidate:
        if a <= num <= b:
            if is_prime(num):
                answer.append(num)
    if answer:
        answer.sort()
        for num in answer:
            print('%d\n'%num)
    print('-1')
def set_candidate():
    candidate = []
    for num in range(1,10000):
        if num < 10:
            if num%2==1:
                candidate.append(num)
                candidate.append(num*10+num)

        elif num < 100:
            num1 = str(num)
            num1 = int(num1+num1[::-1])
            if num1%2==1:
                candidate.append(num1)

            num2 = str(num)
            num2 = int(num2+num2[0])
            if num2%2==1:
                candidate.append(num2)
        elif num < 1000:
            num1 = str(num)
            num1 = int(num1 + num1[::-1])
            if num1%2==1:
                candidate.append(num1)

            num2 = str(num)
            num2 = int(num2+num2[1]+num2[0])
            if num2%2==1:
                candidate.append(num2)
        elif num < 10000:
            num = str(num)
            num = int(num+num[2]+num[1]+num[0])
            if num%2==1:
                candidate.append(num)

    return candidate
def is_prime(num):
    for i in range(2,int(num**(1/2))+1):
        if num%i == 0:
            return False
    return True
solv()