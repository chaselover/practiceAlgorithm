import sys
input = sys.stdin.readline

while True:
    memory = [0 for _ in range(32)]
    cal = 0
    pc = 0
    for i in range(32):
        try:
            memory[i] = int(input().rstrip(),2)
        except EOFError:
            exit()
    while True:
        adress = memory[pc]
        cmd = adress//32
        value = adress%32
        pc = (pc + 1)%32
        if cmd == 0:
            memory[value] = cal
        elif cmd == 1:
            cal = memory[value]
        elif cmd == 2:
            if not cal:
                pc = value
        elif cmd == 4:
            cal = (cal-1)%256
        elif cmd == 5:
            cal = (cal+1)%256
        elif cmd == 6:
            pc = value
        elif cmd == 7:
            break
    print(bin(cal)[2:].zfill(8))

##다른사람
import sys
i,b,f=int,bin,'%08d'
while 1:
 p,a,m=0,0,list(map(lambda x:i(next(sys.stdin),2),range(32)))
 if len(m)!=32:break
 while 1:
  o,x=(lambda s:(lambda s:[i(s[:3],2),i(s[3:],2)])((lambda s:f%(i(b(s)[2:])))(s)))(m[p])
  p=(p+1)%32
  if o==0:m[x]=a
  if o==1:a=m[x]
  if o==2 and a==0:p=x
  if o==4:a=(a+255)%256
  if o==5:a=(a+1)%256
  if o==6:p=x
  if o==7:break
 print(f%(i(b(a)[2:])))


# 다른사람
 import sys
while 1:
    M=[]
    for i in range(32):
        s=sys.stdin.readline()
        if not s: exit()
        M.append(s)
    p=0;a=0
    while p<32:
        i=int(M[p][:3],2);x=int(M[p][3:],2)
        p=(p+1)%32
        if i==0: M[x]=format(a,'08b')
        elif i==1: a=int(M[x],2)
        elif i==2: 
            if a==0: p=x
        elif i==4: a=(a-1)%256
        elif i==5: a=(a+1)%256
        elif i==6: p=x
        elif i==7: break
    print(format(a,'08b'))


# 다른사람
import sys
input = sys.stdin.readline

while 1:
    m, p, a = [0 for _ in range(32)], 0, 0

    for i in range(32):
        try:
            m[i] = int(input().rstrip(), 2)
        except:
            exit()

    while 1:
        o, v = m[p] // 32, m[p] % 32
        p = (p + 1) % 32

        if o == 0:
            m[v] = a
        elif o == 1:
            a = m[v]
        elif o == 2:
            p = v if a == 0 else p
        elif o == 4:
            a = (a - 1) % 256
        elif o == 5:
            a = (a + 1) % 256
        elif o == 6:
            p = v
        elif o == 7:
            break

    print(bin(a)[2:].zfill(8))