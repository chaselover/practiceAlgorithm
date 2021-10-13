import copy

def solution(game_board, table):
    answer = 0
    
    n = len(game_board)
    delta = ((0, 1), (1, 0), (-1, 0), (0, -1))

    def dfs(graph, x, y, position, num):
        ret = [position]
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == num:
                graph[nx][ny] = 2
                ret += dfs(graph, nx, ny, [position[0] + dx, position[1] + dy], num)
        return ret

    # 빈칸 찾기
    block = []
    for i in range(n):
        for j in range(n):
            if not game_board[i][j]:
                game_board[i][j] = 1
                result = dfs(game_board, i, j, [0, 0], n, 0)[1:]
                block.append(result)

    # 회전시켜 block 맞추기
    for rotation in range(4):
        rotated_table = [list(row)[::-1] for row in zip(*table)]

        for i in range(n):
            for j in range(n):
                if rotated_table[i][j] == 1:
                    rotated_table[i][j] = 2
                    result = dfs(rotated_table, i, j, [0, 0], n, 1)[1:]
                    if result in block:
                        block.pop(block.index(result))
                        answer += (len(result) + 1)
                        table = copy.deepcopy(rotated_table)
                    else:
                        rotated_table = copy.deepcopy(table)
    return answer



# 2
from collections import Counter
from dataclasses import dataclass
from itertools import product


@dataclass(frozen=True)
class Pos:
    x: int
    y: int

    def neighbors(self):
        return [
            Pos(self.x, self.y - 1),
            Pos(self.x + 1, self.y),
            Pos(self.x, self.y + 1),
            Pos(self.x - 1, self.y),
        ]


def make_tile_from_positions(positions):
    """Smallest possible representation with rotation"""

    def rotate90(tile):
        return tuple(
            tuple(tile[i][j] for i in range(len(tile)))
            for j in reversed(range(len(tile[0])))
        )

    positions = set(positions)

    xs = [pos.x for pos in positions]
    min_x = min(xs)
    max_x = max(xs)

    ys = [pos.y for pos in positions]
    min_y = min(ys)
    max_y = max(ys)

    tile_representations = [
        tuple(
            tuple(Pos(i, j) in positions for j in range(min_y, max_y + 1))
            for i in range(min_x, max_x + 1)
        )
    ]

    for __ in range(3):
        tile_representations.append(rotate90(tile_representations[-1]))

    return min(tile_representations)


def get_tile_size(tile):
    return sum(sum(row) for row in tile)


def parse_tiles(board, tile_value=1):
    n = len(board)

    # Add sentinel boundaries
    sentinel = 1 - tile_value

    board = [
        [sentinel] * (n + 2),
        *([sentinel] + row + [sentinel] for row in board),
        [sentinel] * (n + 2),
    ]

    # Detect tiles
    tile_positions = []
    for i, j in product(range(1, n + 1), range(1, n + 1)):
        if board[i][j] == tile_value:
            stack = [Pos(i, j)]
            squares = []
            while stack:
                curr = stack.pop()
                board[curr.x][curr.y] = sentinel
                squares.append(curr)
                for neighbor in curr.neighbors():
                    if board[neighbor.x][neighbor.y] == tile_value:
                        stack.append(neighbor)
            tile_positions.append(squares)

    # Make tiles
    tiles = [make_tile_from_positions(p) for p in tile_positions]

    return tiles


def solution(game_board, table):
    tiles = parse_tiles(table, 1)
    empty_spaces = parse_tiles(game_board, 0)

    tile_counter = Counter(tiles)
    empty_space_counter = Counter(empty_spaces)

    used_tiles = tile_counter & empty_space_counter

    return sum(get_tile_size(tile) * occ for tile, occ in used_tiles.items())

import numpy as np
from collections import deque


def pull_left_top(d:np.array):
    while np.count_nonzero(d[:, :1]) == 0:
        d = np.roll(d, shift=-1)
    while np.count_nonzero(d[:1, :]) == 0:
        d = np.roll(d, shift=-1, axis=0)
    return d


def block_split(block, x, y):
    q = deque()
    q.append((x, y, 0))
    visit = np.zeros_like(block)
    visit[x][y] = 1
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    l = len(block)

    while q:
        x, y, d = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or ny < 0 or nx >= l or ny >= l:
                continue
            if block[nx][ny] == 1 and visit[nx][ny] == 0: # 이어진 2\1
                q.append((nx, ny, d+1))
                visit[nx][ny] = 1
                block[nx][ny] = 0

    return pull_left_top(visit)


def match(hole, block):
    for _ in range(4):
        block = pull_left_top(np.rot90(block))
        tmp = hole - block
        if np.count_nonzero(tmp) == 0:
            return True
    return False


def solution(game_board, block):
    # blocks
    block = np.array(block, int)
    blocks = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[]}
    for i in range(len(block)):
        for j in range(len(block)):
            if block[i][j] == 1:
                b = block_split(block, i, j)
                blocks[np.count_nonzero(b)].append(b)

    # holes
    hole = 1 - np.array(game_board, int)
    holes = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[]}
    for i in range(len(block)):
        for j in range(len(block)):
            if hole[i][j] == 1:
                h = block_split(hole, i, j)
                holes[np.count_nonzero(h)].append(h)
    result = 0

    for i in range(1, 7):
        for h in holes[i]:
            for j, b in enumerate(blocks[i]):
                if match(h, b):
                    result += i
                    blocks[i].pop(j)
                    break

    return result



# 3
from collections import defaultdict

block_hashs = [0] * 4
block_size = 0

def solution(game_board, table):
    N = len(game_board)
    row_base = 1 << 1
    column_base = 1 << N
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    global block_hashs

    def dfs(board, x, y):
        visited[x][y] = 1
        global block_size, block_hashs
        block_size += 1
        row_exponent = [x, N - y, N - x, y]
        column_exponent = [y, x, N - y, N - x]
        for k in range(4):
            block_hashs[k] += ((row_base ** row_exponent[k]) *
                               (column_base ** column_exponent[k]))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < N and 0 <= ny < N):
                continue
            if not board[nx][ny] or visited[nx][ny]:
                continue
            dfs(board, nx, ny)

    def process_hash(hash_values):
        for i, hash_value in enumerate(hash_values):
            for hash_base in [row_base, column_base]:
                while hash_value % hash_base == 0:
                    hash_value //= hash_base
            hash_values[i] = hash_value
        return min(hash_values)

    visited = [[0] * N for _ in range(N)]
    game_board_inverted = [[1 - x for x in row] for row in game_board]
    game_board_hash = defaultdict(int)
    block_size_by_hash = {}
    for x in range(N):
        for y in range(N):
            if not game_board_inverted[x][y] or visited[x][y]:
                continue
            block_hashs = [0] * 4
            global block_size
            block_size = 0
            dfs(game_board_inverted, x, y)
            block_hash = process_hash(block_hashs)
            game_board_hash[block_hash] += 1
            block_size_by_hash[block_hash] = block_size

    visited = [[0] * N for _ in range(N)]
    answer = 0
    for x in range(N):
        for y in range(N):
            if not table[x][y] or visited[x][y]:
                continue
            block_hashs = [0] * 4
            dfs(table, x, y)
            block_hash = process_hash(block_hashs)
            if game_board_hash[block_hash] > 0:
                game_board_hash[block_hash] -= 1
                answer += block_size_by_hash[block_hash]
    return answer


def rotate(piece):
    return [[x[i] for x in reversed(piece)] for i in range(len(piece[0]))]

def seek(board, target):
    pieces = []
    length = len(board)
    for i in range(length):
        for j in range(length):
            if board[i][j] == target:
                coord = []
                stack = [[i, j]]
                while stack:
                    pivot = stack.pop()
                    coord.append(pivot)
                    board[pivot[0]][pivot[1]] = 1 - target
                    if pivot[0] != 0:
                        if board[pivot[0]-1][pivot[1]] == target:
                            stack.append([pivot[0]-1, pivot[1]])
                    if pivot[1] != 0:
                        if board[pivot[0]][pivot[1]-1] == target:
                            stack.append([pivot[0], pivot[1]-1])
                    if pivot[0] != length-1:
                        if board[pivot[0]+1][pivot[1]] == target:
                            stack.append([pivot[0]+1, pivot[1]])
                    if pivot[1] != length-1:
                        if board[pivot[0]][pivot[1]+1] == target:
                            stack.append([pivot[0], pivot[1]+1])
                max_row = max([x[0] for x in coord])
                min_row = min([x[0] for x in coord])
                max_col = max([x[1] for x in coord])
                min_col = min([x[1] for x in coord])
                coord = [[x[0]-min_row, x[1]-min_col] for x in coord]
                piece = [[1 if [i, j] in coord else 0 for j in range(max_col-min_col+1)] for i in range(max_row-min_row+1)]
                pieces.append(piece)
    return pieces

def match(blank, piece):
    if len(blank) == len(piece) and len(blank[0]) == len(piece[0]):
        if blank == piece:
            return True
        if blank == rotate(rotate(piece)):
            return True
    if len(blank) == len(piece[0]) and len(blank[0]) == len(piece):
        if blank == rotate(piece):
            return True
        if blank == rotate(rotate(rotate(piece))):
            return True
    return False

def solution(game_board, table):
    answer = 0
    blanks = seek(game_board, 0)
    pieces = seek(table, 1)
    while pieces:
        piece = pieces.pop()
        for i in range(len(blanks)):
            if match(blanks[i], piece):
                del blanks[i]
                answer += sum([sum(x) for x in piece])
                break
    return answer