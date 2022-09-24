S = list(input())
main = ''
check = 0
stack = []
for i in range(len(S)):
    if check == 0:
        if S[i] == "<":
            check = 1
            while stack:
                main += stack.pop()
            main += S[i]
        elif S[i] == " ":
            while stack:
                main += stack.pop()
            main += S[i]
        else:
            stack.append(S[i])
    else:
        main += S[i]
        if S[i] ==">":
            check=0
while stack:
    main += stack.pop()

print(main)