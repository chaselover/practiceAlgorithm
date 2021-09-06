cnt = 0
for char in bin(int(input())):
    if char == '1':
        cnt += 1
print(cnt)