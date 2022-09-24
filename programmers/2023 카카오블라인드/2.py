def solution(cap, n, deliveries, pickups):
    answer = 0
    d_turn, p_turn = [], []
    tmp_d, tmp_p = cap, cap
    for idx in range(n - 1, -1, -1):
        if deliveries[idx]:
            if tmp_d == cap:
                d_turn.append(idx)
            if tmp_d > deliveries[idx]:
                tmp_d -= deliveries[idx]
            elif tmp_d == deliveries[idx]:
                tmp_d -= deliveries[idx]
            else:
                while deliveries[idx]:
                    deliveries[idx] -= tmp_d
                    if deliveries[idx] > tmp_d:
                        d_turn.append(idx)
                    tmp_d = cap
        if pickups[idx]:
            if tmp_p == cap:
                p_turn.append(idx)
            if tmp_p > pickups[idx]:
                tmp_p -= pickups[idx]
            elif tmp_p == pickups[idx]:
                tmp_p -= pickups[idx]
            else:
                while pickups[idx]:
                    pickups[idx] -= tmp_p
                    if pickups[idx] > tmp_p:
                        p_turn.append(idx)
                    tmp_p = cap
    max_length = min(p_turn, d_turn)
    for i in range(max_length):
        answer += 2 * max(p_turn[i], d_turn[i])
        
                    
    return answer
print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))