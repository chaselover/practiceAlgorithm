num = 0
end_flag = False
 
 
def get_status(map_, i, j, status):
    global num
 
    if map_[i][j] == ">":
        return "right"
    elif map_[i][j] == "<":
        return "left"
    elif map_[i][j] == "v":
        return "down"
    elif map_[i][j] == "^":
        return "up"
    elif map_[i][j] == "-":
        if num == 0:
            num = 15
            return status
        else:
            num -= 1
            return status
 
    elif map_[i][j] == "+":
        if num == 15:
            num = 0
            return status
        else:
            num += 1
            return status
 
    elif map_[i][j] == "_":
        if num == 0:
            return "right"
        else:
            return "left"
    elif map_[i][j] == ".":
        return status
    elif map_[i][j] == "@":
        return "end"
    elif map_[i][j] == "?":
        return "all"
    elif map_[i][j] == "|":
        if num == 0:
            return "down"
        else:
            return "up"
 
    elif map_[i][j].isnumeric():
        num = int(map_[i][j])
        return status
 
    else:
        return "right"
 
 
def search(map_, i, j, r, c, status, vi_dict):
    global end_flag
 
    if status == "right":
        if j + 1 < c and not end_flag:
            s = get_status(map_, i, j + 1, status)
            if not str(i) + "." + str(j + 1) + "." + status + "." + str(num) in vi_dict:
                vi_dict[str(i) + "." + str(j + 1) + "." + status + "." + str(num)] = 1
                search(map_, i, j + 1, r, c, s, vi_dict)
            else:
                return
        elif j + 1 >= c:
            s = get_status(map_, i, 0, status)
            if not str(i) + "." + str(0) + "." + status + "." + str(num) in vi_dict:
                vi_dict[str(i) + "." + str(0) + "." + status + "." + str(num)] = 1
                search(map_, i, 0, r, c, s, vi_dict)
            else:
                return
 
    elif status == "left":
        if j - 1 >= 0 and not end_flag:
            s = get_status(map_, i, j - 1, status)
            if not str(i) + "." + str(j - 1) + "." + status + "." + str(num) in vi_dict:
                vi_dict[str(i) + "." + str(j - 1) + "." + status + "." + str(num)] = 1
                search(map_, i, j - 1, r, c, s, vi_dict)
            else:
                return
        elif j - 1 < 0:
            s = get_status(map_, i, c - 1, status)
            if not str(i) + "." + str(c - 1) + "." + status + "." + str(num) in vi_dict:
                vi_dict[str(i) + "." + str(c - 1) + "." + status + "." + str(num)] = 1
                search(map_, i, c - 1, r, c, s, vi_dict)
            else:
                return
 
    elif status == "down":
        if i + 1 < r and not end_flag:
            s = get_status(map_, i + 1, j, status)
            if not str(i + 1) + "." + str(j) + "." + status + "." + str(num) in vi_dict:
                vi_dict[str(i + 1) + "." + str(j) + "." + status + "." + str(num)] = 1
                search(map_, i + 1, j, r, c, s, vi_dict)
            else:
                return
        elif i + 1 >= r:
            s = get_status(map_, 0, j, status)
            if not str(0) + "." + str(j) + "." + status + "." + str(num) in vi_dict:
                vi_dict[str(0) + "." + str(j) + "." + status + "." + str(num)] = 1
                search(map_, 0, j, r, c, s, vi_dict)
            else:
                return
 
    elif status == "up":
        if i - 1 >= 0 and not end_flag:
            s = get_status(map_, i - 1, j, status)
            if not str(i - 1) + "." + str(j) + "." + status + "." + str(num) in vi_dict:
                vi_dict[str(i - 1) + "." + str(j) + "." + status + "." + str(num)] = 1
                search(map_, i - 1, j, r, c, s, vi_dict)
            else:
                return
        elif i - 1 < 0:
            s = get_status(map_, r - 1, j, status)
            if not str(r - 1) + "." + str(j) + "." + status + "." + str(num) in vi_dict:
                vi_dict[str(r - 1) + "." + str(j) + "." + status + "." + str(num)] = 1
                search(map_, r - 1, j, r, c, s, vi_dict)
            else:
                return
 
    elif status == "all":
        if j + 1 < c and not end_flag:
            s = get_status(map_, i, j + 1, "right")
            if not str(i) + "." + str(j + 1) + "." + status + "." + str(num) in vi_dict:
                vi_dict[str(i) + "." + str(j + 1) + "." + status + "." + str(num)] = 1
                search(map_, i, j + 1, r, c, s, vi_dict)
            else:
                return
        elif j + 1 >= c:
            s = get_status(map_, i, 0, "right")
            if not str(i) + "." + str(0) + "." + status + "." + str(num) in vi_dict:
                vi_dict[str(i) + "." + str(0) + "." + status + "." + str(num)] = 1
                search(map_, i, 0, r, c, s, vi_dict)
            else:
                return
 
        if j - 1 >= 0 and not end_flag:
            s = get_status(map_, i, j - 1, "left")
            if not str(i) + "." + str(j - 1) + "." + status + "." + str(num) in vi_dict:
                vi_dict[str(i) + "." + str(j - 1) + "." + status + "." + str(num)] = 1
                search(map_, i, j - 1, r, c, s, vi_dict)
            else:
                return
        elif j - 1 < 0:
            s = get_status(map_, i, c - 1, "left")
            if not str(i) + "." + str(c - 1) + "." + status + "." + str(num) in vi_dict:
                vi_dict[str(i) + "." + str(c - 1) + "." + status + "." + str(num)] = 1
                search(map_, i, c - 1, r, c, s, vi_dict)
            else:
                return
 
        if i + 1 < r and not end_flag:
            s = get_status(map_, i + 1, j, "down")
            if not str(i + 1) + "." + str(j) + "." + status + "." + str(num) in vi_dict:
                vi_dict[str(i + 1) + "." + str(j) + "." + status + "." + str(num)] = 1
                search(map_, i + 1, j, r, c, s, vi_dict)
            else:
                return
        elif i + 1 > r:
            s = get_status(map_, 0, j, "down")
            if not str(0) + "." + str(j) + "." + status + "." + str(num) in vi_dict:
                vi_dict[str(0) + "." + str(j) + "." + status + "." + str(num)] = 1
                search(map_, 0, j, r, c, s, vi_dict)
            else:
                return
 
        if i - 1 >= 0 and not end_flag:
            s = get_status(map_, i - 1, j, "up")
            if not str(i - 1) + "." + str(j) + "." + status + "." + str(num) in vi_dict:
                vi_dict[str(i - 1) + "." + str(j) + "." + status + "." + str(num)] = 1
                search(map_, i - 1, j, r, c, s, vi_dict)
            else:
                return
        elif i - 1 < 0:
            s = get_status(map_, r - 1, j, "up")
            if not str(r - 1) + "." + str(j) + "." + status + "." + str(num) in vi_dict:
                vi_dict[str(r - 1) + "." + str(j) + "." + status + "." + str(num)] = 1
                search(map_, r - 1, j, r, c, s, vi_dict)
            else:
                return
 
    elif status == "end":
        end_flag = True
        return
 
 
def main():
    global num, end_flag
 
    tc = int(input())
    for t in range(1, tc+1):
        r, c = map(int, input().split())
        map_ = [[0]*c for _ in range(r)]
 
        for i in range(r):
            line = input()
            for j in range(c):
                map_[i][j] = line[j]
 
        if map_[0][0].isnumeric():
            num = int(map_[0][0])
        else:
            num = 0
 
        end_flag = False
        vi_dict = {}
        search(map_, 0, 0, r, c, get_status(map_, 0, 0, "right"), vi_dict)
 
        if end_flag:
            print("#%d YES" %(t))
        else:
            print("#%d NO" %(t))
 
 
if __name__ == '__main__':
    main()