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
test_file = "test2.in"

import sys, os, platform

# only if executed on Python 3.11 (gitpod), will be false on france-ioi
if True:
    os.chdir(os.path.dirname(__file__))
    sys.stdin = open(os.path.join("tests", test_file), "r")
##################################################################
from sys import stdin

def harvester():
    nb_manteaux = int(input())
    manteaux = [
        (tuple(map(int, intervalle.split())), manteau)
        for manteau, intervalle in zip(range(nb_manteaux), stdin)
    ]
    manteaux = [(debut, -fin, manteau) for (debut, fin), manteau in manteaux]
    return nb_manteaux, manteaux


def begin_sort(manteaux, nb_manteaux):
    manteaux.sort()
    by_start = [None] * nb_manteaux
    for position, (_, _, manteau) in enumerate(manteaux):
        by_start[manteau] = position
    return by_start


def end_sort(manteaux, nb_manteaux):
    manteaux.sort(key=lambda x: (x[1], x[0], x[2]))
    by_end = [None] * nb_manteaux
    for position, (_, _, manteau) in enumerate(manteaux):
        by_end[manteau] = position
    return by_end


def get_best_manteaux(by_start, by_end):
    sommePosMin = 1 << 19
    for posDebut, posFin in zip(by_start, by_end):
        sommePosMin = min(sommePosMin, posDebut + posFin)
    return sommePosMin


def main():
    nb_manteaux, manteaux = harvester()
    by_start = begin_sort(manteaux, nb_manteaux)
    by_end = end_sort(manteaux, nb_manteaux)
    sommePosMin = get_best_manteaux(by_start, by_end)

    print(nb_manteaux - sommePosMin - 1)


if __name__ == "__main__":
    main()
