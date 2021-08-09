import sys

try_baby_gin = int(input())
cards = []
for _ in range(try_baby_gin):
    count_card = {i:0 for i in range(10)}
    one_try = list(map(int, list(input())))
    for card in one_try:
        count_card[card] += 1
    
    for num in range(10):
        if count_card[num]>=3:
            count_card[num] -= 3*(count_card[num]//3)
        if count_card[num] != 0:
            if count_card[num]%3==count_card[num+1]%3==count_card[num+2]%3:
                cnt= count_card[num]%3
                for i in range(3):
                    count_card[num+i] -= cnt
                continue
            else:
                print("Not Baby-gin")
                break
    else:
        print("Baby-gin")

        