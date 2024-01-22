def get_value(x, y, board):
    if y >= 0 and y < len(board):
        if x >= 0 and x < len(board[0]):
            return board[y][x]
    return 0


def compute_o_map(plan):
    o_map = [[0] * len(plan[0]) for _ in range(len(plan))]

    for y, row in enumerate(plan):
        for x, value in enumerate(row):
            o_map[y][x] = get_value(x, y - 1, o_map) + get_value(x - 1, y, o_map) - get_value(x - 1, y - 1, o_map) + value

    return o_map


def get_max_size(o_map):
    max_size = 0

    for y, row in enumerate(o_map):
        if max_size >= len(o_map) - y:
            break
        for x in range(len(row)):
            if max_size >= len(o_map) - x:
                break

            while get_value(x - 1, y - 1, o_map) - get_value(x + max_size - 1, y - 1, o_map) - get_value(x - 1, y + max_size - 1, o_map) + get_value(x + max_size - 1, y + max_size - 1, o_map) == 0:
                max_size += 1
    return max_size

def solve():
    row, col = (int(x) for x in input().split())
    plan = [list(map(int,input().split())) for _ in range(row)]
    print(get_max_size(compute_o_map(plan)))
