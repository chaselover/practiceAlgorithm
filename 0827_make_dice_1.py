def dfs(depth,target,nums,n,check,dice):
    if depth == target:
        answers.append(int(nums))
        return
    for dice_number in range(n):
        if not check[dice_number]:
            for number in dice[dice_number]:
                if not depth and not number:
                    continue
                check[dice_number] = True
                dfs(depth+1,target,nums+str(number),n,check,dice)
                check[dice_number] = False


def solution(dice):
    global answers
    dice_n = len(dice)
    dice_check = [False for _ in range(dice_n)]
    answers = []
    for i in range(1,dice_n+1):
        dfs(0,i,'',dice_n,dice_check,dice)
    for i in range(1,10**dice_n):
        if i not in answers:
            return i

print(solution([[1, 6, 2, 5, 3, 4], [9, 9, 1, 0, 7, 8]]))