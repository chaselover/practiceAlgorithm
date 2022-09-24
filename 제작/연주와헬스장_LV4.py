# 연주와헬스장_LV4.py
"""
하루 운동에 대한 선택은 실시 할 때마다 해당 기구의 운동 효율이 줄어들기 때문에 dfs로 3세트의 운동 조합을 산출했습니다.
dfs의 결과 최대 무게 증량이 가능한 운동 조합값을 하루단위로 저장할 maxw_a_day, used_a_day 변수로 
하루의 증량과 사용한 기구를 전역으로 관리했습니다.

각 세트가 지날 때마다 이용자의 위치는 하루동안 동일하기 때문에 change_locations_each_set 함수를 통해 
dfs전 미리 연산해 others, others_1, others_2로 전역관리했습니다.

하루 운동이 끝나면 그 날 이용한 기구들에 대해 근육통 counter인 exhausted 딕셔너리에 갱신을 해준 후 
maxw_a_day를 cur_weight에 더해 최대 중량을 갱신합니다.
다음날 이용자들 위치 연산을 위해 change_locations 함수를 통해 다음날 위치를 산출 해 주었고
근육통이 지속되는 날짜에 대해 exhausted를 순회하며 1씩 감산 해주었습니다.
근육통이 끝나면 근육통 배열에서 삭제했습니다.
"""

# 하루 운동할 때 3세트 운동한다.
def exercise(chosen, total, machines, gym):
    global exhausted, maxw_a_day, used_a_day, others, others_1, others_2
    n = len(gym)
    k = len(chosen)
    # 진행한 세트 수에 따라 사람들의 위치가 바뀌거나 최대값들이 갱신된다.
    if k == 0:
        tmp_others = others
    elif k == 1:
        tmp_others = others_1
    elif k == 2:
        tmp_others = others_2
    elif k == 3:
        if maxw_a_day < total:
            maxw_a_day = total
            used_a_day = chosen
        return
    for i in range(n):
        for j in range(n):
            # 다른 사람이 쓰고있는 운동 기구는 쓰지 않습니다.
            if (i, j) not in tmp_others:
                # 선택하면 효율성 반으로.
                machine_id = gym[i][j]
                earn_weight = machines[machine_id] 
                if machine_id in exhausted:
                    earn_weight //= 2
                for choose in chosen:
                    if machine_id == choose:
                        earn_weight //= 2
                exercise(chosen + [machine_id],  total + earn_weight, machines, gym)

# 하루 지날 때 헬스장 이용자들의 위치 변화
def change_locations(others, n):
    ret = {}
    for other in others:
        x, y = other
        d = (others[other] + 1) % 4
        ret[(y, n - x - 1)] = d
    return ret

# 한 세트 지날 때 헬스장 이용자들의 위치 변화
def change_locations_each_set(others, n):
    delta = ((0, 1), (1, 0), (0, -1), (-1, 0))
    ret = {}
    for other in others:
        x, y = other
        d = others[other]
        dx, dy = x + delta[d][0], y + delta[d][1]
        if dx < 0 or dx >= n or dy < 0 or dy >= n:
            d = (d + 2) % 4
            dx, dy = x + delta[d][0], y + delta[d][1]
        ret[dx, dy] = d
    return ret


def solution(cur_weight, gym, peoples, machines):
    global maxw_a_day, exhausted, used_a_day, others, others_1, others_2
    days = 0
    exhausted = {}
    # 다른 사람들 위치 dictionary에 저장.
    others = {}
    for x, y, d in peoples:
        others[(x, y)] = d
    while cur_weight < 500:
        maxw_a_day, used_a_day = 0, []
        # 각 세트를 운동 한 후 헬스장 상태.
        others_1 = change_locations_each_set(others, len(gym))
        others_2 = change_locations_each_set(others_1, len(gym))
        # 하루 운동해서 최댓값 증량
        exercise([], 0, machines, gym)
        cur_weight += maxw_a_day
        for each in used_a_day:
            exhausted[each] = 3
        # 사람들 위치 변경
        others = change_locations(others_2, len(gym))
        # 날짜 변동
        days += 1
        # 날이 지나면 근육통 count - 1
        finish_exhausted = []
        for each_exercise in exhausted:
            exhausted[each_exercise] -= 1
            if not exhausted[each_exercise]:
                finish_exhausted.append(each_exercise)
        for fin in finish_exhausted:
            del exhausted[fin]
    return days



if __name__ == "__main__":
    print(solution(3, [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]], [[1, 2, 3], [3, 4, 2], [0, 4, 2]], [100, 2, 3, 4, 5]))