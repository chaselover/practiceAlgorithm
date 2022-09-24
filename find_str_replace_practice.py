#coding: utf-8

#문자열 찾기 및 조작

data_str = "파이썬은 클래스를 이용해 객체를 생성하는 객체지향 프로그래밍 언어입니다."
mask_str = input("마스킹할 문자열을 입력하세요:")
find_str = input("찾을 문자열을 입력하세요:")
idx = -1
count = 1
while True:
    idx = data_str.find(find_str,idx+1)
    if idx != -1:
        print("[{0}]~[{1}]".format(idx,idx+len(find_str)-1))
        new_str = data_str.replace(find_str,mask_str,count)
        print(new_str)
        count += 1
    else:
        break
print(idx)