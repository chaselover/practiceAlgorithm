word = list(input())
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
print_list = [-1]*26
cnt = 0

for i in range(len(word)):
    for j in range(26):
        if word[i] ==alphabet[j]:
            if print_list[j] != -1:
                cnt+=1
            else:
                print_list[j] = cnt
                cnt +=1

print(*print_list)