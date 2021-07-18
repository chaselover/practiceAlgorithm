import sys
input = sys.stdin.readline



A = int(input())
An = list(map(int,input().split()))

stack = []
result = [-1]*A

stack.append(0)
i = 1

# i 즉 인덱스가 A-1때까지 돌린다.
while stack and i < A:
    # 큰걸찾으면 stack에서 빠지면서 result에 저장해.
    # stack에 차있던것들(오큰수 못찾았던 것들) 쭉 비우면서 진행
    # An[i]보다 크거나 작은수 나오면 스탑하고 다시 stack채우기 진행.
    # 결국 끝까지stack에 남으면 -1
    while stack and An[stack[-1]] < An[i]:
        result[stack[-1]] = An[i]
        print(stack, result)
        stack.pop()

    stack.append(i)
    i+=1
    print(stack, result)

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