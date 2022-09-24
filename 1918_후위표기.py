
a = input()
stack = [] #스택
res='' #출력

for x in a:
    if x.isalpha(): #피연산자인지 아닌지 확인
        res+=x
    else:
        if x == '(':
            stack.append(x)
        elif x == '*' or x =='/':
            while stack and (stack[-1]=='*' or stack[-1]=='/'):
                res+=stack.pop()
            stack.append(x)
        elif x == '+' or x == '-':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(x)
        elif x == ')':
            while stack and stack[-1] != '(':
                res+=stack.pop()
            stack.pop()

#스택안에 남아있는 값들 pop            
while stack:
    res += stack.pop()
print(res)