"""

Template for France-IOI programming tasks with debugger in gitpod

The Python version on gitpod is 3.11, whereas the python version on france-ioi
is sadly stuck at 3.4.2 ... This means no type hints, no dataclasses, ... The
code should therefore remain pretty basic to run flawlessly on france-ioi

"""

##################################################################
# read input from file tests/test1.in as if type on the keyboard
# This shouldn't run on France-IOI
# replace this with the name of your test file
test_file = "test1.in"

import sys, os, platform

# only if executed on Python 3.11 (gitpod), will be false on france-ioi
if platform.python_version_tuple()[:2] == ("3", "11"):
    os.chdir(os.path.dirname(__file__))
    sys.stdin = open(os.path.join("tests", test_file), "r")
##################################################################


from collections import namedtuple

Problem = namedtuple("Problem", [])


def parse_input():
    """

    Parses the input data and returns a dictionary with everything
    well structured.

    """
    row, col = map(int, input().split())
    board = (input().split() for _ in range(row))

    return Problem((row, col), board)


def solve(problem):
    
    small_board=size_reducer(problem[1])
    if 0 in small_board:
        zeroPos=[]
        for y , row in enumerate(small_board):
            for x , value in enumerate(row):
                if 0 is value:
                    zeroPos.append((x,y))

                


    return result


def size_reducer(board):
    chunk_size = min(len(board), len(board[0])) // 11
    reduced_board = [[0] * 12 for _ in range(12)]
    for x in range(12):
        for y in range(12):
            reduced_board[y][x] = get_chunk(board, x, y, chunk_size)

    return reduced_board


def get_chunk(board, x, y, size):
    return len(set(row[x : x + size] for row in board[y : y + size])) == 1


def output(result):
    for r in result:
        print(r)


if __name__ == "__main__":
    problem = parse_input()
    result = solve(problem)
    output(result)
