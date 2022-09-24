sentence = list(input().strip())

if len(sentence)==0:
    print(0)
else:
    print(sentence.count(" ")+1) 