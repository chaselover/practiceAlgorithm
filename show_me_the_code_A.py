import sys
input = sys.stdin.readline


def dfs(depth, people, health, start, attack):
    global answer
    if depth == n:
        answer = max(answer, people)
        return
    for next_node in range(start, n):
        acc_attack = attack + attacks[next_node]
        new_health = health - acc_attack
        if new_health < 0:
            answer = max(answer, people)
            continue
        acc_attack = attack + attacks[next_node]
        dfs(depth + 1, people + populations[next_node], new_health, next_node + 1, acc_attack)
    
n, K = map(int, input().split()) 
attacks = list(map(int, input().split()))
populations = list(map(int, input().split()))
new_attacks = []
for i in range(n):
    new_attacks.append((attacks[i], populations[i]))
new_attacks.sort()
for i in range(n):
    attacks[i] = new_attacks[i][0]
    populations[i] = new_attacks[i][1]
answer = 0
dfs(0, 0, K, 0, 0)
print(answer)
