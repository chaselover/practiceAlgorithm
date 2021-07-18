moem = ['a','i','y','e','o','u']
zaem = ['b','k','x','z','n','h','d','c','w','g','p','v','j','q','t','s','r','l','m','f']

# 무한입력. try except
while 1:
    try:
        S = input()
        ans = ""
        for i in range(len(S)):
            if S[i].lower() in moem:
                if S[i].isupper():
                    k = S[i].lower()
                    for j in range(6):
                        if moem[j] == k:
                            a = moem[(j+3)%6]
                            ans += a.upper()
                elif S[i].islower():
                    for j in range(6):
                        if moem[j] == S[i]:
                            a = moem[(j+3)%6]
                            ans += a
            elif S[i].lower() in zaem:
                if S[i].isupper():
                    k = S[i].lower()
                    for j in range(20):
                        if zaem[j] == k:
                            a = zaem[(j+10)%20]
                            ans += a.upper()
                elif S[i].islower():
                    for j in range(20):
                        if zaem[j] == S[i]:
                            a = zaem[(j+10)%20]
                            ans += a
            else:
                ans += S[i]

        print(ans)
    except:
        break