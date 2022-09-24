import sys
input = sys.stdin.readline



A = int(input())
An = list(map(int,input().split()))

stack = []
result = [-1]*A

stack.append(0)
i = 1

while stack and i < A:
    while stack and An[stack[-1]] < An[i]:
        result[stack[-1]] = An[i]
        stack.pop()

    stack.append(i)
    i+=1

for i in result:
    print(i, end = " ") 
# answer = ""
# for i in range(A):
#     if i==A-1:
#         answer += "-1"
#         break
#     for j in range(i+1,A):
#         if(An[i]<An[j]):
#             answer += f"{An[j]} "
#             break
#         if j==A-1 and (An[i]>=An[j]):
#             answer += "-1 "
# print(answer)