import sys
input = sys.stdin.readline

string = input()
stack = [] #스택
res='' #출력

for ch in string:
    if ch.isalpha(): #피연산자인지 아닌지 확인
        res+=ch
    else:
        if ch == '(':
            stack.append(ch)
        elif ch == '*' or ch =='/':             #안에꺼 다 빼고 넣음(그 자리에서 연산하기 위해서) -> 연산 우선순위가 있기 때문에 안에있는애들을 다빼야 제자리에 들어갈 수 있음.
            while stack and (stack[-1]=='*' or stack[-1]=='/'):
                res+=stack.pop()
            stack.append(ch)
        elif ch == '+' or ch == '-':            #괄호 닫힐때 연산
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(ch)
        elif ch == ')':                         #닫히면 괄호 없어질때까지 출력(연산)
            while stack and stack[-1] != '(':
                res+=stack.pop()
            stack.pop()

#스택안에 남아있는 값들 pop            
while stack:
    res += stack.pop()
print(res)