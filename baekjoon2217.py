fomula = list(input())

while fomula[0] == '0':
    del fomula[0]

fomula = ''.join(fomula)
fomula = fomula.split('-')

i=0

while i != len(fomula):
    fomula[i] = eval(fomula[i])
    i += 1

fomula = list(map(str,fomula))
answer = eval('-'.join(fomula))


print(answer)