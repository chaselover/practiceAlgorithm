import base64

tc=int(input())
 
for i in range(1,tc+1):
    base64str=input()
    base64_bytes = base64.b64decode(base64str)
    string = base64_bytes.decode('ascii')
    print("{} {}".format(i,string))