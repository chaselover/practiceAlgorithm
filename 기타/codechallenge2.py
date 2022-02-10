


def solution(grid):
    d = ((1,0),(0,-1),(-1,0),(0,1))
    results = []
    rows = len(grid)
    cols = len(grid[0])
    visited = {(i,j,d): False for i in range(rows) for j in range(cols) for d in range(4)}
    for i in range(rows):
        for j in range(cols):
            for di in range(4):
                if visited[(i,j,di)]:
                    continue
                length = 1
                x, y, di = i, j, di
                while True:
                    visited[(x,y,di)] = True
                    nx = (x + d[di][0])%rows
                    ny = (y + d[di][1])%cols
                    if grid[nx][ny] == 'S':
                        nd = di
                    elif grid[nx][ny] == 'L':
                        nd = (di-1)%4
                    else:
                        nd = (di+1)%4
                    if visited[(nx,ny,nd)]:
                        results.append(length)
                        break
                    length += 1
                    x,y,di = nx,ny,nd
    results.sort()
    return results

print(solution(["R","R"]))