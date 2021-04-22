
string_1 = list(input())
string_2 = list(input())
string_3 = list(input())
max_cnt = []

for i in range(len(string_1)):
    index2 = string_2.find(string_1[i])
    index3 = string_3.find(string_1[i])

    if index2 != -1 and index3 != -1:
        cnt=1
        j=1
        while 1:
            if string_1[i+j] == string_2[index2+j] and string_2[index2+j] == string_3[index3+j]:
                cnt+=1
                j+=1
            else:
                max_cnt.append(cnt)
                break
    else:
        continue

print(max(max_cnt))