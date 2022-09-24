word = list(input())
c_word=[]
list_word = []
for a in word:
    if 97<=ord(a)<=122:
        a = chr(ord(a)-32)
    c_word.append(a)
    cnt = c_word.count(a)
    list_word.append([cnt,a])

list_word.sort(reverse=True)
if len(list_word)==1:
    print(list_word[0][1])
elif list_word[0][0]==list_word[1][0]:
    print("?")
else:
    print(list_word[0][1])