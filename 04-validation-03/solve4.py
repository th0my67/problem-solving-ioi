
def fillBoard(board: list):
    if not board:
        return []
    board[:-1] = fillBoard(board[:-1])
    board[:-2] = clearBoard(board[:-2])
    board[-1] = 1
    print(len(board))
    board[:-2] = fillBoard(board[:-2])
    return board


def clearBoard(board: list):
    if not board:
        return []
    board[:-2] = clearBoard(board[:-2])
    board[-1] = 0
    print(len(board))
    if len(board) > 1:
        board[:-2] = fillBoard(board[:-2])
        board[:-1] = clearBoard(board[:-1])
    return board




def fastClear(n: int):
    if 1 > n:
        return
    fastClear(n-2)
    print(n)
    if n > 1:
        fastFill(n-2)
        fastClear(n-1)
    return

def fastFill(n: int):
    if 1 > n:
        return
    fastFill(n-1)
    fastClear(n-2)
    print(n)
    fastFill(n-2)
    return

fastClear(4)