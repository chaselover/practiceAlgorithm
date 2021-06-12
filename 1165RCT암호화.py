n = list(input())
ans=[]

for i in range(len(n)):
    if n[i]==" ":
        ans.append(" ")
    elif n[i].islower() and ord(n[i])+13<=ord("z"):
        ans.append(chr(ord(n[i])+13))
    elif n[i].islower() and ord(n[i])+13>ord("z"):
        ans.append(chr(ord(n[i])-13))
    elif n[i].isupper() and ord(n[i])+13<=ord("Z"):
        ans.append(chr(ord(n[i])+13))
    elif n[i].isupper() and ord(n[i])+13>ord("Z"):
        ans.append(chr(ord(n[i])-13))
    elif n[i].isdigit():
        ans.append(str(n[i]))


print("".join(ans))