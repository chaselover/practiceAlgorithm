#coding: utf-8

#Lotto.py

import random

lotto = random.sample(range(1,46,1),6)

print(sorted(lotto))

def input_start():
    start = 0
    try:
        start = int(input("로또 번호의 시작 번호를 입력하세요(기본값1):"))
    except:
        start = 1
    finally:
        return start

def input_end():
    try:
        end = int(input("로또 번호의 끝 번호를 입력하세요(기본값45):"))
    except:
        end = 45
    finally:
        return end

def input_count():
    count = 0
    try:
        count = int(input("로또 공의 개수를 입력하세요(기본값6):"))
    except:
        count = 6
    finally:
        return count

def print_lotto(start, end, count):
    lotto = random.sample(range(start,end+1,1), count)
    print("행운의 로또 번호는", end="")
    print(sorted(lotto), end = "")
    #리스트 기호[]삭제
    for i, num in enumerate(sorted(lotto)):
        if i == len(lotto) -1:#마지막일시
            print("{0}".format(num),end="")
        else:#마지막이 아닐시
            print("{0}".format(num),end="")

    print("입니다.")

    print_lotto(1,45,6)