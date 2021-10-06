from collections import defaultdict

while True:
    try:
        a=input()
        b=input()
        alpha1=defaultdict(int)
        alpha2=defaultdict(int)
        ans=''
        for s in a:
            alpha1[s]+=1
        for s in b:
            alpha2[s]+=1
        s = []
        for char in alpha1:
            if char in alpha2:
                s.append(char)
        s.sort()
        for char in s:
            ans += char*min(alpha1[char],alpha2[char])
        print(ans)
    except:
        break
# 다른코드
try:
 while 1:
  a=input();b=input();l=[]
  for i in a:
   if i in b:
       l+=[i];
       b=b.replace(i,"",1)
  l.sort();
  print("".join(l))
except:
    pass
# 다른코드
while True :
    try :
        a=input()
        b=input()
    except :
        break
    ans = ""
    s = "abcdefghijklmnopqrstuvwxyz"
    for i in s :
        cnt = min(a.count(i), b.count(i))
        ans += i*cnt
    print (ans)
