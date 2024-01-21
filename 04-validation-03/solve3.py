def fillBoard(Board: list):
    if not Board:
        return []
    Board[:-1] = fillBoard(Board[:-1]) 
    Board[:-2] = clearBoard(Board[:-2])
    Board[-1] = 1
    print(len(Board))
    return Board


def clearBoard(Board: list):
    if not Board:
        return []
    Board[:-2] = clearBoard(Board[:-2]) 
    Board[-1] = 0
    print(len(Board))
    if len(Board) > 1:
        Board[:-2] = fillBoard(Board[:-2])
        Board[:-3] = clearBoard(Board[:-3])
        Board[-2] = 0
        print(len(Board)-1)
    return Board


def solve(Board: list):
    if not Board:
        return []
    Board = clearBoard(Board)
    Board[:-2] = fillBoard(Board[:-2])
    solve(Board[:-1])
    return Board


global Board
Board = [1] * 4

solve(Board)
