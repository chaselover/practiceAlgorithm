

import sys
input = sys.stdin.readline

n=int(input())
str=input().rstrip()
nums=[0]*n
for i in range(n):
    nums[i]=int(input().rstrip())
stack=[]

for ch in str:
    #문자이면
    if ch.isupper():
        #nums[해당 문자의 아스키코드에 해당하는 index]
        stack.append(nums[ord(ch)-ord('A')])
    #연산자이면
    else:
        #뒤에 추가된 숫자먼저 빼오고
        #이전에 추가된 숫자빼오기
        num2=stack.pop()
        num1=stack.pop()
        if ch=='+':
            stack.append(num1+num2)
        elif ch=='-':
            stack.append(num1-num2)
        elif ch=='/':
            stack.append(num1/num2)
        elif ch=='*':
            stack.append(num1*num2)
#소수점 두자리까지 출력하는 방법
print(f"{stack[0]:.2f}")