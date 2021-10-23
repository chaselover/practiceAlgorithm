import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

class Algorithm():
    def __init__(self,num):
        self.num = num
        self.min_heap = []
        self.max_heap = []
    def insert(self,pb_num,diff):
        heapq.heappush(self.min_heap,(diff,pb_num))
        heapq.heappush(self.max_heap,(-diff,-pb_num))
    def find_heap(self,flag):
        result = []
        if flag > 0:
            if self.max_heap:
                while (-self.max_heap[0][1] not in number_set) or number_algo[-self.max_heap[0][1]][0] != self.num or number_algo[-self.max_heap[0][1]][1] != -self.max_heap[0][0]:
                    heapq.heappop(self.max_heap)
                    if not self.max_heap:
                        break
            if self.max_heap:
                result = [-self.max_heap[0][0],-self.max_heap[0][1]]
        else:
            if self.min_heap:
                while (self.min_heap[0][1] not in number_set) or number_algo[self.min_heap[0][1]][0] != self.num or number_algo[self.min_heap[0][1]][1] != self.min_heap[0][0]:
                    heapq.heappop(self.min_heap)
                    if not self.min_heap:
                        break
            if self.min_heap:
                result = self.min_heap[0]
        return result


class Difficulty():
    def __init__(self,num):
        self.num = num
        self.min_heap = []
        self.max_heap = []

    def insert(self,pb_num):
        heapq.heappush(self.min_heap,pb_num)
        heapq.heappush(self.max_heap,-pb_num)
    def find_heap(self,x):
        result = []
        if x > 0:
            if self.min_heap:
                while self.min_heap[0] not in number_set or (number_algo[self.min_heap[0]][1]) != self.num:
                    heapq.heappop(self.min_heap)
                    if not self.min_heap:
                        break
            if self.min_heap:
                result = self.min_heap[0]

        else:
            if self.max_heap:
                while -self.max_heap[0] not in number_set or (number_algo[-self.max_heap[0]][1]) != self.num:
                    heapq.heappop(self.max_heap)
                    if not self.max_heap:
                        break
            if self.max_heap:
                result = -self.max_heap[0]
        return result


N = int(input())
algo_set = set()
diff_set = set()
algo_dict = {}
diff_dict = {}
number_algo = {}
number_set = set()
for _ in range(N):
    number,dif,algo = map(int,input().split())
    if algo not in algo_set:
        algo_dict[algo] = Algorithm(algo)
        algo_set.add(algo)
    if dif not in diff_set:
        diff_dict[dif] = Difficulty(dif)
        diff_set.add(dif)
    algo_dict[algo].insert(number,dif)
    diff_dict[dif].insert(number)
    number_algo[number] = [algo,dif]
    number_set.add(number)


M = int(input())

for i in range(M):
    command,*arg = input().split()
    if command == 'recommend':
        G,x = map(int,arg)
        print(algo_dict[G].find_heap(x)[1])
    elif command == 'recommend2':
        x = int(arg[0])
        diff_check = 0 if x == 1 else float('inf')
        pb_num_check = -1
        for algo_num in algo_dict:
            ch = algo_dict[algo_num].find_heap(x)
            if not ch: continue
            if x == 1:
                if ch[0] >diff_check:
                    diff_check = ch[0]
                    pb_num_check = ch[1]
                elif ch[0] == diff_check:
                    if pb_num_check < ch[1]:
                        pb_num_check = ch[1]
            else:
                if ch[0] < diff_check:
                    diff_check = ch[0]
                    pb_num_check = ch[1]
                elif ch[0] == diff_check:
                    if pb_num_check > ch[1]:
                        pb_num_check = ch[1]
        print(pb_num_check)
    elif command == 'recommend3':
        flag,L_num = map(int,arg)
        result = -1
        if flag == -1:
            L_num = L_num + flag
        while 0<=L_num<=100:
            if L_num in diff_set:
                ch = diff_dict[L_num].find_heap(flag)
                if not ch:
                    L_num = L_num + flag
                    continue
                result = ch
                print(ch)
                break
            L_num = L_num + flag
        if result == -1:
            print(-1)

    elif command == 'solved':
        pb_num = int(arg[0])
        number_set.remove(pb_num)
        del number_algo[pb_num]
    else:
        pb_num,diff_num,algo_num = map(int,arg)
        if algo_num not in algo_set:
            algo_dict[algo_num] = Algorithm(algo_num)
            algo_set.add(algo_num)
        if diff_num not in diff_set:
            diff_dict[diff_num] = Difficulty(diff_num)
            diff_set.add(diff_num)
        algo_dict[algo_num].insert(pb_num,diff_num)
        diff_dict[diff_num].insert(pb_num)
        number_algo[pb_num] = [algo_num,diff_num]
        number_set.add(pb_num)



# 2
import sys, heapq
input = sys.stdin.readline

n = int(input())

algo_dict = {}
level_dict = {}
problem = {}


problem_min_heap = []
problem_max_heap = []

for _ in range(n):
    pb_num, level, al_num = map(int, input().split())
    # solved했는지 안 했는지 check
    problem[pb_num] = [level, al_num]
    # Recommend 2를 위한 heapq
    heapq.heappush(problem_min_heap, (level, pb_num))
    heapq.heappush(problem_max_heap, (-level, -pb_num))
    # Algorithm Dict
    if algo_dict.get(al_num) is not None:
        # min_heap
        heapq.heappush(algo_dict[al_num][0], (level, pb_num))
        # max_heap
        heapq.heappush(algo_dict[al_num][1], (-level, -pb_num))
    else:
        min_heap = []
        max_heap = []
        heapq.heappush(min_heap, (level, pb_num))
        heapq.heappush(max_heap, (-level, -pb_num))
        algo_dict[al_num] = [min_heap, max_heap]
    # level Dict
    if level_dict.get(level) is not None:
        heapq.heappush(level_dict[level][0], pb_num)
        heapq.heappush(level_dict[level][1], -pb_num)
    else:
        min_heap = []
        max_heap = []
        heapq.heappush(min_heap, pb_num)
        heapq.heappush(max_heap, -pb_num)
        level_dict[level] = [min_heap, max_heap]

m = int(input())

for _ in range(m):
    command, *args = list(input().rstrip().split())
    if command == "recommend":
        al_num, x = list(map(int, args))
        if x == 1:
            top = (algo_dict[al_num][1])[0]
            while -top[0] != problem[-top[1]][0] or al_num != problem[-top[1]][1]:
                heapq.heappop(algo_dict[al_num][1])
                top = (algo_dict[al_num][1])[0]
            print(-top[1])
        else :
            top = (algo_dict[al_num][0])[0]
            while top[0] != problem[top[1]][0] or al_num != problem[top[1]][1]:
                heapq.heappop(algo_dict[al_num][0])
                top = (algo_dict[al_num][0])[0]
            print(top[1])

    elif command == "recommend2":
        x = int(args[0])
        if x == 1:
            while -problem_max_heap[0][0] != problem[-problem_max_heap[0][1]][0]:
                heapq.heappop(problem_max_heap)
            print(-problem_max_heap[0][1])    
        else:
            while problem_min_heap[0][0] != problem[problem_min_heap[0][1]][0]:
                heapq.heappop(problem_min_heap)
            print(problem_min_heap[0][1])
    elif command == "recommend3":
        x, level = list(map(int, args))
        success = False
        if x == 1:
            for lev in range(level, 101):
                if level_dict.get(lev) is not None:
                    while len(level_dict[lev][0]) > 0 and lev != problem[(level_dict[lev][0])[0]][0]:
                        heapq.heappop(level_dict[lev][0])
                    if len(level_dict[lev][0]) == 0:
                        continue
                    print((level_dict[lev][0])[0])
                    success = True
                    break
            if not success:
                print(-1)
        else :
            for lev in range(level-1, 0, -1):
                if level_dict.get(lev) is not None:
                    while len(level_dict[lev][1]) > 0 and lev != problem[-(level_dict[lev][1])[0]][0]:
                        heapq.heappop(level_dict[lev][1])
                    if len(level_dict[lev][1]) == 0:
                        continue
                    print(-(level_dict[lev][1])[0])
                    success = True
                    break
            if not success:
                print(-1)
    elif command == "add":
        pb_num, level, al_num = list(map(int, args))
        problem[pb_num] = [level, al_num]
        heapq.heappush(problem_min_heap, (level, pb_num))
        heapq.heappush(problem_max_heap, (-level, -pb_num))
        if algo_dict.get(al_num) is not None:
            # min_heap
            heapq.heappush(algo_dict[al_num][0], (level, pb_num))
            # max_heap
            heapq.heappush(algo_dict[al_num][1], (-level, -pb_num))
        else:
            min_heap = []
            max_heap = []
            heapq.heappush(min_heap, (level, pb_num))
            heapq.heappush(max_heap, (-level, -pb_num))
            algo_dict[al_num] = [min_heap, max_heap]
        # level Dict
        if level_dict.get(level) is not None:
            heapq.heappush(level_dict[level][0], pb_num)
            heapq.heappush(level_dict[level][1], -pb_num)
        else:
            min_heap = []
            max_heap = []
            heapq.heappush(min_heap, pb_num)
            heapq.heappush(max_heap, -pb_num)
            level_dict[level] = [min_heap, max_heap]
    elif command == "solved":
        pb_num = int(args[0])
        problem[pb_num] = [0, 0]
